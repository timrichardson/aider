Incremental Fetch
Most of the datasets include transactional data that gets frequently updated, and importing all the data in each schedule can slow down the process of providing real-time insights. Incremental fetch for databases enables you to import only the new and updated records into Zoho Analytics.
To import data using incremental fetch, Zoho Analytics needs the following details:
- A column or field that helps in identifying the new records or rows in the table. This could be a sequential number column like ID, date, or a date and time column.
- How to import the new records into the table. You can append the new records to the table, or add records and replace them if the records already exist.
Supported Plans
Incremental fetch is available for all plans. Click here to know more about Zoho Analytics Pricing.
Supported Data Sources
Incremental fetch is currently supported only for databases.
Configuring Incremental Fetch
You can configure incremental fetch while scheduling an import. Follow the below steps to configure incremental fetch,
- Select the tables you wish to import.
- Configure the Import Settings. Click Schedule this Import.
- In the Import Synchronization Settings pane that opens, select Only new/modified records from the What Data to Fetch drop-down menu.
- All the numeric data type columns will be listed. Select the column that helps in identifying the new records.
- Select How do you want to import the data.
- Add Records at the end: Choosing this will append the new records to the end of the table.
- Add Records and replace if already exists: Updates the existing records in the table and appends the new records at the end of the table.
- Select a Column to match the existing records if you have chosen Add Records and replace if existing option from How do you want to import section. Click Next.
- The Synchronization settings pane will open. Choose the interval in which you would like to synchronize your data. You can also schedule a periodic fetch - daily, weekly or monthly - to import all the data.
While configuring incremental fetch for multiple tables, choose the column that helps in identifying the new records for each table as shown in the below image.