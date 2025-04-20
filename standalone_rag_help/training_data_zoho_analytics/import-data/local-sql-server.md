Importing from SQL Server using Zoho Databridge
If you have data in a local/hosted SQL Server database, then you can easily import your data into Zoho Analytics using the Zoho Databridge. Zoho Analytics also allows you to connect data live from the SQL Server database.
The Zoho Databridge bridges your local SQL Server database and Zoho Analytics server to fetch data from your local/hosted SQL Server database. With this, you can also automate the import process to synchronize the data from your local/hosted SQL Server database into Zoho Analytics at a periodic interval.
You can either import the data into Zoho Analytics or connect directly with the SQL database server.
- Data Import: Data in the SQL Server database will be imported and stored in Zoho Analytics. You can setup periodic schedules to fetch the latest data automatically from your SQL Server database. Report loading time will be faster as the data is stored in Zoho Analytics.
- Live Connect: In this mode, data will not be fetched from SQL Server database and stored in Zoho Analytics. Instead for the reports that you create, Zoho Analytics will generate appropriate queries that will connect the required data live from SQL Server database to Zoho Analytics and show you the report. In this case the loading time will directly depend on the performance of the SQL Server database. The Live Connect option is exclusively available for all paid plans and trials.
Data Import
- How do I install Zoho Databridge?
- How do I import data from the SQL Server database using Zoho Databridge?
- How long does it take for the data to be imported into Zoho Analytics?
- How can I edit the Import setup?
- How can I schedule import from SQL Server database?
- Will I be notified on import failures?
- Import from SQL Server database that is hosted in the cloud has failed. How to solve this?
- Can I import data from SQL Server database into an existing Zoho Analytics workspace?
- Can I import data from SQL Server database into an existing table in Zoho Analytics?
- I have synced data from SQL Server database into a table. Can I change the data source of this table?
- Can I import data from SQL Server which are hosted in various networks/private clouds?
- Will foreign keys defined between my tables in SQL Server database be linked in Zoho Analytics as well?
- Can I import tables from the same database into multiple Workspaces in Zoho Analytics?
- Can I change the data type of the columns imported in Zoho Analytics?
- How do I remove the import setup?
- I am unable to establish the connection between the local SQL Server database and Zoho Analytics server. How do I solve this?
Live Connect [Beta]
- How do I install Zoho Databridge?
- How do I connect live with the SQL Server database?
- How can I edit the live connect setup?
- How is Live Connect different from Data Import?
- How long does it take for me to visualize my data in Zoho Analytics?
- Will the reports/dashboards query hit my database server every time I open it or can it be cached in Zoho Analytics?
(or) Can I store a cache of my data points in Zoho Analytics to get quick access to my views? - Can I connect Views created in SQL Server database (apart from Tables) to Zoho Analytics?
- Will foreign keys defined between my tables in SQL Server database be linked in Zoho Analytics as well?
- I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
- What is a Mismatch?
- When do Mismatches occur and how to resolve them?
- Can I connect the new columns added in my SQL Server database to Zoho Analytics?
- Can I change the data type of the columns in Zoho Analytics?
- Can I import data from other data sources into the same workspace that I have used to connect with SQL Server database?
- Can I create Query Tables over the SQL Server database?
- What happens when I delete or rename the database in SQL Server database?
- How do I remove the Setup?
- What are the limitations of SQL Server database Live Connect?
Troubleshooting Tips
- I am unable to establish the connection between the local SQL Server database and Zoho Analytics server. How do I solve this?
- I get an error message "Sorry, a problem in connecting to your Database server. Reason The TCP/IP connection to the host < >." What should I do?
- I get an alert message "Login failed for user < >." What should I do?
1. How do I install Zoho Databridge?
2. How do I import data from the SQL Server database using Zoho Databridge?
To import data from local SQL Server database, it is mandatory to install Zoho Databridge. Refer to the previous question to know how to Install.
3. How long does it take for the data to be imported into Zoho Analytics?
Import will take from a few minutes to hours depending on the volume of the data. Please note that, if you access the Workspace before the initial fetch, it will not display any data.
4. How can I edit the Import setup?
You can edit the import setup anytime needed by following the steps below:
- Open the Workspace.
- Click the Data Sources tab from the left bar.
- All the data sources for this Workspace will be listed. Click the SQL Server data source you want to edit.
- The Data Sources page will open. Click the Edit Connection link.
- Modify the settings as needed and click Save. The connection details will be saved.
5. How can I schedule Import from SQL Server database?
Zoho Analytics allows you to schedule the import anytime. You can schedule the import for an existing table by following the steps below:
- Open the workspace.
- Click the Data Sources tab from the left bar.
- All the data sources for this Workspace will be listed. Click the SQL Server data source which you want to schedule the import.
- The Data Sources page will open. Click the Sync Settings link.
- The Local Database - Synchronization Settings dialog will open.
- Select the schedule interval you need in the Repeat drop-down. Supported intervals are:
- Not Scheduled
- Every 'N' Hours
- Every Day
- Weekly Once
- Monthly Once
- Select when the data need to be imported in Perform option.
- In the Notify me after every Sync Failure(s) drop-down menu, set the number of consecutive import failures after which you need to be notified.
- Click Save. The data for your SQL Server database will be imported into Zoho Analytics in the set interval.
You can also schedule the import while initial import using the Schedule Setting option in the Step 4 of Import Wizard.
6. Will I be notified on import failures?
Yes, you will be notified after consecutive import failure, in case it occurs. You can set the number of consecutive import failures after which you need to be notified in the Notify me after every Sync Failure(s) option of the schedule import.
7. Import from SQL Server database that is hosted in the cloud fails. How to solve this?
Import from the cloud database may fail when the Databridge does not have the privilege to access the data. In case your cloud database security system only allows access from restricted IP Addresses, then it will blacklist the server/machine where Databridge is installed. Ensure that you have whitelisted the IP Address of the machine/ server where the Databridge is installed.
8. Can I import data from SQL Server database into an existing Zoho Analytics workspace?
Yes, you can import your data from SQL Server into an existing workspace.
Follow the below steps to import data into an existing workspace:
- Open the Workspace into which you wish to import the data.
- Click Create > New Table / Import Data.
- The Import Your Data section will open. Click the Local Databases tab.
- The Import Wizard will open. Configuring the import will be similar to the steps followed in this presentation.
9. Can I import data from SQL Server database into an existing table in Zoho Analytics?
Yes, you can import data into an existing table if you are importing from the same source database as the imported table. To do this,
- From the required table, click Import Data > Import into this Table.
- The Select Data to Import tab of Import wizard will open.
- You can choose to import from a different table using the Select Table option or import using the Custom Query. You can also choose to import using the Stored Procedure option if you have an SQL query stored in your database.
10. I have synced data from database into a table. Can I change the data source of this table?
Yes, you can change the data source of a table, into which the SQL Server database has been synced. To do this,
- Open the Workspace.
- Click the Data Sources tab from the left bar.
- All the data sources for this Workspace will be listed. Click the data source you want to edit.
- The Data Sources page will open. Click the Edit Connection link.
- In the Local Database - Edit Connection dialog that open, modify the data source. You can also change the databridge that fetches the data.
- Click Save to implement the changes made.
11. Can I import data from the SQL Server which are hosted in various networks/private clouds?
Yes, you can import from various databases that are hosted in different networks by installing multiple databridges. You need to install separate databridges for each network. To link all the databridge installations to your account, use the same installation key available in the Download dialog.
- Single Databridge installation can import data from various data sources available in the same network.
- You can install only one Databridge per machine.
12. Will foreign keys defined between my tables in SQL Server database be linked in Zoho Analytics as well?
No, the tables will not be directly linked in Zoho Analytics. You need to link the required tables in Zoho Analytics using the Look-up feature. Click here to learn about look-up.
13. Can I import tables from the same database into multiple workspaces in Zoho Analytics?
Yes, you can import tables from the same database source to multiple workspaces in Zoho Analytics. Read more about import.
14. Can I change the data type of the columns imported in Zoho Analytics?
Yes, you can change the data type of the columns imported into Zoho Analytics. However, it is necessary that the data type of your column is compatible with the datatype of the column in your SQL Server database for successful data synchronizations. It is always recommended that you change the data type in both your SQL Server database as well as your Zoho Analytics Workspace.
15. How do I remove the import setup?
You can remove the import setup by following the steps below.
- Open the Workspace.
- Click the Data Sources tab from the left bar.
- All the data sources for this Workspace will be listed. Click the data source you want to remove.
- In the Data Sources tab that opens, click the Settings icon.
- Click the Remove Data Source option from the drop-down menu.
Please note that this only removes the connection. You can still continue accessing the Workspace in Zoho Analytics.
16. I am unable to establish the connection between the local SQL Server database and Zoho Analytics server. How do I solve this?
This may happen due to various factors such as connectivity issues or privileges to access the protected data source. Refer to our Zoho Databridge Troubleshooting tip section to solve the specific issue you are facing.
Live Connect [Beta]
1. How do I install Zoho Databridge?
You can easily install Zoho Databridge from the Zoho Analytics interface. Refer here to learn how.
2. How do I connect live with the SQL Server database?
3. How can I edit the live connect setup?
4. How is Live Connect different from Data Import?
Tabulated below are the differences between the Data Import feature and Live Connect feature.
| Data Import | Live Connect |
| Data in SQL Server database will be imported and stored in Zoho Analytics. | Data from the SQL Server database will be fetched live using appropriate reporting queries whenever you create or access a report in Zoho Analytics. |
| Filtered data set can be imported from SQL Server database using customized queries. | Custom Query feature is not available in SQL Server database Live Connect. However, you can create Views in the source database and import the same into Zoho Analytics. |
| Multiple data sources (apart from SQL Server database) can be imported into the same workspace and they can be combined for reporting & analysis purposes. | Cannot import data from any other data source into the same workspace in which Live Connect from SQL Server database is setup. |
| Changes made to the columns such as addition/deletion will be synchronized automatically. | Any changes such as column addition/deletion/renaming will not be reflected. You will have to manually map the data using the Sync Design option. |
When importing multiple tables, the foreign keys defined between the tables in the SQL Server database will not be linked in Zoho Analytics. However, you can manually link the tables in Zoho Analytics using the Look-up column feature. | Look-up relationship will be automatically created for tables that are linked via foreign keys in the SQL Server database. You can also manually link the tables in Zoho Analytics using Look-up column feature. |
| Users can create query tables. | Users cannot create query tables. |
| Report loading time will be fast as the data is stored in Zoho Analytics. | Report loading time directly depends on the SQL Server database response time and the amount of data in SQL Server database. |
5. How long does it take for me to visualize my data in Zoho Analytics?
As there is no data import process involved, the loading time depends upon the amount of data stored in your SQL Server database and also the response time of your SQL Server database.
6. Will the reports/dashboards query hit my database server every time I open it or can it be cached in Zoho Analytics?
(or) Can I store a cache of my data points in Zoho Analytics to get quick access to my views?
Zoho Analytics allows you to create a cache for the reports in your live connect database to reduce the query fetching time.
To enable cache for your live connect workspace, please follow the below steps:
- From your Workspace Explorer, click Settings from the side menubar.
- In the General - Workspace Settings page that opens, choose Yes for Enable Cache for this Workspace.
- Provide Cache Refresh Interval in Minutes.
- Click Save & Close.
A cache for the reports will be created for the Workspace.
- Enabling cache will help create a cache for your reports in the workspace. This data will get updated periodically based on the time provided in the Cache Refresh Interval in Minutes.
- You can create a cache only for the reports, and not for tables in the workspace.
- This option is available only for Live Connect.
7. Can I connect Views created in the SQL Server database (apart from Tables) to Zoho Analytics?
Yes, you can connect with both Views and Tables created in the SQL Server database to Zoho Analytics.
8. Will foreign keys defined between my tables in the SQL Server database be linked in Zoho Analytics as well?
Yes. In case you have linked two or more tables in your SQL Server database using foreign keys, they will be linked automatically using a Look-up column in Zoho Analytics as well.
9. I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
This alert message will be displayed when Zoho Analytics is not able to access the information from the SQL Server database. This could be because the tables/columns that you are trying to access in Zoho Analytics is deleted or renamed in SQL Server database.
In this case, it is recommended that you remap the table/column. Refer to this presentation to know how to remap a table.
10. What is a Mismatch?
When you have created reports in Zoho Analytics over the tables or columns which no longer have a direct mapping in the SQL Server database, it will be listed as a mismatch.
So, ensure that the tables/columns in Zoho Analytics workspace and SQL Server database match. The tables/columns that do not match will be listed in the Mismatch tab of the Local Database Connection Settings page. Refer the next question to know more about mismatch.
11. When do Mismatches occur and how to resolve them?
12. Can I connect new columns added in my SQL Server database to Zoho Analytics?
Yes, you can connect the new columns that are added in your SQL Server database to Zoho Analytics from the Local Database Connection Settings page. Refer to this presentation to know more.
Note:
If there exists a mismatch between the already available data in your Zoho Analytics workspace and your SQL Server database, Zoho Analytics will NOT be able to fetch the new column information. In this case, you need to first resolve the mismatches to connect to the new columns.13. Can I change the data type of the columns in Zoho Analytics?
No, you cannot change the data type of the columns in Zoho Analytics.
14. Can I import data from other data sources into the same workspace that I have used to connect with the SQL Server database?
No, you cannot import data from other data sources into the same workspace that you have used to connect with the SQL Server database.
15. Can I create Query Tables over the SQL Server data?
No, you will not be able to create Query Tables if you have setup the workspace using the SQL Server Live Connect option. This is because this option does not fetch and store the data locally in Zoho Analytics. If you wish to create Query Tables, you can create the required query as a view in the data source and connect the same with Zoho Analytics.
16. What happens when I delete or rename the database in the SQL Server database?
When you delete or rename a database in the SQL Server database, Zoho Analytics loses its connectivity with SQL Server database. Thereafter, a warning message, as shown below, would be displayed. This error message will also be displayed if there are any connectivity issues or if your SQL Server database credentials have expired.
For more information regarding the same, refer to the Edit Connection presentation.
17. How do I remove the Setup?
You have to delete the workspace in Zoho Analytics to remove the connection setup.
To delete the workspace,
- Log in to Zoho Analytics
- Click the More Actions icon that appears on mouse hover adjacent to the workspace name that you want to delete
- Click the Delete Workspace option
18. What are the limitations of using the SQL Server database Live Connect?
Given below are a few shortcomings that one might face while using the SQL Server database Live Connect option.
- Data from your SQL Server database will NOT be locally stored in Zoho Analytics. Zoho Analytics will generate appropriate queries to fetch the required data live from SQL Server database and show you the report. Hence, the loading time will directly depend on the performance of the SQL Server database server.
- Any changes such as column addition/deletion/renaming will not be mapped automatically. The user must manually map the updates made.
- Users cannot combine data from other data sources into the same workspace in which you have connected the SQL Server database.
- Users cannot create query tables.
- Users cannot change the data type of the columns in Zoho Analytics.
Troubleshooting Tips
1. I am unable to establish the connection between the local SQL Server database and Zoho Analytics server. How do I solve this?
This may happen due to various factors such as connectivity issues or privileges to access the protected data source. Refer to our Zoho Databridge Troubleshooting tip section to solve the specific issue you are facing.
2. I get an error message "Sorry, a problem in connecting to your Database server. Reason The TCP/IP connection to the host < >." What should I do?
The error message will be displayed when the TCP/IP configuration is not enabled for your SQL Server.
To enable the same, please perform the below steps:
- Open your Microsoft SQL Server folder from your Windows machine.
- Navigate through Configuration Tools > SQL Server Configuration Manager > SQL Server Network Configuration > Protocols for [your SQL server instance name].
- In the Protocol Name section, right-click on TCP/IP.
- Click Properties.
- In the Protocol section of TCP/IP Properties pop-up page, change the status of Enabled to Yes.
3. I get an alert message "Login failed for user < >." What should I do?
This message will be displayed when there is a problem with your authentication details. Ensure that you have provided a valid user name and password.
Also, please note that currently, we support only SQL Server authentication. We do not provide direct support for Windows authentication. However, if required, you can choose to Connect using the JDBC URL option.