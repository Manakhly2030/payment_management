from erpnext.setup.utils import get_exchange_rate
import frappe
from collections import defaultdict
from erpnext.accounts.doctype.payment_request.payment_request import (
    get_existing_payment_request_amount,
    get_amount,
)
from frappe.utils.data import flt


@frappe.whitelist()
def create_payment_request(selected_rows):
    response = {"error": []}
    selected_rows = frappe.parse_json(selected_rows)
    grouped_by_supplier = defaultdict(list)
    for row in selected_rows:
        grouped_by_supplier[row.get("party")].append(row)

    for party, rows in grouped_by_supplier.items():
        for row in rows:
            if (
                row.get("voucher_type") is None
                or row.get("voucher_no") is None
                or row.get("voucher_type") == "Journal Entry"
            ):
                continue

            existing_payment_request_amount = get_existing_payment_request_amount(
                row.get("voucher_type"), row.get("voucher_no")
            )
            ref_doc = frappe.get_doc(row.get("voucher_type"), row.get("voucher_no"))
            if (
                not hasattr(ref_doc, "order_type")
                or ref_doc.order_type != "Shopping Cart"
            ):
                ref_amount = get_amount(ref_doc, party)
                if (
                    existing_payment_request_amount + flt(row.get("outstanding")) > ref_amount
                ):
                    response["error"].append(
                        f"Payment Request for <a href=\"{ref_doc.get_url()}\"> {row.get('voucher_no')} </a> already exists."
                    )
                    continue

            payment_request = frappe.get_doc(
                {
                    "doctype": "Payment Request",
                    "party": party,
                    "party_type": row.get("party_type"),
                    "payment_request_type": "Outward",
                    "party_type": row.get("party_type"),
                    "reference_doctype": row.get("voucher_type"),
                    "reference_name": row.get("voucher_no"),
                    "grand_total": row.get("outstanding"),
                }
            )
            payment_request.save()
    return response.get("error", "ok")


@frappe.whitelist()
def create_payment_entry(selected_rows):
    selected_rows = frappe.parse_json(selected_rows)
    grouped_by_supplier = defaultdict(list)

    for row in selected_rows:
        if not row.get("voucher_no"):
            continue
        grouped_by_supplier[row["party"]].append(row)

    for party, rows in grouped_by_supplier.items():
        references = []
        total_paid = 0
        account_currency = "USD"
        party_currency = "USD"

        for row in rows:
            total_paid += row["invoiced"]

            account_currency = row["account_currency"]
            party_currency = row["currency"]

            references.append(
                {
                    "reference_doctype": row.get("voucher_type"),
                    "reference_name": row["voucher_no"],
                    "total_amount": row["total_due"],
                    "outstanding_amount": row["outstanding"],
                    "allocated_amount": row["invoiced"],
                }
            )

        exchange_rate = get_exchange_rate(account_currency, party_currency)

        payment_entry = frappe.get_doc(
            {
                "doctype": "Payment Entry",
                "payment_type": "Pay",
                "party_type": row["party_type"],
                "party": party,
                "posting_date": row["posting_date"],
                "paid_amount": total_paid,
                "paid_to": row["party_account"],
                "received_amount": total_paid,
                "source_exchange_rate": exchange_rate or 1,
                "references": references,
            }
        )

        payment_entry.flags.ignore_mandatory = True
        payment_entry.save()

    return "ok"
