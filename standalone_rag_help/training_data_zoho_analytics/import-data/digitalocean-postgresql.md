Import Data from DigitalOcean PostgreSQL
The data stored in DigitalOcean PostgreSQL Cloud Database can be analyzed using Zoho Analytics in two ways. You can either import your data into Zoho Analytics, or connect directly with the DigitalOcean PostgreSQL server.
- Data Import: The data in DigitalOcean PostgreSQL will be imported and stored in Zoho Analytics. You can set up periodic schedules to fetch the latest data automatically from your DigitalOcean PostgreSQL database. The reports loading time will load faster as the data is stored in Zoho Analytics.
- Live Connect: In this mode, data will not be fetched from DigitalOcean PostgreSQL and stored in Zoho Analytics. Instead for the reports that you create, Zoho Analytics will generate appropriate queries that will connect the required data live from DigitalOcean PostgreSQL to Zoho Analytics and show you the report. In this case, the loading time will directly depend on the performance of DigitalOcean PostgreSQL.
Read about the main differences between Data Import and Live Connect.
Please note that the Live Connect option is exclusively available for paid plans and trials only. Refer to the Live Connect section to learn.
Data Import
- How do I import data from the DigitalOcean PostgreSQL database?
- How can I edit the setup?
- How long does it take for the data to be imported into Zoho Analytics?
- Can I import data from Views created in DigitalOcean PostgreSQL (apart from Tables) into Zoho Analytics?
- Will foreign keys defined between my tables in the DigitalOcean PostgreSQL database be linked in Zoho Analytics as well?
- Can I change the data type of the columns imported in Zoho Analytics?
- I have connected to a database and imported a few tables into Zoho Analytics. Can I add more tables from the same source to the existing connection?
- Can I import data from DigitalOcean PostgreSQL database into an existing table in Zoho Analytics?
- I have synced data from DigitalOcean PostgreSQL database into a table. Can I change the data source of this table?
- I have synced data from a database into multiple tables in this workspace? Can I remove the data source for a single table?
- Can I import data from my DigitalOcean PostgreSQL database into an existing Zoho Analytics workspace?
- Can I synchronize the data from my Cloud Database instantly?
- The Last Data Sync Status in Data sources page shows Sync Failed. How do I resolve it?
- How do I remove the Setup?
Live Connect
- How do I connect live with the DigitalOcean PostgreSQL database?
- How can I edit the live connect setup?
- How is Live Connect different from Data Import?
- How long does it take for me to visualize my data in Zoho Analytics?
- Will the reports/dashboards query hit my database server every time I open it or can it be cached in Zoho Analytics? (or) Can I store a cache of my data points in Zoho Analytics to get quick access to my views?
- Can I connect Views created in DigitalOcean PostgreSQL (apart from Tables) to Zoho Analytics?
- Will foreign keys defined between my tables in DigitalOcean PostgreSQL database be linked in Zoho Analytics as well?
- Can I link the related tables, connected from the Cloud Database using the Live Connect option, in Zoho Analytics?
- I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
- What is a Mismatch?
- When do Mismatches occur and how to resolve them?
- Can I synchronize the meta data of the table from my Cloud Database instantly?
- Can I connect new columns added in my DigitalOcean PostgreSQL database to Zoho Analytics?
- Can I change the data type of the columns in Zoho Analytics?
- Can I import data from other data sources into the same workspace that I have used to connect with DigitalOcean PostgreSQL?
- Can I create Query Tables over the DigitalOcean PostgreSQL data?
- What happens when I delete or rename the database in DigitalOcean PostgreSQL?
- How do I remove the Setup?
- What are the limitations of using the DigitalOcean PostgreSQL Live Connect?
Troubleshooting Tips
- I get an error message "Sorry, there is a problem in connecting to your cloud data source. Check your connection details and try again." What should I do?
- I am unable to find the Live Connect option while importing data into Zoho Analytics. What could be the possible reasons?
Data Import
1. How do I import data from the DigitalOcean PostgreSQL database?
2. How can I edit the setup?
3. How long does it take for the data to be imported into Zoho Analytics?
After setting up, you might have to wait for sometime for the initial fetch to finish. This depends on the amount of data to be imported into Zoho Analytics and also the response time of your DigitalOcean PostgreSQL server. You will receive an email notification once the import is complete. Please note that if you access the workspace before the initial fetch, it will not display any data.
4. Can I import data from Views created in DigitalOcean PostgreSQL (apart from Tables) into Zoho Analytics?
Yes, you can import data from Tables as well as Views available in your DigitalOcean PostgreSQL database into your Zoho Analytics workspace.
5. Will foreign keys defined between my tables in the DigitalOcean PostgreSQL database be linked in Zoho Analytics as well?
When importing multiple tables, the foreign keys defined between the tables in DigitalOcean PostgreSQL database will be linked in Zoho Analytics. The foreign keys will be created as Lookup columns in Zoho Analytics.
If you import data from one table at a time (choosing the single table option) then the foreign keys will not be defined. However, you can manually link the tables in Zoho Analytics using the Lookup column feature. Click here to learn about the Lookup column feature.
6. Can I change the data type of the columns imported in Zoho Analytics?
Yes, you can change the data type of the columns imported into Zoho Analytics. However, it is necessary that the data type of your column is compatible with the data type of the column in your DigitalOcean PostgreSQL database for successful data synchronizations. It is always recommended that you change the data type in both your DigitalOcean PostgreSQL database as well as your Zoho Analytics workspace.
7. I have connected to a database and imported a few tables into Zoho Analytics. Can I add more tables from the same source to the existing connection?
Yes, you can add tables from the same source to the existing connection. Follow the below steps:
- From your DigitalOcean PostgreSQL workspace, navigate to Create > New Table / Import Data.
- Click the Cloud Databases option. The Connect to Cloud Database wizard will open.
- From the Connection Name drop-down menu, select the existing DigitalOcean PostgreSQL database name.
- The rest of the steps are similar to importing data from cloud database.
8. Can I import data from DigitalOcean PostgreSQL database into an existing table in Zoho Analytics?
Yes, you can import data into an existing table if you are importing from the same source database as the imported table.
- From the required table, click Import Data > Import Data into this Table.
- The Select Data to Import tab of the Import wizard will open.
- You can choose to import from the same table or a different table using the Select Table option, or import using the Custom Query.
- The rest of the steps are similar to importing from a single table.
9. I have synced data from DigitalOcean PostgreSQL database into a table. Can I change the data source of this table?
Yes, you can change the data source of the [Zoho Analytics] table into which the DigitalOcean PostgreSQL database has been synced. To do this,
- Open the workspace.
- Click the Data Sources tab from the left bar.
- All the data sources for this workspace will be listed. Click the data source you want to edit.
- The Data Sources page will open. Click the Edit Connection link.
- In the Cloud Database - Edit Connection dialog that opens, modify the data source.
- Click Save to implement the changes made.
10. I have synced data from a database into multiple tables in this workspace? Can I remove the data source for a single table?
Yes, you can remove the data source for a single table from this data source. Follow the below steps to do this.
- Open the workspace.
- Click the Data Sources tab from the left bar.
- All the data sources for this workspace will be listed. Click the data source you want to edit.
- The Data Sources page will open, listing all the tables synced from the data source.
- Hover the mouse over the table which you want to remove. A contextual menu will open.
- Click the Trash icon. Data synchronization will be removed for this table alone. You can choose to synchronize data from other sources, or manually import data into this table as needed. For the rest of the tables, the same data source will continue to be in sync.
11. Can I import data from my DigitalOcean PostgreSQL database into an existing Zoho Analytics workspace?
- Yes. Follow the below steps to import data into an existing workspace:
- Open the workspace into which you wish to import the data.
- Navigate through Create > New Table / Import Data.
- Click the Cloud Databases option.
- Configuring the import will be similar to the steps followed in this presentation.
12. Can I synchronize the data from my Cloud Database instantly?
Yes, you can synchronize your data from Cloud Database instantly when needed.
To synchronize your data instantly:
- Open the required workspace.
- From the home page, click the Data Sources tab.
- In the Data Sources page that opens, click the Sync Now link.
13. The Last Data Sync Status in Data sources page shows Sync Failed. How do I resolve it?
You can resolve your sync failure by understanding the reason behind the failure. There are two methods to know the reason for the sync failure:
Method 1:
- Open the required workspace.
- Click the Data Sources tab from the left bar.
- The Data Sources page will open. Click the View Last Import Details icon that appears on mouse hover of each table row.
- The Import Details pop-up page will open. You will find the reason for your failure in the Details section. Take the necessary action based on the reason provided.
Method 2:
- Open the corresponding table.
- Navigate through Import Data > Last Import Details.
- The Import Details pop-up page will open. You will find the reason for your failure in the Details section. Take the necessary action based on the reason provided.
14. How do I remove the Setup?
To remove the setup,
- Open the required workspace.
- Click the Data Sources tab from the left bar.
- All the data sources for this workspace will be listed. Click the DigitalOcean PostgreSQL data source that you want to remove.
- In the Data Sources tab that opens, click the Settings icon inline to the data source name on the right.
- Click the Remove Data Source option from the drop-down menu.
Please note that the data source connection will be removed, but the tables and the data will be retained in the workspace. As the data source connected is removed, no further synchronization will happen.
Live Connect
1. How do I connect live with the DigitalOcean PostgreSQL database?
2. How can I edit the live connect setup?
3. How is Live Connect different from Data Import?
Tabulated below are the differences between the Data Import feature and Live Connect feature.
Data Import | Live Connect |
Data in DigitalOcean PostgreSQL will be imported and stored in Zoho Analytics. | Data from DigitalOcean PostgreSQL will be fetched live using appropriate reporting queries whenever you create or access a report in Zoho Analytics. |
Filtered data set can be imported from DigitalOcean PostgreSQL using customized queries. | Custom Query feature is not available in DigitalOcean PostgreSQL Live Connect. However, you can create Views in the source database and connect the same with Zoho Analytics. |
Multiple data sources (apart from DigitalOcean PostgreSQL) can be imported into the same workspace and they can be combined for reporting & analysis purposes. | Cannot import data from any other data source in to the same workspace in which Live Connect from DigitalOcean PostgreSQL is setup. |
Changes made to the columns such as addition/deletion will be synchronized automatically. | Any changes such as column addition/deletion/renaming will not be reflected. You will have to manually map the data using the Sync Design option. |
When importing multiple tables, the foreign keys defined between the tables in the DigitalOcean PostgreSQL database will not be linked in Zoho Analytics. However, you can manually link the tables in Zoho Analytics using the Lookup column feature. | Lookup relationship will be automatically created for tables that are linked via foreign keys in the DigitalOcean PostgreSQL database. You can also manually link the tables in Zoho Analytics using Lookup column feature. |
Users can create query tables. | Users cannot create query tables. |
Report loading time will be fast as the data is stored in Zoho Analytics. | Report loading time directly depends on the server response time and the amount of data in DigitalOcean PostgreSQL. |
4. How long does it take for me to visualize my data in Zoho Analytics?
As there is no data import process involved, the loading time depends upon the amount of data stored in your DigitalOcean PostgreSQL database and also the response time of your DigitalOcean PostgreSQL server.
5. Will the reports/dashboards query hit my database server every time I open it or can it be cached in Zoho Analytics? (or) Can I store a cache of my data points in Zoho Analytics to get quick access to my views?
Zoho Analytics allows you to create a local cache of reports, created over your live connect database. This will increase the speed of loading reports as it will reduce the data fetching time from your live databaseTo enable cache for your live connect workspace, please follow the below steps:
- From your Workspace Explorer , click Settings from the side menubar.
- In the General - Workspace Settings page that opens, choose Yes for Enable Cache for this Workspace.
- In Cache Refresh Interval in Minutes , specify the duration to refresh the report.
- Click Save & Close.
A cache for the reports will be created for the Workspace.
- Enabling cache will help create a cache for your reports in the workspace. This data will get updated periodically based on the time provided in the Cache Refresh Interval in Minutes .
- You can create a cache only for the reports, and not for tables in the workspace.
- This option is available only for Live Connect.
6. Can I connect Views created in DigitalOcean PostgreSQL (apart from Tables) to Zoho Analytics?
Yes, you can connect with both Views and Tables created in DigitalOcean PostgreSQL to Zoho Analytics.
7. Will foreign keys defined between my tables in DigitalOcean PostgreSQL database be linked in Zoho Analytics as well?
Yes. In case you have linked two or more tables in your DigitalOcean PostgreSQL database using foreign keys, they will be linked automatically using a Lookup column in Zoho Analytics as well. You can also manually create a lookup relationship among the imported tables in Zoho Analytics.
8. Can I link the related tables, connected from the Cloud Database using the Live Connect option, in Zoho Analytics?
Yes, you can link the related tables in Zoho Analytics using the lookup column feature. Learn more.
- You will not be able to create Query Tables if you have set up the workspace using the DigitalOcean PostgreSQL Live Connect option as this option does not fetch and store the data locally in Zoho Analytics.
- The Join Tables (lookup column) option will not be available in the Import Wizard. You can create a lookup relation only on the imported tables.
9. I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
This alert message will be displayed when Zoho Analytics is not able to access the information from DigitalOcean PostgreSQL. This could be because the tables/columns that you are trying to access in Zoho Analytics are deleted or renamed in DigitalOcean PostgreSQL.
In this case, it is recommended that you remap the table/column. Refer to this presentation to know how to remap a table.
10. What is a Mismatch?
When you have created reports in Zoho Analytics over the tables or columns which no longer have a direct mapping in DigitalOcean PostgreSQL database, it will be listed as mismatch.
So, ensure that the tables/columns in Zoho Analytics workspace and DigitalOcean PostgreSQL database matches. The tables/columns that do not match will be listed in the Mismatch tab of the DigitalOcean ConnectionSettings page. Refer to the next question to know more about mismatch.
11. When do Mismatches occur and how to resolve them?
12. Can I synchronize the meta data of the table from my Cloud Database instantly?
Yes, you can synchronize the meta data of the table from Cloud Database instantly when needed.
To synchronize the meta data instantly:
- From the workspace explorer, click the Data Sources tab.
- You will get navigated to the DigitalOcean PostgreSQL Connection Settings page. All the tables available in the workspace will be listed.
- Mouse over the required table. The option to sync the table will be displayed inline to the table name.
- Click the Sync link inline to the table name.
- The table meta data from the Cloud Database will get instantly synchronized in Zoho Analytics table.
13. Can I connect new columns added in my DigitalOcean PostgreSQL database to Zoho Analytics?
Yes, you can connect the new columns that are added in your DigitalOcean PostgreSQL database to Zoho Analytics from the DigitalOcean PostgreSQL Connection Settings page. Refer to this presentation to know more.
14. Can I change the data type of the columns in Zoho Analytics?
No, you cannot change the data type of the columns in Zoho Analytics.
15. Can I import data from other data sources into the same workspace that I have used to connect with DigitalOcean PostgreSQL?
No, you cannot import data from other data sources into the same workspace that you have used to connect with DigitalOcean PostgreSQL.
16. Can I create Query Tables over the DigitalOcean PostgreSQL data?
No, you will not be able to create Query Tables if you have set up the workspace using the DigitalOcean PostgreSQL Live Connect option. This is because this option does not fetch and store the data locally in Zoho Analytics. If you wish to create Query Tables, you can create the required query as a view in the data source and connect the same with Zoho Analytics.
17. What happens when I delete or rename the database in DigitalOcean PostgreSQL?
When you delete or rename a database in DigitalOcean PostgreSQL, Zoho Analytics loses its connectivity with DigitalOcean PostgreSQL. After that, a warning message, as shown below, would be displayed. This error message will also be displayed if there are any connectivity issues or if your DigitalOcean PostgreSQL credentials have expired.
For more information regarding the same, refer to the Edit Connection presentation.
18. How do I remove the Setup?
You have to delete the workspace in Zoho Analytics to remove the connection setup.
To delete the workspace,
- From your Zoho Analytics account, click the More Actions icon that appears on mouse hover adjacent to the workspace name that you want to delete.
- Click the Delete Workspace option from the drop-down menu.
19. What are the limitations of using the DigitalOcean PostgreSQL Live Connect?
Given below are a few short comings that one might face while using the DigitalOcean PostgreSQL Live Connect option.
- Data from your DigitalOcean PostgreSQL database will NOT be locally stored in Zoho Analytics. Zoho Analytics will generate appropriate queries to fetch the required data live from DigitalOcean MySQL and show you the report. Hence, the loading time will directly depend on the performance of DigitalOcean MySQL.
- Any changes such as column addition/deletion/renaming will not be mapped automatically. The user must manually map the updates made.
- Users cannot combine data from other data sources into the same workspace in which you have connected the DigitalOcean PostgreSQL database.
- Users cannot create query tables.
- Users cannot change the data type of the columns in Zoho Analytics.
Troubleshooting Tips
1. I get an error message "Sorry, there is a problem in connecting to your cloud data source. Check your connection details and try again." What should I do?
This error occurs in the following scenario:
Scenario | Solution |
Incorrect connection settings are specified | Ensure that the correct Endpoint/Hostname, Port, and user credentials are specified. |
2. I am unable to find the Live Connect option while importing data into Zoho Analytics. What could be the possible reasons?
You will be able to connect live in Zoho Analytics only if,
- You have a paid or trial plan.
- You are importing data into a new Workspace in Zoho Analytics.