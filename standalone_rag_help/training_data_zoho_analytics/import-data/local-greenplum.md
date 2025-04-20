Importing from Greenplum using Zoho Databridge
If you have data in a local /hosted Greenplum database, then you can easily import your data into Zoho Analytics using the Zoho Databridge. The Zoho Databridge bridges your local Greenplum database and Zoho Analytics server to fetch data from your local /hosted Greenplum database. With this, you can also automate the import process to synchronize the data from your local /hosted Greenplum database into Zoho Analytics at a periodic interval.
Zoho Databridge
- What is Zoho Databridge?
- How do I install Zoho Databridge?
- What are the prerequisites to successfully import data into Zoho Analytics?
Data Import
- How do I import data from the Greenplum database using Zoho Databridge?
- How long does it take for the data to be imported into Zoho Analytics?
- How can I edit the Import setup?
- How can I schedule import from Greenplum database?
- Will I be notified on import failures?
- Import from Greenplum database that is hosted in the cloud has failed. How to solve this?
- Can I import data from Greenplum database into an existing Zoho Analytics Workspace?
- I have synced data from Greenplum database into a table. Can I change the data source of this table?
- Can I import data from Greenplum which are hosted in various networks/private cloud?
- Will foreign keys defined between my tables in Greenplum database be linked in Zoho Analytics as well?
- Can I change the data-type of the columns imported in Zoho Analytics?
- How do I remove the import setup?
- I am unable to establish the connection between the local Greenplum database and Zoho Analytics server. How do I solve this?
Live Connect
- How long does it take for me to visualize my data in Zoho Analytics?
- How can I edit the Live Connect setup?
- How is Live Connect different from Data Import?
- Can I store a cache of my data points in Zoho Analytics to get quick access to my views?
- Can I connect to the Views created in the Greenplum database (apart from Tables) to Zoho Analytics?
- Will foreign keys defined between my tables in the Vertica database be linked in Zoho Analytics as well?
- I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
- What is a Mismatch?
- When do Mismatches occur and how to resolve them?
- Can I connect to the new columns added in my Greenplum database to Zoho Analytics?
- Can I change the data type of the columns in Zoho Analytics?
- Can I import data from other data sources into the same workspace that I have used to connect with the Greenplum database database?
- Can I create Query Tables over the Greenplum database data?
- What happens when I delete or rename the database in the Greenplum database?
- How do I remove the Setup?
- What are the limitations of using the Greenplum database Live Connect?
Zoho Databridge
1. What is Zoho Databridge?
Zoho Databridge is a lightweight independent utility that bridges your on-premise data source and Zoho Analytics server to enable easy data import. You can also automate the import process to synchronize the data from your local or hosted database into Zoho Analytics at a periodic interval.
2. How do I install Zoho Databridge?
3. What are the prerequisites to successfully import data into Zoho Analytics?
You need to place the JDBC jar file for Greenplum database inside the /lib/drivers folder and restart the Databridge. Only after doing this, you will be able to import data from the Greenplum database. To do this,
- Download the JDBC jar file.
- Open the already downloaded Zoho Databridge folder and navigate to lib > drivers folder.
- Copy the downloaded JDBC jar file and paste it in the drivers folder.
- Restart the Zoho Databridge.
Data Import
1. How do I import data from the Greenplum database using Zoho Databridge?
To import data from local Greenplum database, it is mandatory to install Zoho Databridge. Refer to the previous question to know how to Install.
2. How long does it take for the data to be imported into Zoho Analytics?
Import will take from a few minutes to hours depending on the volume of the data. Please note that, if you access the Workspace before the initial fetch, it will not display any data.
3. How can I edit the Import setup?
You can edit the import setup anytime needed by following the steps below.
- Open the Workspace.
- Click Data Source from the left bar.
- All data sources for this Workspace will be listed. Click the Greenplum data source you want to edit.
- The Data Source page will open.
- Click the Edit Connection link and modify the settings as needed.
4. How can I schedule Import from Greenplum database?
Zoho Analytics allows you to schedule the import anytime. You can schedule the import for an existing table by following the steps below.
- Open the Workspace.
- Click Data Source from the left bar.
- All data sources for this Workspace will be listed. Click the Greenplum data source for which you want to schedule the import.
- The Data Source page will open. Click Sync Settings.
The Local Database - Synchronization Settings will open.
- Select the schedule interval you need in the Repeat drop-down. Supported intervals are:
- Not Scheduled
- Every 'N' Hours
- Every Day
- Weekly Once
- Monthly Once
- Select when the data needs to be imported in Perform every option.
- In the Notify me after every 'N' Sync Failure(s) option, set the number of consecutive import failure after which you need to be notified.
- Click Save. The data for your Greenplum database will be imported into Zoho Analytics in the set interval.
You can also schedule the import while initial import using the Schedule Settings option in the Step 4 of Import Wizard.
5. Will I be notified on import failures?
Yes, you will be notified after consecutive import failure, in case it occurs. You can set the number of consecutive import failures after which you need to be notified in the Notify me after every 'N' Sync Failure(s) option of the schedule import.
6. Import from Greenplum database that is hosted in the cloud fails. How to solve this?
Import from the database may fail when the Databridge does not have the privilege to access the data. In case your database security system only allows access from restricted IP Addresses, then it will blacklist the server/machine where Databridge is installed. Ensure that you have whitelisted the IP Address of the machine/ server where the Databridge is installed.
7. Can I import data from Greenplum database into an existing Zoho Analytics Workspace?
Yes, you can import your data from Greenplum into an existing Workspace.
Follow the below steps to import data into an existing workspace:
- Open the Workspace into which you wish to import the data.
Click Create > New Table / Import Data.
- The Import Your Data section will open. Click Local Databases option.
- The Import Wizard will open. Configuring the import will be similar to the steps followed in this presentation.
8. I have synced data from database into a table. Can I change the data source of this table?
Yes, you can change the data source of a table, into which the Greenplum database has been synced.
Follow the below steps to import if the source is available in the same Greenplum database that is imported into the table.
- Open the Workspace.
- Click Import Data> Import into this Table.
- The Select Data to Import tab of Import wizard will open.
- You can choose to import from a different table using the Select Table option or import using the Custom Query.
If the source is available in a different local database, follow the below steps:
- Open the Workspace.
- Click Data Source from the left bar.
- All data sources for this Workspace will be listed. Click the data source you want to edit.
- The Data Source page will open. Click Edit Connection link.
- In the Local Database - Edit Connection dialog that open, modify the data source. You can also change the Databridge that fetches the data.
9. Can I import data from the Greenplum which are hosted in various networks/private cloud?
Yes, you can import from various databases that are hosted in different networks by installing multiple Databridges. You need to install various Databridges for each network. To link all the Databridge installations to your account, use the same installation key available in the Download dialog.
Note:
- Single Databridge installation can import data from various data sources available in the same network.
- You can install only one Databridge per machine.
10. Will foreign keys defined between my tables in Greenplum database be linked in Zoho Analytics as well?
No, the tables will not be directly linked in Zoho Analytics. You need to link the required tables in Zoho Analytics using the Look-up column feature. Click here to learn about look-up.
11. Can I change the datatype of the columns imported in Zoho Analytics?
Yes, you can change the datatype of the columns imported into Zoho Analytics. However, it is necessary that the datatype of your column is compatible with the datatype of the column in your Greenplum database for successful data synchronizations. It is always recommended that you change the data type in both your Greenplum database as well as your Zoho Analytics Workspace.
12. How do I remove the import setup?
You can remove the import setup by following the steps below.
- Open the Workspace.
- Click Data Sources from the left bar.
- All data sources for this Workspace will be listed. Click the data source you want to remove.
- In the Data Sources tab that opens, click the Settings icon.
Click the Remove Data Source.
Please do note that this only removes the connection. You can still continue accessing the Workspace in Zoho Analytics.
13. I am unable to establish the connection between the local Greenplum database and Zoho Analytics server. How do I solve this?
This may happen due to various factors such as connectivity issues or privileges to access the protected data source. Refer to our Zoho Databridge Troubleshooting tip section to solve the specific issue you are facing.
Live Connect
1.How do I connect live with the Greenplum Database?
2. How long does it take for me to visualize my data in Zoho Analytics?
As there is no data import process involved, the loading time depends upon the amount of data stored in your Greenplum database and also the response time of your Greenplum database.
3. How can I edit the live connect setup?
4. How is Live Connect different from Data Import?
Data Import | Live Connect |
Data in Greenplum database will be imported and stored in Zoho Analytics. | Data from Greenplum Database will be fetched live using appropriate reporting queries whenever you create or access a report in Zoho Analytics. |
Filtered data set can be imported from Greenplum Database using customized queries. | Custom Query feature is not available in Greenplum Database Live Connect. However, you can create Views in the source database and connect the same with Zoho Analytics. |
Multiple data sources (apart from Greenplum Database) can be imported into the same workspace and they can be combined for reporting & analysis purposes. | Cannot import data from any other data source in to the same workspace in which Live Connect from Greenplum Database is setup. |
Changes made to the columns such as addition/deletion will be synchronized automatically. | Any changes such as column addition/deletion/renaming will not be reflected. You will have to manually map the data using the Sync Design option. |
When importing multiple tables, the foreign keys defined between the tables in the Greenplum Database database will not be linked in Zoho Analytics. However, you can manually link the tables in Zoho Analytics using the Lookup column feature. | Lookup relationship will be automatically created for tables that are linked via foreign keys in the Greenplum Database database. You can also manually link the tables in Zoho Analytics using Lookup column feature. |
Users can create query tables. | Users cannot create query tables. |
Report loading time will be fast as the data is stored in Zoho Analytics. | Report loading time directly depends on the server response time and the amount of data in Greenplum Database. |
5. Will the reports/dashboards query hit my database server every time I open it or can it be cached in Zoho Analytics?
(or) Can I store a cache of my data points in Zoho Analytics to get quick access to my views?
Zoho Analytics allows you to create a cache for the reports in your live connect database to reduce the query fetching time.
To enable cache for your live connect workspace, please follow the below steps:
- From your Workspace Explorer, click the Settings tab from the side menubar.
- In the General - Workspace Settings page that opens, choose Yes for Enable Cache for this Workspace.
- In Cache Refresh Interval in Minutes, specify the duration to refresh the report .
- Click Save & Close.
A cache for the reports will be created.
Note:
- Enabling cache will help create a cache for your reports in the workspace. This data will get updated periodically based on the time provided in the Cache Refresh Interval in Minutes.
- You can create a cache only for the reports, and not for tables in the workspace.
- This option is available only for Live Connect.
6. Can I connect Views created in the Greenplum database (apart from Tables) to Zoho Analytics?
Yes, you can connect with both Views and Tables created in the Greenplum database to Zoho Analytics.
7. Will foreign keys defined between my tables in the Greenplum database be linked in Zoho Analytics as well?
Yes. In case you have linked two or more tables in your Greenplum database using foreign keys, they will be linked automatically using a Look-up column in Zoho Analytics as well.
Note: The lookups created/modified in the added (linked with Zoho Analytics) tables will not be reflected in Zoho Analytics (even with Sync Design option). You need to create the lookup in Zoho Analytics manually. However, the lookup information will be created in Zoho Analytics when new tables are linked.
8. I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
This alert message will be displayed when Zoho Analytics is not able to access the information from the Greenplum database. This could be because the tables/columns that you are trying to access in Zoho Analytics are deleted or renamed in the Greenplum database.
In this case, it is recommended that you remap the table/column. Refer to this presentation to know how to remap a table.
9. What is a Mismatch?
When you have created reports in Zoho Analytics over the tables or columns which no longer have a direct mapping in the Greenplum database, it will be listed as a mismatch.
So, ensure that the tables/columns in Zoho Analytics workspace and Greenplum database match. The tables/columns that do not match will be listed in the Mismatch tab of the Local Database ConnectionSettings page.
10. When do Mismatches occur and how to resolve them?
11. Can I connect new columns added in my Greenplum database to Zoho Analytics?
Yes, you can connect the new columns that are added in your Greenplum database to Zoho Analytics from the Local Database Connection Settings page.
Note: If there exists a mismatch between the already available data in your Zoho Analytics workspace and your Greenplum database, Zoho Analytics will NOT be able to fetch the new column information. In this case, you need to first resolve the mismatches to connect to the new columns.
12. Can I change the data type of the columns in Zoho Analytics?
No, you cannot change the data type of the columns in Zoho Analytics.
13. Can I import data from other data sources into the same workspace that I have used to connect with the Greenplum database database?
No, you cannot import data from other data sources into the same workspace that you have used to connect with the Greenplum database.
14. Can I create Query Tables over the Greenplum data?
No, you will not be able to create Query Tables if you have setup the workspace using the Live Connect option. This is because this option does not fetch and store the data locally in Zoho Analytics. If you wish to create Query Tables, you can create the required query as a view in the data source and connect the same with Zoho Analytics.
15. What happens when I delete or rename the database in the Greenplum database?
When you delete or rename a database in the Greenplum database, Zoho Analytics loses its connectivity with the Greenplum database. After that, a warning message, as shown below, would be displayed. This error message will also be displayed if there are any connectivity issues or if your Greenplum database credentials have expired.
16. How do I remove the Setup?
You have to delete the workspace in Zoho Analytics to remove the connection setup.
To delete the workspace,
- Log in to Zoho Analytics
- Click the More Actions icon that appears on mouse hover adjacent to the workspace name that you want to delete.
- Click the Delete Workspace option.
17. What are the limitations of using the Greenplum database Live Connect?
Given below are a few shortcomings that one might face while using the Greenplum database Live Connect option.
- Data from your Greenplum database will NOT be locally stored in Zoho Analytics. Zoho Analytics will generate appropriate queries to fetch the required data live from the Greenplum database and show you the report. Hence, the loading time will directly depend on the performance of the Greenplum database server.
- Any changes such as column addition/deletion/renaming will not be mapped automatically. The user must manually map the updates made.
- Users cannot combine data from other data sources into the same workspace in which they have connected the Greenplum database.
- Users cannot create query tables.
- Users cannot change the data type of the columns in Zoho Analytics.