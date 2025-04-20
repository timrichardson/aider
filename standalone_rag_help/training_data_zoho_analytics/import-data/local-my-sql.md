Importing from MySQL using Zoho Databridge
If you have data in a local/hosted MySQL database, then you can easily import your data into Zoho Analytics using the Zoho Databridge. Zoho Analytics also allows you to connect data live from the MySQL database.
The Zoho Databridge bridges your local MySQL database and Zoho Analytics server to fetch data from your local/hosted MySQL database. With this, you can also automate the import process to synchronize the data from your local/hosted MySQL database into Zoho Analytics at a periodic interval.
You can either import the data into Zoho Analytics or connect directly with the MySQL database server.
- Data Import: Data in the MySQL database will be imported and stored in Zoho Analytics. You can setup periodic schedules to fetch the latest data automatically from your MySQL database. Report loading time will be faster as the data is stored in Zoho Analytics.
- Live Connect: In this mode, data will not be fetched from MySQL database and stored in Zoho Analytics. Instead for the reports that you create, Zoho Analytics will generate appropriate queries that will connect the required data live from MySQL database to Zoho Analytics and show you the report. In this case the loading time will directly depend on the performance of the MySQL database. The Live Connect option is exclusively available for paid plans and trials.
Data Import
- How do I install Zoho Databridge?
- What are the various import options offered by Zoho Analytics for importing data from databases?
- How do I import data from the MySQL database using Zoho Databridge?
- Where to place the JDBC jar file of the MySQL database?
- How to import data into Zoho Analytics using SSL certificate?
- How to import data into Zoho Analytics using SSH Tunneling?
- How long does it take for the data to be imported into Zoho Analytics?
- How can I edit the Import setup?
- How can I schedule import from MySQL database?
- Will I be notified of import failures?
- Import from MySQL database that is hosted in the cloud has failed. How to solve this?
- Can I import data from MySQL database into an existing Zoho Analytics workspace?
- Can I import data from MySQL database into an existing table in Zoho Analytics?
- I have synced data from MySQL database into a table. Can I change the data source of this table?
- Can I import data from MySQL databases that are hosted in various networks/private clouds?
- Will foreign keys defined between my tables in MySQL database be linked in Zoho Analytics as well?
- Can I import tables from the same database into multiple Workspaces in Zoho Analytics?
- Can I change the data type of the columns imported in Zoho Analytics?
- How do I remove the import setup?
- I am unable to establish the connection between the local MySQL database and Zoho Analytics server. How do I solve this?
Live Connect [Beta]
- How do I install Zoho Databridge?
- How do I connect live with the MySQL database?
- How can I edit the live connect setup?
- How is Live Connect different from Data Import?
- Where to place the JDBC jar file of the MySQL database?
- How long does it take for me to visualize my data in Zoho Analytics?
- Will the reports/dashboards query hit my database server every time I open it or can it be cached in Zoho Analytics?
(or) Can I store a cache of my data points in Zoho Analytics to get quick access to my views? - Can I connect Views created in MySQL database (apart from Tables) to Zoho Analytics?
- Will foreign keys defined between my tables in MySQL database be linked in Zoho Analytics as well?
- I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
- What is a Mismatch?
- When do Mismatches occur and how to resolve them?
- Can I connect the new columns added in my MySQL database to Zoho Analytics?
- Can I change the data type of the columns in Zoho Analytics?
- Can I import data from other data sources into the same workspace that I have used to connect with MySQL database?
- Can I create Query Tables over the MySQL database?
- What happens when I delete or rename the database in MySQL database?
- How do I remove the Setup?
- What are the limitations of MySQL database Live Connect?
1. How do I install Zoho Databridge?
The below presentation explains how to install Zoho Databridge in Zoho Analytics.
2.What are the various import options offered by Zoho Analytics for importing data from databases?
Zoho Analytics offers the following options to import data from databases.
- Import a single table
- Import multiple tables
- Custom query
- Stored procedure
3. How do I import data from the MySQL database using Zoho Databridge?
The below presentation explains how to import data from a MySQL database using Zoho Databridge.
4. Where to place the JDBC jar file of the MySQL database?
You need to place the JDBC jar file for MySQL database inside the /lib/drivers folder and restart the Databridge. Only after doing this, you will be able to import data from the MySQL database. To do this,
- Download the JDBC jar file.
- Open the already downloaded Zoho Databridge folder and navigate to lib > drivers folder.
- Copy the downloaded JDBC jar file and paste it in the drivers folder.
- Restart the Zoho Databridge.
5. How to import data into Zoho Analytics using SSL certificate?
Zoho Analytics allows you to secure your data import using SSL certificate for local databases. SSL (Secure Sockets Layer) is a digital certificate that secures the transport of information between the web server and the clients. It helps in establishing an encrypted connection between the web server and the clients.
You can choose anyone of the following ways to import data using SSL,
- Without Certificate
- With Certificate
Without Certificate
- Select the checkbox Use SSL.
- Click Without Certificate.
With Certificate
To import data using SSL certificate,
- Place the SSL certificate in /zcert folder.
- Restart Zoho Databridge.
- Select the checkbox, Use SSL.
- Click With Certificate.
Zoho Analytics will validate the certificate and proceed with importing.
If you chose With Certificate and failed to upload the certificate or upload an expired certificate, in both cases, an error message will be displayed, and the import process will be suspended.
Supported File formats
Zoho Analytics supports the following SSL file formats,
- .pem
- .crt
- .der
- .cer
6.How to import data into Zoho Analytics using SSH Tunneling?
Zoho Analytics allows you to connect to the database using the SSH port forwarding method.
Follow the below steps to import data using SSH Tunneling:
- Select the checkbox, Use SSH Tunneling.
- Enter the SSH Host Name, SSH Port number, SSH Username and SSL Password.
After specifying the all the necessary details, Click Ok to proceed with import.
7. How long does it take for the data to be imported into Zoho Analytics?
Import will take from a few minutes to hours depending on the volume of the data. Please note that, if you access the Workspace before the initial fetch, it will not display any data.
8. How can I edit the Import setup?
You can edit the import setup anytime by following the steps below:
- Open the Workspace.
- Click the Data Sources tab from the left bar.
- All the data sources for this Workspace will be listed. Click the MySQL data source that you want to edit.
- The Data Sources page will open. Click the Edit Connection link.
- Modify the settings as needed and click Save. The connection details will be saved.
9. How can I schedule import from MySQL database?
Zoho Analytics allows you to schedule the import anytime. You can schedule the import for an existing table by following the steps below.
- Open the Workspace.
- Click the Data Sources tab from the left bar.
- All the data sources for this Workspace will be listed. Click the MySQL data source for which you want to schedule the import.
- The Data Sources page will open. Click the Sync Settings link.
- The Local Database - Synchronization Settings dialog will open.
- Select the required schedule interval in the Repeat drop-down menu. Supported intervals are:
- Not Scheduled
- Every 'N' Hours
- Every Day
- Weekly Once
- Monthly Once
- Select when the data needs to be imported in Perform every option.
- In the Notify me after every Sync Failure(s) drop-down menu, set the number of consecutive import failures after which you need to be notified.
- Click Save. Data from the MySQL database will be imported into Zoho Analytics in the set interval.
You can also schedule the import while initial import using the Schedule Setting option in the Step 4 of Import Wizard.
10. Will I be notified of import failures?
Yes, you can be notified after consecutive import failures, in case it occurs. To get notified of import failures, you need to set the number of consecutive import failures after which you need to be notified in the Notify me after every Sync Failure(s) option of the schedule import.
11. Import from MySQL database that is hosted in the cloud fails. How to solve this?
Import from the cloud database may fail when the Databridge does not have the privilege to access the data. In case your cloud database security system only allows access from restricted IP Addresses, then it will blocklist the server/machine where Databridge is installed. Ensure that you have whitelisted the IP Address of the machine/ server where the Databridge is installed.
12. Can I import data from a MySQL database into an existing Zoho Analytics workspace?
Yes, you can import data from a MySQL database into an existing Zoho Analytics workspace.
Follow the below steps to import data into an existing workspace:
- Open the workspace into which you wish to import the data.
- Click Create > New Table / Import Data.
- The Import Your Data section will open. Click the Local Databases tab.
- The Import Wizard will open. Configuring the import will be similar to the steps followed in this presentation.
13. Can I import data from MySQL database into an existing table in Zoho Analytics?
Yes, you can import data into an existing table if you are importing from the same source database as the imported table.
- From the required table, click Import Data > Import into this Table.
- The Select Data to Import tab of the Import wizard will open.
- You can choose to import from a different table using the Select Table option or import using the Custom Query. You can also choose to import using the Stored Procedure option if you have an SQL query stored in your database.
14. I have synced data from MySQL database into a table. Can I change the data source of this table?
Yes, you can change the data source of a table, into which the MySQL database has been synced. To do this,
- Open the workspace.
- Click the Data Sources tab from the left bar.
- All the data sources for this workspace will be listed. Click the data source you want to edit.
- The Data Sources page will open. Click the Edit Connection link.
- In the Local Database - Edit Connection dialog that opens, modify the data source. You can also change the databridge that fetches the data.
- Click Save to implement the changes made.
15. Can I import data from MySQL databases that are hosted in various networks/private clouds?
Yes, you can import from various databases that are hosted in different networks by installing multiple databridges. You need to install separate databridges for each network. To link all the databridge installations to your account, use the same installation key available in the Download dialog.
Note:
- Single databridge installation can import data from various data sources available in the same network.
- You can install only one databridge per machine.
16. Will foreign keys defined between my tables in the MySQL database be linked in Zoho Analytics as well?
No, the tables will not be directly linked in Zoho Analytics. You need to link the required tables in Zoho Analytics using the Look-up feature. Click here to learn about look-up.
17. Can I import tables from the same database into multiple workspaces in Zoho Analytics?
Yes, you can import tables from the same database source to multiple workspaces in Zoho Analytics. Read more about import.
18. Can I change the data type of the columns imported in Zoho Analytics?
Yes, you can change the data type of the columns imported into Zoho Analytics. However, it is necessary that the data type of your column is compatible with the data type of the column in your MySQL database for successful data synchronizations. It is always recommended that you change the data type in both your MySQL database as well as your Zoho Analytics Workspace.
19. How do I remove the import setup?
You can remove the import setup by following the steps below.
- Open the Workspace.
- Click the Data Sources tab from the left bar.
- All the data sources for this Workspace will be listed. Click the MySQL data source you want to remove.
- In the Data Sources tab that opens, click the Settings icon inline to the data source name on the right.
- Click the Remove Data Source option from the drop-down menu.
Please do note that this only removes the connection. You can still continue accessing the workspace in Zoho Analytics.
20. I am unable to establish the connection between the local MySQL database and Zoho Analytics server. How do I solve this?
This may happen due to various factors such as connectivity issues or privileges to access the protected data source. Refer to our Zoho Databridge Troubleshooting tip section to solve the specific issue you are facing.
Live Connect [Beta]
1. How do I install Zoho Databridge?
You can easily install Zoho Databridge from the Zoho Analytics interface. Refer here to learn how.
2. How do I connect live with the MySQL database?
3. How can I edit the live connect setup?
4. How is Live Connect different from Data Import?
Tabulated below are the differences between the Data Import feature and the Live Connect feature.
| Data Import | Live Connect |
| Data in the MySQL database will be imported and stored in Zoho Analytics. | Data from the MySQL database will be fetched live using appropriate reporting queries whenever you create or access a report in Zoho Analytics. |
| Filtered data set can be imported from a MySQL database using customized queries. | Custom Query feature is not available in MySQL database Live Connect. However, you can create Views in the source database and connect the same with Zoho Analytics. |
| Multiple data sources (apart from the MySQL database) can be imported into the same workspace and they can be combined for reporting & analysis purposes. | Cannot import data from any other data source into the same workspace in which Live Connect from MySQL database is setup. |
| Changes made to the columns such as addition/deletion will be synchronized automatically. | Any changes such as column addition/deletion/renaming will not be reflected. You will have to manually map the data using the Sync Design option. |
When importing multiple tables, the foreign keys defined between the tables in the MySQL database will not be linked in Zoho Analytics. However, you can manually link the tables in Zoho Analytics using the Look-up column feature. | Look-up relationship will be automatically created for tables that are linked via foreign keys in the MySQL database. You can also manually link the tables in Zoho Analytics using Look-up column feature. |
| Users can create query tables. | Users cannot create query tables. |
| Report loading time will be fast as the data is stored in Zoho Analytics. | Report loading time directly depends on the MySQL database response time and the amount of data in the MySQL database. |
5. Where to place the JDBC jar file of the MySQL database?
You need to place the JDBC jar file for MySQL database inside the /lib/drivers folder and restart the Databridge. Only after doing this, you will be able to connect data from the MySQL database. To do this,
- Download the JDBC jar file.
- Open the already downloaded Zoho Databridge folder and navigate to lib > drivers folder.
- Copy the downloaded JDBC jar file and paste it in the drivers folder.
- Restart the Zoho Databridge.
6. How long does it take for me to visualize my data in Zoho Analytics?
As there is no data import process involved, the loading time depends upon the amount of data stored in your MySQL database and also the response time of your MySQL database.
7. Will the reports/dashboards query hit my database server every time I open it or can it be cached in Zoho Analytics?
(or) Can I store a cache of my data points in Zoho Analytics to get quick access to my views?
Zoho Analytics allows you to create a cache for the reports in your live connect database to reduce the query fetching time.
To enable cache for your live connect workspace, please follow the below steps:
- From your Workspace Explorer, click the Settings tab from the side menubar.
- In the General - Workspace Settings page that opens, choose Yes to Enable Cache for this Workspace.
- Provide Cache Refresh Interval in Minutes.
- Click Save & Close.
A cache for the reports will be created for the workspace.
- Enabling cache will help create a cache for your reports in the workspace. This data will get updated periodically based on the time provided in the Cache Refresh Interval in Minutes.
- You can create a cache only for the reports, and not for tables in the workspace.
- This option is available only for Live Connect.
8. Can I connect Views created in the MySQL database (apart from Tables) to Zoho Analytics?
Yes, you can connect with both Views and Tables created in the MySQL database to Zoho Analytics.
9. Will foreign keys defined between my tables in the MySQL database be linked in Zoho Analytics as well?
Yes. In case you have linked two or more tables in your MySQL database using foreign keys, they will be linked automatically using a Look-up column in Zoho Analytics as well.
10. I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
This alert message will be displayed when Zoho Analytics is not able to access the information from the MySQL database. This could be because the tables/columns that you are trying to access in Zoho Analytics are deleted or renamed in the MySQL database.
In this case, it is recommended that you remap the table/column. Refer to this presentation to know how to remap a table.
11. What is a Mismatch?
When you have created reports in Zoho Analytics over the tables or columns which no longer have a direct mapping in the MySQL database, it will be listed as a mismatch.
So, ensure that the tables/columns in Zoho Analytics workspace and MySQL database match. The tables/columns that do not match will be listed in the Mismatch tab of the Local Database Connection Settings page. Refer to the next question to know more about mismatch.
12. When do Mismatches occur and how to resolve them?
13. Can I connect new columns added in my MySQL database to Zoho Analytics?
Yes, you can connect the new columns that are added in your MySQL database to Zoho Analytics from the Local Database Connection Settings page. Refer to this presentation to know more.
Note: If there exists a mismatch between the already available data in your Zoho Analytics workspace and your MySQL database, Zoho Analytics will NOT be able to fetch the new column information. In this case, you need to first resolve the mismatches to connect to the new columns.
14. Can I change the data type of the columns in Zoho Analytics?
No, you cannot change the data type of the columns in Zoho Analytics.
15. Can I import data from other data sources into the same workspace that I have used to connect with the MySQL database?
No, you cannot import data from other data sources into the same workspace that you have used to connect with the MySQL database.
16. Can I create Query Tables over the MySQL data?
No, you will not be able to create Query Tables if you have setup the workspace using the Live Connect option. This is because this option does not fetch and store the data locally in Zoho Analytics. If you wish to create Query Tables, you can create the required query as a view in the data source and connect the same with Zoho Analytics.
17. What happens when I delete or rename the database in the MySQL database?
When you delete or rename a database in the MySQL database, Zoho Analytics loses its connectivity with the MySQL database. Thereafter, a warning message, as shown below, would be displayed. This error message will also be displayed if there are any connectivity issues or if your MySQL database credentials have expired.
For more information regarding the same, refer to the Edit Connection presentation.
18. How do I remove the Setup?
You have to delete the workspace in Zoho Analytics to remove the connection setup.
To delete the workspace,
- Log in to Zoho Analytics
- Click the More Actions icon that appears on mouse hover adjacent to the workspace name that you want to delete
- Click the Delete Workspace option
19. What are the limitations of using the MySQL database Live Connect?
Given below are a few shortcomings that one might face while using the MySQL database Live Connect option.
- Data from your MySQL database will NOT be locally stored in Zoho Analytics. Zoho Analytics will generate appropriate queries to fetch the required data live from the MySQL database and show you the report. Hence, the loading time will directly depend on the performance of the MySQL database server.
- Any changes such as column addition/deletion/renaming will not be mapped automatically. The user must manually map the updates made.
- Users cannot combine data from other data sources into the same workspace in which they have connected the MySQL database.
- Users cannot create query tables.
- Users cannot change the data type of the columns in Zoho Analytics.