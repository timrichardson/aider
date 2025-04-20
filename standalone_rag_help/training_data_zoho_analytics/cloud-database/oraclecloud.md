Import data from Oracle Cloud
If you have your data stored in Oracle Cloud Database, then you can easily import your data into Zoho Analytics for reporting & analysis. Zoho Analytics allows you to either import the data into Zoho Analytics or connect directly with the Oracle server.
- Data Import: Data in Oracle Cloud will be imported and stored in Zoho Analytics. You can setup periodic schedules to fetch the latest data automatically from your Oracle Cloud database. Report loading time will be faster as the data is stored in Zoho Analytics.
- Live Connect: In this mode, data will not be fetched from Oracle Cloud and stored in Zoho Analytics. Instead for the reports that you create Zoho Analytics will generate appropriate queries that will connect the required data live from Oracle Cloud to Zoho Analytics and show you the report. In this case the loading time will directly depend on the performance of Oracle Cloud.
Please note that the Live Connect option is exclusively available for paid plans and trials only. Refer to the Live Connect section to learn.
Data Import
- How do I import data from the Oracle Cloud database?
- What can I do if I am unable to find the Public IP in my Oracle DB Systems page?
- How can I edit the setup?
- How long does it take for the data to be imported into Zoho Analytics?
- Can I import data from Views created in Oracle Cloud (apart from Tables) into Zoho Analytics?
- Will foreign keys defined between my tables in the Oracle Cloud database be linked in Zoho Analytics as well?
- Can I change the data type of the columns in Zoho Analytics?
- I have connected to a database and imported a few tables into Zoho Analytics. Can I add more tables from the same source to the existing connection?
- Can I import data from Oracle Cloud database into an existing table in Zoho Analytics?
- I have synced data from a database into a table. Can I change the data source of this table?
- Can I import data from my Oracle Cloud database into an existing Zoho Analytics workspace?
- Can I synchronize the data from my Cloud Database instantly?
- The Last Data Sync Status in Datasources page shows Sync Failed. How do I resolve it?
- How do I remove the Setup?
Live Connect [Beta]
- How do I connect live with the Oracle Cloud database?
- How can I edit the live connect setup?
- How is Live Connect different from Data Import?
- How long does it take for me to visualize my data in Zoho Analytics?
- Will the reports/dashboards query hit my database server every time I open it or can it be cached in Zoho Analytics?
- Can I connect Views created in Oracle Cloud (apart from Tables) to Zoho Analytics?
- Will foreign keys defined between my tables in Oracle Cloud database be linked in Zoho Analytics as well?
- Can I link the related tables, connected from the Cloud Database using the Live Connect option, in Zoho Analytics?
- I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
- What is a Mismatch?
- When do Mismatches occur and how to resolve them?
- Can I synchronize a data table from my Cloud Database instantly?
- Can I connect the new columns added in my Oracle Cloud database to Zoho Analytics?
- Can I change the data type of the columns in Zoho Analytics?
- Can I import data from other data sources into the same workspace that I have used to connect with Oracle Cloud?
- Can I create Query Tables over the Oracle Cloud data?
- What happens when I delete or rename the database in Oracle Cloud?
- How do I delete a view from a workspace?
- How to restore a deleted view in the workspace?
- How do I remove the Setup?
- What are the limitations of Oracle Cloud Live Connect?
Troubleshooting Tips
- I get an error message "Sorry, there is a problem in connecting to your cloud data source. Check your connection details and try again." What should I do?
- I am unable to find the Live Connect option while importing data into Zoho Analytics. What could be the possible reasons?
Data Import
1. How do I import data from the Oracle Cloud database?
2. What can I do if I am unable to find the Public IP in my Oracle DB Systems page?
If you are unable to find the Public IP in your Oracle DB Systems page, then create a Virtual Cloud Network for your database in the Oracle Cloud console.
3. How can I edit the setup?
4. How long does it take for the data to be imported into Zoho Analytics?
After setup, you might have to wait sometime for the initial fetch to happen. This depends upon the amount of data to be imported into Zoho Analytics and also the response time of your Oracle Cloud server. You will receive an email notification once the import is complete. Please note that, if you access the workspace before the initial fetch, it will not display any data.
5. Can I import data from Views created in Oracle Cloud (apart from Tables) into Zoho Analytics?
Yes, you can import data from Tables as well as Views available in your Oracle Cloud database into your Zoho Analytics workspace.
6. Will foreign keys defined between my tables in the Oracle Cloud database be linked in Zoho Analytics as well?
When importing multiple tables, the foreign keys defined between the tables in Oracle Cloud database will be linked in Zoho Analytics. The foreign keys will be created as Look-up columns in Zoho Analytics.
If you import data from one table at a time (choosing single table option) then the foreign keys will not be defined. However, you can manually link the tables in Zoho Analytics using the Look-up column feature. Click here to learn about the Look-up column feature.
7. Can I change the data type of the columns imported in Zoho Analytics?
Yes, you can change the datatype of the columns imported into Zoho Analytics. However it is necessary that the data-type of your column is compatible with the data-type of the column in your Oracle Cloud database for successful data synchronizations. It is always recommended that you change the data type in both your Oracle Cloud database as well as your Zoho Analytics workspace.
8. I have connected to a database and imported a few tables into Zoho Analytics. Can I add more tables from the same source to the existing connection?
Yes, you can add tables from the same source to the existing connection. Follow the below steps:
- From your Oracle Cloud workspace, navigate to Create > New Table / Import Data.
- Click the Cloud Databases option. The Connect to Cloud Database wizard will open.
- From the Connection name drop down menu, select the existing Oracle Cloud database name.
- The rest of the steps are similar to importing data from cloud database.
9. Can I import data from Oracle Cloud database into an existing table in Zoho Analytics?
Yes, you can import data into an existing table if you are importing from the same source database as the imported table.
- From the required table, click Import Data > Import Data into this Table.
- The Select Data to Import tab of the Import wizard will open.
- You can choose to import from the same table or a different table using the Select Table option, or import using the Custom Query.
- The rest of the steps are similar to importing from a single table.
10. I have synced data from Oracle Cloud database into a table. Can I change the data source of this table?
Yes, you can change the data source of a table, into which the Oracle Cloud database has been synced. To do this,
- Open the workspace.
- Click the Data Sources tab from the left bar.
- All the data sources for this workspace will be listed. Click the data source you want to edit.
- The Data Sources page will open. Click the Edit Connection link.
- In the Cloud Database - Edit Connection dialog that opens, modify the data source.
- Click Save to implement the changes made.
11. Can I import data from my Oracle Cloud database into an existing Zoho Analytics workspace?
Yes. Follow the below steps to import data into an existing workspace:
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
13. The Last Data Sync Status in Datasources page shows Sync Failed. How do I resolve it?
You can resolve your sync failure by understanding the reason behind the failure. There are two methods to know the reason for the sync failure:
Method 1:
- Open the required workspace.
- Click the Data Sources tab from the left bar.
- All the data sources for this workspace will be listed. Click the data source that has failed to sync.
- The Data Sources page will open. Click the View Last Import Details icon that appears on mouse over of each table row.
- The Import Details pop-up page will open. You will find the reason for your failure in the Details section. Take the necessary action based on the reason provided.
Method 2:
- Open the corresponding table.
- Navigate through Import Data > Last Import Details.
- The Import Details pop-up page will open. You will find the reason for your failure in the Details section. Take the necessary action based on the reason provided.
14. How do I remove the Setup?
To remove the setup,
- Open the required workspace.
- Click the Data Sources tab from the left bar.
- All the data sources for this workspace will be listed. Click the Oracle Cloud data source that you want to remove.
- In the Data Sources tab that opens, click the Settings icon inline to the data source name on the right.
- Click the Remove Data Source option from the drop-down menu.
Please note that the data source connection will be removed, but the tables and the data will be retained in the workspace. As the data source connected is removed, no further synchronization will happen.
Live Connect [Beta]
1. How do I connect live with the Oracle Cloud database?
2. How can I edit the live connect setup?
3. How is Live Connect different from Data Import?
Tabulated below are the differences between the Data Import feature and Live Connect feature.
| Data Import | Live Connect |
| Data in Oracle Cloud will be imported and stored in Zoho Analytics. | Data from Oracle Cloud will be fetched live using appropriate reporting queries whenever you create or access a report in Zoho Analytics. |
| Filtered data set can be imported from Oracle Cloud using customized queries. | Custom Query feature is not available in Oracle Cloud Live Connect. However, you can create Views in the source database and connect the same with Zoho Analytics. |
| Multiple data sources (apart from Oracle Cloud) can be imported into the same workspace and they can be combined for reporting & analysis purpose. | Cannot import data from any other data source into the same workspace in which Live Connect from Oracle Cloud is setup. |
| Changes made to the columns such as addition/deletion will be synchronized automatically. | Any changes such as column addition/deletion/renaming will not be reflected. You will have to manually map the data using the Sync Design option. |
| When importing multiple tables, the foreign keys defined between the tables in the Oracle Cloud database will not be linked in Zoho Analytics. However, you can manually link the tables in Zoho Analytics using the Look-up column feature. | Look-up relationship will be automatically created for tables that are linked via foreign keys in the Oracle Cloud database. You can also manually link the tables in Zoho Analytics using Look-up column feature. |
| Users can create query tables. | Users cannot create query tables. |
| Report loading time will be fast as the data is stored in Zoho Analytics. | Report loading time directly depends on the Oracle Cloud server response time and the amount of data in Oracle Cloud. |
4. How long does it take for me to visualize my data in Zoho Analytics?
As there is no data import process involved, the loading time depends upon the amount of data stored in your Oracle Cloud database and also the response time of your Oracle Cloud server.
5. Will the reports/dashboards query hit my database server every time I open it or can it be cached in Zoho Analytics?
(or) Can I store a cache of my data points in Zoho Analytics to get quick access to my views?
Zoho Analytics allows you to create a cache for the reports in your live connect database to reduce the query fetching time.
To enable cache for your live connect workspace, please follow the below steps:
- From your Workspace Explorer, click Settings from the side menubar.
- In the General - Workspace Settings page that opens, choose Yes for Enable Cache for this Workspace.
- Provide Cache Refresh Interval in Minutes.
- Click Save & Close.
A cache for the reports will be created for the Workspace.
Note:
- Enabling cache will help create a cache for your reports in the workspace. This data will get updated periodically based on the time provided in the Cache Refresh Interval in Minutes.
- You can create a cache only for the reports, and not for tables in the workspace.
- This option is available only for Live Connect.
6. Can I connect Views created in Oracle Cloud (apart from Tables) to Zoho Analytics?
Yes, you can connect with both Views and Tables created in Oracle Cloud to Zoho Analytics.
7. Will foreign keys defined between my tables in Oracle Cloud database be linked in Zoho Analytics as well?
Yes. In case you have linked two or more tables in your Oracle Cloud database using foreign keys, they will be linked automatically using a Look-up column in Zoho Analytics as well. You can also manually create a lookup relationship among the imported tables in Zoho Analytics.
8. Can I link the related tables, connected from the Cloud Database using the Live Connect option, in Zoho Analytics?
Yes, you can link the related tables in Zoho Analytics using the lookup column feature. Learn more.
Note:
- You will not be able to create Query Tables if you have setup the workspace using the Oracle Cloud Live Connect option as this option does not fetch and store the data locally in Zoho Analytics.
- The Join Tables (lookup column) option will not be available in the Import Wizard. You can create a lookup relation only on the imported tables.
9. I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
This alert message will be displayed when Zoho Analytics is not able to access the information from Oracle Cloud. This could be because the tables/columns that you are trying to access in Zoho Analytics is deleted or renamed in Oracle Cloud.
In this case, it is recommended that you remap the table/column. Refer to this presentation to know how to remap a table.
10. What is a Mismatch?
When you have created reports in Zoho Analytics over the tables or columns which no longer have a direct mapping in Oracle Cloud database, it will be listed as mismatch.
So, ensure that the tables/columns in Zoho Analytics workspace and Oracle Cloud database matches. The tables/columns that do not match will be listed in the Mismatch tab of the Oracle Cloud Connection Settings page. Refer the next question to know more about mismatch.
11. When do Mismatches occur and how to resolve them?
12. Can I synchronize a data table from my Cloud Database instantly?
Yes, you can synchronize your data table from Cloud Database instantly when needed.
To synchronize your data instantly:
- From the workspace explorer, click the Data Sources tab.
- You will get navigated to the Oracle Cloud Connection Settings page. All the tables available in the workspace will be listed.
- Mouse over the required table. The option to sync the table will be displayed inline to the table name.
- Click the Sync link inline to the table name.
- The table data from the Cloud Database will get instantly synchronized in Zoho Analytics table.
13. Can I connect new columns added in my Oracle Cloud database to Zoho Analytics?
Yes, you can connect the new columns that are added in your Oracle Cloud database to Zoho Analytics from the Oracle Cloud Connection Settings page. Refer to this presentation to know more.
Note: If there exists a mismatch between the already available data in your Zoho Analytics workspace and your Oracle Cloud database, Zoho Analytics will NOT be able to fetch the new column information. In this case, you need to first resolve the mismatches to connect to the new columns.
14. Can I change the data type of the columns in Zoho Analytics?
No, you cannot change the data type of the columns in Zoho Analytics.
15. Can I import data from other data sources into the same workspace that I have used to connect with Oracle Cloud?
No, you cannot import data from other data sources into the same workspace that you have used to connect with Oracle Cloud.
16. Can I create Query Tables over the Oracle Cloud data?
No, you will not be able to create Query Tables if you have setup the workspace using the Oracle Cloud Live Connect option. This is because this option does not fetch and store the data locally in Zoho Analytics. If you wish to create Query Tables, we request you to use the Data Import option.
17. What happens when I delete or rename the database in Oracle Cloud?
When you delete or rename a database in Oracle Cloud, Zoho Analytics loses its connectivity with Oracle Cloud. Thereafter, a warning message, as shown below, would be displayed. This error message will also be displayed if there are any connectivity issues or if your Oracle Cloud credentials have expired.
For more information regarding the same, refer to the Edit Connection presentation.
18. How do I delete a view from a workspace?
You can easily delete a view from a live connect workspace, by following the below steps:
- Click the More Actions icon that appears on mouse-over the view name.
- Click the Delete option from the drop-down menu.
- You can also delete multiple views by selecting all the views that you want to delete and clicking the Delete option from the top.
The deleted views will be successfully removed from the workspace and placed in Trash. You can restore the views within 45 days of deletion from the Trash. After the mentioned timeframe, the views will get deleted permanently.
19. How to restore a deleted view in the workspace?
You can restore a deleted view from the workspace trash. To restore a deleted view,
- Open the trash by clicking the Trash icon on the left menubar of the workspace.
- All the deleted views will be listed here. You can restore the required view by clicking the Restore icon that appears on mouse-over the view.
- You can restore multiple views by selecting the required views and clicking the Restore option from the top.
Note:
- You cannot have two or more of the same tables with the same name in a workspace, hence you cannot restore a table if you have connected to the same table from the source database.
- When you have two or more of the same tables in the trash, you can restore only one table. This instance occurs when you import and delete the same table multiple times.
20. How do I remove the Setup?
You have to delete the workspace in Zoho Analytics to remove the connection setup.
To delete the workspace,
- Log in to Zoho Analytics
- Click the More Actions icon that appears on mouse hover adjacent to the workspace name that you want to delete
- Click the Delete Workspace option
21. What are the limitations of using the Oracle Cloud Live Connect?
Given below are a few shortcomings that one might face while using the Oracle Cloud Live Connect option.
- Data from your Oracle Cloud database will NOT be locally stored in Zoho Analytics. Zoho Analytics will generate appropriate queries to fetch the required data live from Oracle Cloud and show you the report. Hence, the loading time will directly depend on the performance of Oracle Cloud.
- Any changes such as column addition/deletion/renaming will not be mapped automatically. The user must manually map the updates made.
- Users cannot combine data from other data sources into the same workspace in which you have connected the Oracle Cloud database.
- Users cannot create query tables.
- Users cannot change the data type of the columns in Zoho Analytics.
Troubleshooting Tips
1. I get an error message "Sorry, there is a problem in connecting to your cloud data source. Check your connection details and try again." What should I do?
This error occurs in the following scenarios:
| Scenario | Solution |
| Incorrect connection settings are specified | Ensure that the correct user credentials are specified. |
| Your cloud database service does not recognize Zoho Analytics as an authenticated agent to fetch the data | To import data from Oracle Cloud you need to allowlist Zoho Analytics IP address. |
2. I am unable to find the Live Connect option while importing data into Zoho Analytics. What could be the possible reasons?
You will be able to connect live in Zoho Analytics only if,
- You have a paid or trial plan.
- You are importing data into a new Workspace in Zoho Analytics.