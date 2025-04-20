Import Data from Amazon Lightsail - MySQL
If you have your data stored in Amazon Lightsail Cloud Database, then you can easily import your data into Zoho Analytics for reporting & analysis. Zoho Analytics allows you to either import the data into Zoho Analytics, or connect directly with the Amazon Lightsail server.
Data Import: In this mode, the data will be imported and stored in Zoho Analytics. You can set up periodic schedules to fetch the latest data automatically from your Amazon Lightsail database. Report loading time will depend on the amount of data stored in Zoho Analytics.
Live Connect: In this mode, data will not be fetched from Amazon Lightsail and stored in Zoho Analytics. Instead, for the reports that you create, Zoho Analytics will generate appropriate queries. These queries will connect the required data live from Amazon Lightsail to Zoho Analytics and show you the report. In this case, the loading time will directly depend on the performance of Amazon Lightsail.
Data Import
- How do I import data from Amazon Lightsail?
- How do I schedule import for Amazon Lightsail?
- How do I edit the setup?
- What happens when data import or data sync fails?
- Can I import data from Views created in Amazon Lightsail - MySQL (apart from Tables) into Zoho Analytics?
- Can I blend data from other data sources into the Amazon Lightsail workspace?
- How to remove the data source?
Live Connect
- How do I connect live with the Amazon Lightsail - MySQL
- How is Live Connect different from Data Import?
- How to edit the live connect setup?
- Will the reports/dashboards query hit my database server every time I open it, or can it be cached in Zoho Analytics?(or) Can I store a cache of my data points in Zoho Analytics to get quick access to my views?
- Can I connect Views created in the Amazon Lightsail database (apart from Tables) to Zoho Analytics?
- Will foreign keys defined between my tables in the Amazon Lightsail database be linked in Zoho Analytics as well?
- I got an alert message, "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
- What is a Mismatch?
- When do Mismatches occur and how to resolve them?
- Can I connect new columns added in my Amazon Lightsail database to Zoho Analytics?
- Can I change the data type of the columns in Zoho Analytics?
- Can I create Query Tables over the Amazon Lightsail data?
- What happens when I delete or rename the database in the Amazon Lightsail database?
- How do I remove the Amazon Lightsail Live Connection with Zoho Analytics setup?
- What are the limitations of using the Amazon Lightsail database Live Connect?
Data Import
1. How do I import data from Amazon Lightsail?
Note: After initiating the import process, you might have to wait sometime for the initial fetch to happen. The time taken depends upon the amount of data to be imported into Zoho Analytics, and also the response time of the database server.
You will receive an email notification once the import is complete. Please note that if you access the workspace before the initial fetch, it will not display any data.
2. How do I schedule import for Amazon Lightsail?
Zoho Analytics provides flexible sync frequencies like hourly, daily, weekly, and monthly to ensure that your data is always up-to-date for effective analysis.
Users can schedule import,
Additionally, it also provides the following options to customize the data import settings:
- Incremental Fetch (new records or modified records): In this method, only the newly added records are imported in each sync schedule. This is useful when the data source has transactional data that gets updated frequently. Refer to the Incremental Fetch article, to learn more.
- All records: In this method, all the records are imported in each sync schedule.
3. How do I edit the setup?
Users with administrator privileges can view and edit the connection settings by accessing the Data Sources tab.
The Data Sources tab includes the following details:
- Data Sync Status: Indicates whether the synchronization is currently active, completed, or if there are any errors/issues.
- Last Sync Time: Displays the timestamp of the most recent synchronization.
- Next Sync Time: Displays the timestamp of when the next sync is set to occur.
- Sync frequency: Displays how often the synchronization happens.
Modify Connection Details and Sync Settings
- Access the Data Sources tab on the side navigation bar.
- All the data sources in the workspace will be listed. Choose the data source you want to edit
- Click Edit Connection to modify the connection details and then click Save.
- Click Sync Settings to schedule import or modify the sync frequency.
Modify import synchronization settings
Zoho Analytics provides comprehensive details about the table settings like the Table Name, Source Table Name, What data is fetched, Time and Sync status.
To modify the Table level settings,
- Access the Data Sources tab
- Hover the mouse over the table where you want to modify the settings.
- Sync Now: Click the Sync Now icon to include the recent changes made in the data source.
- Edit synchronization settings: Click the Edit icon to change the import settings.
- Delete table: Click the Delete icon to remove the connection.
- Last Import Details: Click the Information icon to view the last import details of the table.
4. What happens when data import or data sync fails?
In the case of continuous import failure, an email will be sent to the registered address with the reason for failure and solution. The Data Sources tab will also list the sync failure details. Refer to Edit Connection section to resolve import and sync failures.
You can also choose to notify other administrators and custom users about the data sync failure.
5. Can I import data from Views created in Amazon Lightsail - MySQL (apart from Tables) into Zoho Analytics?
Yes, you can import data from Tables as well as Views available in your Amazon Light sail MySQL database into your Zoho Analytics workspace.
6. Can I blend data from other data sources into the Amazon Lightsail workspace?
Yes, Zoho Analytics allows you to blend data from various sources.
Import data into an existing table
- Click Import > Import data into this table.
- Select the table you want to import.
- Choose how you want to import the records.
Import Data into an existing Workspace:
Refer to the setup presentation, for importing data into an existing workspace.
7. How to remove the data source?
When you remove a data source, there will be no connection between the source application and Zoho Analytics. However, the tables and the data will be available in the workspace and no further synchronization will happen.
To remove the data source,
- Click Data Sources > Settings.
- Choose Remove Data Source from the drop-down list.
Live Connect
1. How do I connect live with the Amazon Lightsail - MySQL
2. How is Live Connect different from Data Import?
Tabulated below are the differences between the Data Import feature and Live Connect feature.
| Data Import | Live Connect |
| Data in Amazon Lightsail will be imported and stored in Zoho Analytics. | Data from Amazon Lightsail will be fetched live using appropriate reporting queries whenever you create or access a report in Zoho Analytics. |
| Filtered data set can be imported from Amazon Lightsail using customized queries. | Custom Query feature is not available in Amazon Lightsail Live Connect. However, you can create Views in the source database and connect the same with Zoho Analytics. |
| Multiple data sources (apart from Amazon Lightsail) can be imported into the same workspace and they can be combined for reporting & analysis purpose. | Cannot import data from any other data source into the same workspace in which Live Connect from Amazon Lightsail is setup. |
| Changes made to the columns such as addition/deletion will be synchronized automatically. | Any changes such as column addition/deletion/renaming will not be reflected. You will have to manually map the data using the Sync Design option. |
| When importing multiple tables, the foreign keys defined between the tables in the Amazon Lightsail database will not be linked in Zoho Analytics. However, you can manually link the tables in Zoho Analytics using the Look-up column feature. | Look-up relationship will be automatically created for tables that are linked via foreign keys in the Amazon Lightsail database. You can also manually link the tables in Zoho Analytics using Look-up column feature. |
| Users can create query tables. | Users cannot create query tables. |
| Report loading time will be fast as the data is stored in Zoho Analytics. | Report loading time directly depends on the Amazon Lightsail server response time and the amount of data in Amazon Lightsail. |
3. How to edit the live connect setup?
Access the Data source tab to modify the connection settings.
- Add tables: Click Add more tables to include the new tables added to the source database.
- Sync changes: Click Sync to include the recent changes made to the data.
- Delete table: Click Delete to remove live connect for a table.
4. Will the reports/dashboards query hit my database server every time I open it, or can it be cached in Zoho Analytics?
(or) Can I store a cache of my data points in Zoho Analytics to get quick access to my views?
Zoho Analytics allows you to create a cache for the reports in your live connect database to reduce the query fetching time.
To enable cache for your Live Connect workspace, please follow the below steps:
- From your Workspace Explorer, click the Settings tab from the side menubar.
- In the General - Workspace Settings page that opens, choose Yes for Enable Cache for this Workspace.
- In the Cache Refresh Interval in Minutes field, specify the duration to refresh the report.
- Click Save & Close.
A cache for the reports will be created for the Workspace.
5. Can I connect Views created in the Amazon Lightsail database (apart from Tables) to Zoho Analytics?
Yes, you can connect with both Views and Tables created in the Amazon Lightsail database to Zoho Analytics.
6. Will foreign keys defined between my tables in the Amazon Lightsail database be linked in Zoho Analytics as well?
Yes. In case you have linked two or more tables in your Amazon Lightsail database using foreign keys, they will be linked automatically using a Look-up column in Zoho Analytics as well.
Note: The lookups created/modified in the added (linked with Zoho Analytics) tables will not be reflected in Zoho Analytics (even with Sync Design option). You need to create the lookup in Zoho Analytics manually. However, the lookup information will be created in Zoho Analytics when new tables are linked.
7. I got an alert message, "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
This alert message will be displayed when Zoho Analytics is not able to access the information from the Amazon Lightsail database. This could be because the tables/columns that you are trying to access in Zoho Analytics are deleted or renamed in the Amazon Lightsail database.
In this case, we recommend you to remap the table/column. Refer to mismatch section to know how to remap a table.
8. What is a Mismatch?
When you have created reports in Zoho Analytics over the tables or columns which no longer have a direct mapping in the Amazon Lightsail database, it will be listed as a mismatch.
So, ensure that the tables/columns in Zoho Analytics workspace and Amazon Lightsail database match. The tables/columns that do not match will be listed in the Mismatch tab of the Cloud Database Connection Settings page.
9. When do Mismatches occur and how to resolve them?
10. Can I connect new columns added in my Amazon Lightsail database to Zoho Analytics?
Yes, you can connect the new columns that are added in your Amazon Lightsail database to Zoho Analytics from the Local Database Connection Settings page.
Note: If there exists a mismatch between the already available data in your Zoho Analytics workspace and your Amazon Lightsail database, Zoho Analytics will NOT be able to fetch the new column information. In this case, you need to first resolve the mismatches to connect to the new columns.
11. Can I change the data type of the columns in Zoho Analytics?
No, you cannot change the data type of the columns in Zoho Analytics while using the Live Connect option.
12. Can I create Query Tables over the Amazon Lightsail data?
No, you will not be able to create Query Tables if you have setup the workspace using the Live Connect option. This is because this option does not fetch and store the data locally in Zoho Analytics. If you wish to create Query Tables, you can create the required query as a view in the data source (Amazon Lightsail database, in this case) and connect the same with Zoho Analytics.
13. What happens when I delete or rename the database in the Amazon Lightsail database?
When you delete or rename a database in the Amazon Lightsail database, Zoho Analytics loses connectivity with the Amazon Lightsail database. After that, a warning message as shown below, will be displayed. This error message will also be displayed if there are any connectivity issues, or if your Amazon Lightsail database credentials have expired.
14. How do I remove the Amazon Lightsail Live Connection with Zoho Analytics setup?
You have to delete the workspace in Zoho Analytics to remove the connection setup.
To delete the workspace,
- Log in to Zoho Analytics
- Click the More Actions icon that appears on mouse hover adjacent to the workspace name that you want to delete.
- Click the Delete Workspace option.
15. What are the limitations of using the Amazon Lightsail database Live Connect?
Given below are a few shortcomings that one might face while using the Amazon Lightsail database Live Connect option.
- Data from your Amazon Lightsail database will NOT be locally stored in Zoho Analytics. Zoho Analytics will generate appropriate queries to fetch the required data live from the Amazon Lightsail database and show you the report. Hence, the loading time will directly depend on the performance of the Amazon Lightsail database server.
- Any changes such as column addition/deletion/renaming will not be mapped automatically. The user must manually map the updates made.
- Users cannot combine data from other data sources into the same workspace in which they have connected the Amazon Lightsail database.
- Users cannot create query tables.
- Users cannot change the data type of the columns in Zoho Analytics.