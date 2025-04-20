Import data from Microsoft Azure SQL Data Warehouse
If you have your data stored in Microsoft Azure SQL Data Warehouse Cloud Database, then you can easily import your data into Zoho Analytics for reporting & analysis. You can also set up schedules to fetch the latest data from your Microsoft Azure SQL Data Warehouse database periodically.
Data Import: Data in Microsoft Azure Data Warehouse will be imported and stored in Zoho Analytics. You can setup periodic schedules to fetch the latest data automatically from your Microsoft Azure Data Warehouse database. Report loading time will be faster as the data is stored in Zoho Analytics.
Live Connect: In this mode, data will not be fetched from Microsoft Azure Data Warehouse and stored in Zoho Analytics. Instead for the reports that you create Zoho Analytics will generate appropriate queries that will connect the required data live from Microsoft Azure Data Warehouse to Zoho Analytics and show you the report. In this case the loading time will directly depend on the performance of Microsoft Azure Data Warehouse.
Data Import
- Preamble: Why should I allowlist Zoho Analytics IP address and how do I do it?
- How do I import data from the Microsoft Azure SQL Data Warehouse database?
- How can I edit the setup?
- How long does it take for the data to be imported into Zoho Analytics?
- Can I import data from Views created in Microsoft Azure SQL Data Warehouse (apart from Tables) into Zoho Analytics?
- Will foreign keys defined between my tables in the Microsoft Azure SQL Data Warehouse database be linked in Zoho Analytics as well?
- Can I change the data-type of the columns in Zoho Analytics?
- I have synced data from a database into a table. Can I change the data source of this table?
- Can I import data from my Microsoft Azure SQL Data Warehouse database into an existing Zoho Analytics workspace?
- Can I synchronize the data from my Cloud Database instantly?
- How do I remove the Setup?
Live Connect
- Preamble: Why should I allowlist Zoho Analytics IP address and how do I do it?
- How do I connect live with the Microsoft Azure Data Warehouse database?
- How can I edit the live connect setup?
- How is Live Connect different from Data Import?
- How long does it take for me to visualize my data in Zoho Analytics?
- Will the reports/dashboards query hit my database server every time I open it or can it be cached in Zoho Analytics?
- Can I connect Views created in Microsoft Azure Data Warehouse (apart from Tables) to Zoho Analytics?
- Will foreign keys defined between my tables in Microsoft Azure Data Warehouse database be linked in Zoho Analytics as well?
- Can I link the related tables, connected from the Cloud Database using the Live Connect option, in Zoho Analytics?
- I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
- What is a Mismatch?
- When do Mismatches occur and how to resolve them?
- Can I synchronize the meta data of the table from my Cloud Database instantly?
- Can I connect the new columns added in my Microsoft Azure Data Warehouse database to Zoho Analytics?
- Can I change the data type of the columns in Zoho Analytics?
- Can I import data from other data sources into the same workspace that I have used to connect with Microsoft Azure Data Warehouse?
- Can I create Query Tables over the Microsoft Azure Data Warehouse data?
- What happens when I delete or rename the database in Microsoft Azure Data Warehouse?
- How do I remove the Setup?
- What are the limitations of Microsoft Azure Data Warehouse Live Connect?
Data Import
1. Preamble: Why should I allowlist Zoho Analytics IP addresses and How do I do it?
2. How do I import data from the Microsoft Azure SQL Data Warehouse database?
3. How can I edit the setup?
4. How long does it take for the data to be imported into Zoho Analytics?
After setup, you might have to wait sometime for the initial fetch to happen. This depends upon the amount of data to be imported into Zoho Analytics and also the response time of your Microsoft Azure SQL Data Warehouse server. You will receive an email notification once the import is complete. Please note that, if you access the workspace before the initial fetch, it will not display any data.
5. Can I import data from Views created in Microsoft Azure SQL Data Warehouse (apart from Tables) into Zoho Analytics?
Yes, you can import data from both Views and Tables into Zoho Analytics.
6. Will foreign keys defined between my tables in the Microsoft Azure SQL Data Warehouse database be linked in Zoho Analytics as well?
When importing multiple tables, the foreign keys defined between the tables in Microsoft Azure SQL Data Warehouse database will be linked in Zoho Analytics. The foreign keys will be created as Look-up columns in Zoho Analytics.
If you import data from one table at a time (choosing single table option) then the foreign keys will not be defined. However, you can manually link the tables in Zoho Analytics using the Look-up column feature. Click here to learn about the Look-up column feature.
7. Can I change the data-type of the columns imported in Zoho Analytics?
Yes, you can change the datatype of the columns imported into Zoho Analytics. However it is necessary that the data-type of your column is compatible with the data-type of the column in your Microsoft Azure SQL Data Warehouse database for successful data synchronizations. It is always recommended that you change the data type in both your Microsoft Azure SQL Data Warehouse database as well as your Zoho Analytics workspace.
8. I have synced data from a database into a table. Can I change the data source of this table?
Yes, you can change the data source of a table, into which the Microsoft Azure SQL Data Warehouse database has been synced.
Follow the below steps to import if the source is available in the same Microsoft Azure SQL Data Warehouse database that is imported into the table.
- Open the Workspace.
- Click Import Data> Import into this Table.
- The Select Data to Import tab of Import wizard will open.
- You can choose to import from a different table using the Select Table option or import using the Custom Query.
Follow the below steps to import if the source is available in a different local database.
- Open the Workspace.
- Click Data Source from the left bar.
- All data sources for this Workspace will be listed. Click the data source you want to edit.
- The Data Source page will open. Click Edit Connection.
- In the Cloud Database - Edit Connection dialog that open, modify the data source. You can also change the Databridge that fetches the data.
9. Can I import data from my Microsoft Azure SQL Data Warehouse database into an existing Zoho Analytics workspace?
Yes. Follow the below steps to import data into an existing workspace:
- Open the Workspace into which you wish to import the data.
- Navigate through Create > Import Data.
- Click the Cloud Databases option.
Configuring the import will be similar to the steps followed in this presentation.
10. Can I synchronize the data from my Cloud Database instantly?
Yes, you can synchronize your data from Cloud Database instantly when needed.
To synchronize your data instantly:
- Login to your Zoho Analytics account.
- Open the corresponding Workspace.
- From the home page, click Data Source tab. The Data Source page will open.
- Click Sync Now link.
11. How do I remove the Setup?
To remove the setup,
- Login to your Zoho Analytics account.
- Open the corresponding Workspace.
- From the home page, click Data Source tab. The Data Source page will open.
- Click the Settings icon.
- Select Remove Data Source from the drop-down menu that opens.
Please note that the data source connection will be removed, but the tables and the data will be retained in the workspace. As the data source connected is removed, no further synchronization will happen.
Live Connect
1. Preamble: Why should I allowlist Zoho Analytics IP addresses and How do I do it?
Note: Click to view the entire list of IP addresses that needs to be allowlisted.
2. How do I connect live with the Microsoft Azure SQL Data Warehouse database?
3. How can I edit the live connect setup?
4. How is Live Connect different from Data Import?
Tabulated below are the differences between the Data Import feature and Live Connect feature.
| Data Import | Live Connect |
| Data in Microsoft Azure SQL Data Warehouse will be imported and stored in Zoho Analytics. | Data from Microsoft Azure SQL Data Warehouse will be fetched live using appropriate reporting queries whenever you create or access a report in Zoho Analytics. |
| Filtered data set can be imported from Microsoft Azure SQL Data Warehouse using customized queries. | Custom Query feature is not available in Microsoft Azure SQL Data Warehouse Live Connect. However, you can create Views in the source database and connect the same with Zoho Analytics. |
| Multiple data sources (apart from Microsoft Azure SQL Data Warehouse) can be imported into the same workspace and they can be combined for reporting & analysis purpose. | Cannot import data from any other data source into the same workspace in which Live Connect from Microsoft Azure SQL Data Warehouse is setup. |
| Changes made to the columns such as addition/deletion will be synchronized automatically. | Any changes such as column addition/deletion/renaming will not be reflected. You will have to manually map the data using the Sync Design option. |
| When importing multiple tables, the foreign keys defined between the tables in the Microsoft Azure SQL Data Warehouse database will not be linked in Zoho Analytics. However, you can manually link the tables in Zoho Analytics using the Look-up column feature. | Look-up relationship will be automatically created for tables that are linked via foreign keys in the Microsoft Azure SQL Data Warehouse database. You can also manually link the tables in Zoho Analytics using Look-up column feature. |
| Users can create query tables. | Users cannot create query tables. |
| Report loading time will be fast as the data is stored in Zoho Analytics. | Report loading time directly depends on the Microsoft Azure SQL Data Warehouse server response time and the amount of data in Microsoft Azure SQL Data Warehouse. |
5. How long does it take for me to visualize my data in Zoho Analytics?
As there is no data import process involved, the loading time depends upon the amount of data stored in your Microsoft Azure SQL Data Warehouse database and also the response time of your Microsoft Azure SQL Data Warehouse server.
6. Will the reports/dashboards query hit my database server every time I open it or can it be cached in Zoho Analytics?
(or) Can I store a cache of my data points in Zoho Analytics to get quick access to my views?
Zoho Analytics allows you to create a local cache of reports, created over your live connect database. This will increase the speed of loading reports as it will reduce the data fetching time from your live databaseTo enable cache for your live connect workspace, please follow the below steps:
- From your Workspace Explorer, click Settings from the side menubar.
- In the General - Workspace Settings page that opens, choose Yes for Enable Cache for this Workspace.
- In Cache Refresh Interval in Minutes, specify the duration to refresh the report .
- Click Save & Close.
A cache for the reports will be created for the Workspace.
Note:
- Enabling cache will help create a cache for your reports in the workspace. This data will get updated periodically based on the time provided in the Cache Refresh Interval in Minutes.
- You can create a cache only for the reports, and not for tables in the workspace.
- This option is available only for Live Connect.
7. Can I connect Views created in Microsoft Azure SQL Data Warehouse (apart from Tables) to Zoho Analytics?
Yes, you can connect with both Views and Tables created in Microsoft Azure SQL Data Warehouse to Zoho Analytics.
8. Will foreign keys defined between my tables in Microsoft Azure SQL Data Warehouse database be linked in Zoho Analytics as well?
Yes. In case you have linked two or more tables in your Microsoft Azure SQL Data Warehouse database using foreign keys, they will be linked automatically using a Look-up column in Zoho Analytics as well. You can also manually create a lookup relationship among the imported tables in Zoho Analytics.
Note: The lookups created/modified in the added (linked with Zoho Analytics) tables will not be reflected in Zoho Analytics (even with Sync Design option). You need to manually create the lookup in Zoho Analytics. However, the lookup information will be created in Zoho Analytics when new tables are linked.
9. Can I link the related tables, connected from the Cloud Database using the Live Connect option, in Zoho Analytics?
Yes, you can link the related tables in Zoho Analytics using the lookup column feature. Learn more.
Note:
- You will not be able to create Query Tables if you have setup the workspace using the Microsoft Azure SQL Data Warehouse Live Connect option as this option does not fetch and store the data locally in Zoho Analytics.
- The Join Tables (lookup column) option will not be available in the Import Wizard. You can create a lookup relation only on the imported tables.
10. I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
This alert message will be displayed when Zoho Analytics is not able to access the information from Microsoft Azure SQL Data Warehouse. This could be because the tables/columns that you are trying to access in Zoho Analytics is deleted or renamed in Microsoft Azure SQL Data Warehouse.
In this case, it is recommended that you remap the table/column. Refer to this presentation to know how to remap a table.
11. What is a Mismatch?
When you have created reports in Zoho Analytics over the tables or columns which no longer have a direct mapping in Microsoft Azure SQL Data Warehouse database, it will be listed as mismatch.
So, ensure that the tables/columns in Zoho Analytics workspace and Microsoft Azure SQL Data Warehouse database matches. The tables/columns that do not match will be listed in the Mismatch tab of the Microsoft Azure SQL Connection Settings page. Refer the next question to know more about mismatch.
12. When do Mismatches occur and how to resolve them?
13. Can I synchronize the meta data of the table from my Cloud Database instantly?
Yes, you can synchronize the meta data of the table from Cloud Database instantly when needed.
To synchronize the meta data instantly:
- From the workspace explorer, click the Data Sources tab.
- You will get navigated to the Microsoft Azure SQL Data Warehouse Connection Settings page. All the tables available in the workspace will be listed.
- Mouse over the required table. The option to sync the table will be displayed inline to the table name.
- Click the Sync link inline to the table name.
- The table meta data from the Cloud Database will get instantly synchronized in Zoho Analytics table.
Note: You can also synchronize all the tables available in the workspace with your Microsoft Azure SQL Data Warehouse data using the Sync Design button.
14. Can I connect new columns added in my Microsoft Azure SQL Data Warehouse database to Zoho Analytics?
Yes, you can connect the new columns that are added in your Microsoft Azure SQL Data Warehouse database to Zoho Analytics from the Microsoft Azure SQL Data Warehouse Connection Settings page. Refer to this presentation to know more.
Note: If there exists a mismatch between the already available data in your Zoho Analytics workspace and your Microsoft Azure SQL Data Warehouse database, Zoho Analytics will NOT be able to fetch the new column information. In this case, you need to first resolve the mismatches to connect to the new columns.
15. Can I change the data type of the columns in Zoho Analytics?
No, you cannot change the data type of the columns in Zoho Analytics.
16. Can I import data from other data sources into the same workspace that I have used to connect with Microsoft Azure SQL Data Warehouse?
No, you cannot import data from other data sources into the same workspace that you have used to connect with Microsoft Azure SQL Data Warehouse.
17. Can I create Query Tables over the Microsoft Azure SQL Data Warehouse data?
No, you will not be able to create Query Tables if you have setup the workspace using the Microsoft Azure SQL Data Warehouse Live Connect option. This is because this option does not fetch and store the data locally in Zoho Analytics. If you wish to create Query Tables, you can create the required query as a view in the data source and connect the same with Zoho Analytics.
18. What happens when I delete or rename the database in Microsoft Azure SQL Data Warehouse?
When you delete or rename a database in Microsoft Azure SQL Data Warehouse, Zoho Analytics loses its connectivity with Microsoft Azure SQL Data Warehouse. Thereafter, a warning message, as shown below, would be displayed. This error message will also be displayed if there are any connectivity issues or if your Microsoft Azure SQL Data Warehouse credentials have expired.
For more information regarding the same, refer to the Edit Connection presentation.
19. How do I remove the Setup?
You have to delete the workspace in Zoho Analytics to remove the connection setup.
To delete the workspace,
- From your Zoho Analytics account, click the More Actions icon that appears on mouse hover adjacent to the workspace name that you want to delete.
- Click the Delete Workspace option from the drop-down menu.
20. What are the limitations of using the Microsoft Azure Data Warehouse Live Connect?
Given below are a few short comings that one might face while using the Microsoft Azure Data Warehouse Live Connect option.
- Data from your Microsoft Azure Data Warehouse database will NOT be locally stored in Zoho Analytics. Zoho Analytics will generate appropriate queries to fetch the required data live from Microsoft Azure Data Warehouse and show you the report. Hence, the loading time will directly depend on the performance of Microsoft Azure Data Warehouse.
- Any changes such as column addition/deletion/renaming will not be mapped automatically. The user must manually map the updates made.
- Users cannot combine data from other data sources into the same workspace in which you have connected the Microsoft Azure Data Warehouse database.
- Users cannot create query tables.
- Users cannot change the data type of the columns in Zoho Analytics.