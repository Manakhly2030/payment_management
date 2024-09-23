**Accounts Payable with Payment Management Report**
---------------------------------------------------

**Problem Statement**

The Accounts Payable report in ERPNext provides a comprehensive overview of all outstanding payables to suppliers. Now out of these payable, the management or finance head may want to decide which invoices to be processed today. If action is based various factors including total payment that they can process based on bank balance.

Currently there is no easy way to give instructions to process specific outstanding payments to the accounts team from accounts payable report. This new report tries to solve this problem.

**Introduction**

This report is identical to Accounts Payable report, but it adds additional features of allowing user to choose payments to be processed, shows total amount of chosen payments to compare it with bank balance and process payments by creating draft payment entry or payment order directly from the report.

**Access the report:**

1.  Search for "Accounts Payable with Payment Management Report" in ERPNext.
    
2.  The report will load, displaying the relevant data
    
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcd2R0ERydfAXGbd31UYCho1hNAoELSClTPxfzRlGYiquRUAoM1agByahzFdc_g8cnLMUc1ZbTzb02deUqebTnbkyLX6alf0P_j4nBzwsqahYo8q2rPzRuzYlUk6YY3qkiEe_hTocN2NEqBSwevXnvhzZx7PAGGXRmc3hfBOA?key=o2pLARlkV8oC0DpOaWuWPA)

**Using the Report Filters**

All filters in this report function as standard filters in the ERPNext Accounts Payable report.

1.  Group By Supplier: When this filter is applied, the data is displayed as grouped by supplier.
    
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcbphW5iVOTsGn6uWzELtcWQIbKX4sKNUnGf1L6RqeuEyaJSkez8ddBVk_jHBbHWWfD9hjovCv3eo9jjXIKYv5_akwtjBCe-VeyIMqrp5lmJYc2YoKFCdDX1wFoyv9CEHvIcTQF2Xkmabu24iqvOzNgW8xx1HRWJNyKr8U4KA?key=o2pLARlkV8oC0DpOaWuWPA)

**Creating Payment Entries:**

1.  **Selecting Rows:** Select the rows corresponding to the invoices you want to pay. The system adds the amount of each selected invoice to the number card, showing the total amount to be paid
    
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcbphW5iVOTsGn6uWzELtcWQIbKX4sKNUnGf1L6RqeuEyaJSkez8ddBVk_jHBbHWWfD9hjovCv3eo9jjXIKYv5_akwtjBCe-VeyIMqrp5lmJYc2YoKFCdDX1wFoyv9CEHvIcTQF2Xkmabu24iqvOzNgW8xx1HRWJNyKr8U4KA?key=o2pLARlkV8oC0DpOaWuWPA)
2.  **Number Card:** Displays the total amount of the selected invoices. Additionally, “Actions” Button will be visible at the upper right corner of the report.
    
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcYmMXCpfz7X4HiZCPhFLMRGMlyxzvLwHOkS3F6e_G20eckVH0NrsNk8WcZbZnWu-3P13IiQcxyFm8_fQvtFh9RlxAQtKyVbIs4mDmcNR1P971GQTFtzLpXJcxh98JA5S83IML-cTaBc3psIUIkvAvTtEBI_xxY0OZEeL9f1g?key=o2pLARlkV8oC0DpOaWuWPA)
3.  **Creating Payment Entries:**
    
    1.  Click on the Action button.
        
    2.  Select Create Payment Entry.
        
    3.  The system will create a payment entry for each selected supplier.
        
    4.  Once the message appears following payment entry creation, clicking the payment entry link will take you to the relevant Payment Entry
        
    
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdFAPuna1WNXs9Q4zfCIVuhsTgTYsx-h3AXtw868rfDcfVYBXy0DKNlkhW2xlMJUg_rgayEdrSVA8zIjh5jxmyntP3zID4R33d9_Iw2Z6a5AbDmu-g3bv5BKJpePI56JPJlBXVn43bIrjac5TkexrEYohtNq5AheamH-lDsPQ?key=o2pLARlkV8oC0DpOaWuWPA)

**Additional Features**

1.  **Handling Multiple Documents:** If you have both Purchase Invoices and Journal Entries in the system, you can select rows for both. The system will create a payment for each selected document.
    
2.  **Create Payment Request:** There is a Create Payment Request option within the Action button to automatically generate payment requests.
    
    ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdsKt0-n6fv4Dd7TrivFE6WFKf_36t4H25oIyHJ320HOlVC1ikDtWSBLCG1oC3GcfQa_kRE2T17BHKcf9moeVrNZfPk30QOfakXLxT-5NaGb-kmMpaGtkl5t9KWsZrsD6oUM2-HLQhcXY-wh2p2lR5F3XQ12q9Tou6A6H1Q?key=o2pLARlkV8oC0DpOaWuWPA)

**Conclusion**

The Accounts Payable with Payment Management report is an essential tool for financial management, providing a clear view of outstanding payables and facilitating eƯicient payment processing. By using this report, businesses can ensure timely payments and maintain good relationships with suppliers
