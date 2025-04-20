Importing from HyperSQL using Zoho Databridge
Zoho Analytics allows you to import data stored in the HyperSQL database using the Zoho Databridge. You can also automate the import process to synchronize the data from your local /hosted HSQL database into Zoho Analytics in a periodic interval. Report loading time will be faster as the data is stored in Zoho Analytics.
The Zoho Databridge bridges your local& HSQL database and Zoho Analytics server to fetch data from your local/hosted HSQL database. With this, you can also automate the import process to synchronize the data from your local/hosted HSQL database into Zoho Analytics at a periodic interval.
Data Import
- How do I install Zoho Databridge?
- How do I import data from the HSQL database using Zoho Databridge?
- How long does it take for the data to be imported into Zoho Analytics?
- How can I edit the Import setup?
- How can I schedule import from HSQL database?
- Will I be notified on import failures?
- Import from HSQL database that is hosted in the cloud has failed. How to solve this?
- Can I import data from HSQL database into an existing Zoho Analytics workspace?
- Can I import data from HSQL database into an existing table in Zoho Analytics?
- I have synced data from HSQL database into a table. Can I change the data source of this table?
- Can I import data from HSQL databases that are hosted in various networks/private clouds?
- Will foreign keys defined between my tables in HSQL database be linked in Zoho Analytics as well?
- Can I change the data type of the columns imported in Zoho Analytics?
- Can I import tables from the same database into multiple workspaces in Zoho Analytics?
- How do I remove the import setup?
Live Connect
- How do I configure Live Connect for the HSQL database?
- Can I change the data type of the columns in Live Connect?
- How is Live connect different from Data import method?
- How do I edit the live connection setup?
- What is a mismatch and how do I resolve it?
- Can I store a cache of my data points in Zoho Analytics to get quick access to my views?
- Can I connect Views created in the HSQL database (apart from Tables) to Zoho Analytics?
- I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
- Can I blend data from different sources in to the workspace in which live connection is configured?
- How do I remove the Setup?
Data Import
1. How do I install Zoho Databridge?
2. How do I import data from the HSQL database using Zoho Databridge?
To import data from local HSQL database, it is mandatory to install Zoho Databridge. Refer to the previous question to know how to Install.
3. How long does it take for the data to be imported into Zoho Analytics?
Import will take from a few minutes to hours depending on the volume of the data. Please note that, if you access the Workspace before the initial fetch, it will not display any data.
4. How can I edit the Import setup?
You can edit the import setup anytime needed by following the steps below.
- Open the workspace.
- Click the Data Sources tab from the left bar.
- All data sources for this workspace will be listed. Click the HSQL data source that you want to edit.
- The Data Sources page will open. Click the Edit Connection link.
- Modify the settings as needed and click Save. The connection details will be saved.
5. How can I schedule Import from HSQL database?
Zoho Analytics allows you to schedule the import anytime. You can schedule the import for an existing table by following the steps below.
- Open the workspace.
- Click the Data Sources tab from the left bar.
- All data sources for this workspace will be listed. Click the HSQL data source for which you want to schedule the import.
- The Data Sources page will open. Click the Sync Settings link.
- The Local Database - Synchronization Settings dialog will open.
- Select the schedule interval you need in the Repeat drop-down. Supported intervals are:
- Not Scheduled
- Every 'N' Hours
- Every Day
- Weekly Once
- Monthly Once
- Select when the data needs to be imported in Perform every option.
- In the Notify me after every Sync Failure(s) option, set the number of consecutive import failure after which you need to be notified.
- Click Save. The data for your HSQL database will be imported into Zoho Analytics in the set interval.
You can also schedule the import while initial import using the Schedule Setting option in the Step 4 of Import Wizard.
6. Will I be notified on import failures?
Yes, you can be notified after consecutive import failures, in case it occurs. To get notified of import failures, you need to set the number of consecutive import failures after which you need to be notified in the Notify me after every Sync Failure(s) option of the schedule import.
7. Import from HSQL database that is hosted in the cloud fails. How to solve this?
Import from the database may fail when the Databridge does not have the privilege to access the data. In case your database security system only allows access from restricted IP Addresses, then it will blacklist the server/machine where Databridge is installed. Ensure that you have whitelisted the IP Address of the machine/ server where the Databridge is installed.
8. Can I import data from HSQL database into an existing Zoho Analytics Workspace?
Yes, you can import your data from HSQL into an existing Workspace.
Follow the below steps to import data into an existing workspace:
- Open the Workspace into which you wish to import the data.
- Click Create > New Table / Import Data.
- The Import Your Data section will open. Click the Local Databases tab.
- The Import Wizard will open. Configuring the import will be similar to the steps followed in this presentation.
9. Can I import data from HSQL database into an existing table in Zoho Analytics?
Yes, you can import data into an existing table if you are importing from the same source database as the imported table. To do this:
- From the required table, click Import Data > Import into this Table.
- The Select Data to Import tab of Import wizard will open.
- You can choose to import from a different table using the Select Table option or import using the Custom Query.
10. I have synced data from database into a table. Can I change the data source of this table?
Yes, you can change the data source of a table, into which the HSQL database has been synced. To do this:
- Open the workspace.
- Click the Data Sources tab from the left bar.
- All data sources for this workspace will be listed. Click the data source you want to edit.
- The Data Sources page will open. Click the Edit Connection link.
- In the Local Database - Edit Connection dialog that open, modify the data source. You can also change the Databridge that fetches the data.
- Click Save to implement the changes made.
11. Can I import data from the HSQL which are hosted in various networks/private cloud?
Yes, you can import from various databases that are hosted in different networks by installing multiple Databridges. You need to install various Databridges for each network. To link all the Databridge installations to your account, use the same installation key available in the Download dialog.
Note:
- Single Databridge installation can import data from various data sources available in the same network.
- You can install only one Databridge per machine.
12. Will foreign keys defined between my tables in HSQL database be linked in Zoho Analytics as well?
Yes. In case you have linked two or more tables in your database using foreign keys, they will be linked automatically using a Look-up column in Zoho Analytics as well. You can also create lookup columns manually using the Lookup feature available in Zoho Analytics. Learn more.
13. Can I change the data type of the columns imported in Zoho Analytics?
Yes, you can change the data type of the columns imported into Zoho Analytics. However, it is necessary that the data type of your column is compatible with the data type of the column in your HSQL database for successful data synchronizations. It is always recommended that you change the data type in both your HSQL database as well as your Zoho Analytics Workspace.
14. Can I import tables from the same database into multiple workspaces in Zoho Analytics?
Yes, you can import tables from the same database source to multiple workspaces in Zoho Analytics. Read more about import.
15. How do I remove the import setup?
You can remove the import setup by following the steps below.
- Open the workspace.
- Click the Data Sources tab from the left bar.
- All data sources for this workspace will be listed. Click the data source you want to remove.
- In the Data Sources tab that opens, click the Settings icon.
Please note that this only removes the connection. You can still continue accessing the workspace in Zoho Analytics.
Live Connect
1. How do I configure Live Connect for the HSQL database?
2. Can I change the data type of the columns in Live Connect?
No, Zoho Analytics does not allow you to change the data type of the column. However, if the data type is changed in the source database, then Zoho Analytics will list the data type change in the mismatch section. Refer to this section to sync the data type changes.
3. How is Live connect different from Data import method?
| Data Import | Live Connect |
| In this method, data will be imported and stored in Zoho Analytics. | In this method,data will be fetched live using appropriate reporting queries whenever you create or access a report in Zoho Analytics. |
| Filtered data set can be imported from using customized queries. | Custom Query feature is not available in live connect. However, you can create Views in the source database and connect the same to Zoho Analytics. |
| Data from different sources can be imported into the same workspace and can be combined for analysis. | Cannot import data from any other data source into the same workspace in which Live Connect is setup. |
| Changes made to the columns, such as addition/deletion, will be synchronized automatically. | Any changes, such as column addition/deletion/renaming, will not be reflected. You will have to manually map the data using the Sync Design option. |
| When importing multiple tables, the foreign keys defined between the tables in the database database will not be linked in Zoho Analytics. However, you can manually link the tables in Zoho Analytics using the Lookup column feature. | Lookup relationship will be automatically created for tables that are linked via foreign keys in the database database. You can also manually link the tables in Zoho Analytics using Lookup column feature. |
| Users can create query tables. | Users cannot create query tables. |
| Report loading time will be fast as the data is stored in Zoho Analytics. | Report loading time directly depends on the server response time and the amount of data in database. |
4. How do I edit the live connection setup?
Zoho Analytics allows you to incorporate any changes made in the source database. To modify the settings, Access the Data Sources tab from the side navigation pane.
The Local Database Connection settings page will display the connection details,
- Edit Connection: This option helps you modify the connection settings.
- Sync Design: Zoho Analytics allows you to sync any changes made in the source database. This can be done at two levels,
- Click Sync Design to include the recent changes made to the data.
- Click the Sync option adjacent to the table name to include the changes made to the table.
- Add Table: Click Add more tables to include the new tables added to the source database.
- Delete Table: Click Delete to remove the live connect for a table.
5. What is a mismatch and how do I resolve it?
A mismatch occurs when,
- Tables, columns in Amazon Lightsail (the source database) are deleted or renamed.
- The data type of the columns is changed in Amazon Lightsail, but the changes are not synced in Zoho Analytics.
While using the Live Connect option, it is necessary that the table names, column names, and data type of the columns are the same in both the source database and Zoho Analytics. If they are not the same, they will be listed as a mismatch in the Mismatch tab.
Resolving Mismatch
6. Can I store a cache of my data points in Zoho Analytics to get quick access to my views?
Zoho Analytics allows you to create a cache for the reports in your live connect database to reduce the query fetching time.
To enable cache for your Live Connect workspace, please follow the below steps:
- From the Workspace Explorer, click the Settings tab from the side menubar.
- In the General - Workspace Settings page that opens, choose Yes for Enable Cache for this Workspace.
- In the Cache Refresh Interval in Minutes field, specify the duration to refresh the report.
- Click Save & Close.
7. Can I connect Views created in the HSQL database (apart from Tables) to Zoho Analytics?
Yes, you can connect with both Views and Tables created in the HSQL database to Zoho Analytics.
8. I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
This alert message will be displayed when Zoho Analytics is not able to access the information from the database. This could be because the tables/columns that you are accessing in Zoho Analytics are deleted or renamed in the HSQL database.
In this case, it is recommended that you remap the table/column. Refer to this presentation to know how to remap a table.
9. Can I blend data from different sources in to the workspace in which live connection is configured?
Currently, Zoho Analytics does not allow you to import data from other databases or applications or create query tables in the workspace in which Live Connect is configured.
If you wish to create query tables, you can create the required query as a view in the data source and connect it to Zoho Analytics.
10. How do I remove the Setup?
To delete the workspace,
- Log in to Zoho Analytics
- Click the More Actions icon that appears on mouse hover adjacent to the workspace name that you want to delete.
- Click the Delete Workspace option.