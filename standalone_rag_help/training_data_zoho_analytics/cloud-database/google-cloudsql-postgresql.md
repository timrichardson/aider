Import data from Google Cloud SQL PostgreSQL
If you have your data stored online in the Google Cloud SQL PostgresSQL database, then you can seamlessly import your data into Zoho Analytics for reporting and analysis. Zoho Analytics allows you to either import the data into Zoho Analytics or connect directly with the Google Cloud SQL PostgreSQL server.
- Data Import: Data in Google Cloud SQL PostgreSQL will be imported and stored in Zoho Analytics. You can setup periodic schedules to fetch the latest data automatically from your Google Cloud SQL PostgreSQL database. Report loading time will be faster as the data is stored in Zoho Analytics.
- Live Connect: In this mode, data will not be fetched from Google Cloud SQL PostgreSQL and stored in Zoho Analytics. Instead for the reports that you create Zoho Analytics will generate appropriate queries that will connect the required data live from Google Cloud SQL PostgreSQL to Zoho Analytics and show you the report. In this case the loading time will directly depend on the performance of Google Cloud SQL PostgreSQL.
Please note that the Live Connect option is exclusively available for paid plans and trials only. Refer to the Live Connect section to learn.
Data Import
- Preamble: Why should I allowlist Zoho Analytics IP addresses and How do I do it?
- How do I import data from the Google Cloud SQL PostgreSQL database?
- How can I edit the setup?
- How long does it take for the data to be imported into Zoho Analytics?
- Can I import data from Views created in Google Cloud SQL PostgreSQL (apart from Tables) into Zoho Analytics?
- Will foreign keys defined between my tables in Google Cloud SQL PostgreSQL database be linked in Zoho Analytics as well?
- Can I change the data-type of the columns in Zoho Analytics?
- I have synced data from a database into a table. Can I change the data source of this table?
- Can I import data from my Google Cloud SQL PostgreSQL database into an existing Zoho Analytics database?
- Can I synchronize the data from my Cloud Database instantly?
- How do I remove the Setup?
Live Connect
- Preamble: Why should I allowlist Zoho Analytics IP address and how do I do it?
- How do I connect live with the Google Cloud SQL PostgreSQL database?
- How can I edit the live connect setup?
- How is Live Connect different from Data Import?
- How long does it take for me to visualize my data in Zoho Analytics?
- Will the reports/dashboards query hit my database server every time I open it or can it be cached in Zoho Analytics?
- Can I connect Views created in Google Cloud SQL PostgreSQL (apart from Tables) to Zoho Analytics?
- Will foreign keys defined between my tables in Google Cloud SQL PostgreSQL database be linked in Zoho Analytics as well?
- I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
- What is a Mismatch?
- When do Mismatches occur and how to resolve them?
- Can I connect the new columns added in my Google Cloud SQL PostgreSQL database to Zoho Analytics?
- Can I change the data-type of the columns in Zoho Analytics?
- Can I import data from other data sources into the same workspace that I have used to connect with Google Cloud SQL PostgreSQL?
- Can I create Query Tables over the Google Cloud SQL PostgreSQL data?
- What happens when I delete or rename the database in Google Cloud SQL PostgreSQL?
- How do I remove the Setup?
- What are the limitations of Google Cloud SQL PostgreSQL Live Connect?
Data Import
1. Preamble: Why should I allowlist Zoho Analytics IP addresses and How do I do it?
2. How do I import data from the Google Cloud SQL PostgreSQL database?
3. How can I edit the setup?
4. How long does it take for the data to be imported into Zoho Analytics?
After setup, you might have to wait some time for the initial fetch to happen. This depends upon the amount of data fetched from Google Cloud SQL PostgreSQL database and also the response time of the Google Cloud SQL PostgreSQL server. You will receive an email notification once the import is complete. If you access the Workspace before the initial fetch, it will not display any data.
5. Can I import data from Views created in Google Cloud SQL PostgreSQL (apart from Tables) into Zoho Analytics?
Yes, you can import data from both Views and Tables into Zoho Analytics.
6. Will foreign keys defined between my tables in Google Cloud SQL PostgreSQL database be linked in Zoho Analytics as well?
When importing multiple tables, the foreign keys defined between the tables in Google Cloud SQL PostgreSQL database will be linked in Zoho Analytics. The foreign keys will be created as Look-up columns in Zoho Analytics.
If you import data from one table at a time (choosing single table option) then the foreign keys will not be defined. However, you can manually link the tables in Zoho Analytics using the Look-up column feature. Click here to learn about the Look-up column feature.
7. Can I change the data-type of the columns imported in Zoho Analytics?
Yes, you can change the datatype of the columns imported into Zoho Analytics. However, it is necessary that the datatype of your column is compatible with the datatype of the column in your Google Cloud SQL PostgreSQL console for successful data synchronizations. It is always recommended that you change the data type in both your Google Cloud SQL PostgreSQL database as well as your Zoho Analytics database.
8. I have synced data from a database into a table. Can I change the data source of this table?
Yes, you can change the data source of a table, into which the Google Cloud SQL PostgreSQL database has been synced.
Follow the below steps to import if the source is available in the same Google Cloud SQL PostgreSQL database that is imported into the table.
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
9. Can I import data from my Google Cloud SQL PostgreSQL database into an existing Zoho Analytics database?
Yes. Follow the below steps to import data into an existing database:
- Open the Workspace into which you wish to import the data.
- Click the Import Data button in the Explorer tab.
- Click Cloud Databases option.
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
- In the Explorer tab, click Data Sources button.
- In the Data Sources tab that opens click the Settings icon and select Remove Data Source as shown in the snapshot.
Please do note that this only removes the connection. You can still continue accessing the Workspace in Zoho Analytics.
Live Connect
1. Preamble: Why should I allowlist Zoho Analytics IP addresses and How do I do it?
2. How do I connect live with the Google Cloud SQL PostgreSQL database?
3. How can I edit the live connect setup?
4. How is Live Connect different from Data Import?
Tabulated below are the differences between the Data Import feature and Live Connect feature.
| Data Import | Live Connect |
| Data in Google Cloud SQL PostgreSQL will be imported and stored in Zoho Analytics. | Data from Google Cloud SQL PostgreSQL will be fetched live using appropriate reporting queries whenever you create or access a report in Zoho Analytics. |
| Filtered data set can be imported from Google Cloud SQL PostgreSQL using customized queries. | Custom Query feature is not available in Google Cloud SQL PostgreSQL Live Connect. |
| Multiple data sources (apart from Google Cloud SQL PostgreSQL) can be imported into the same workspace and they can be combined for reporting & analysis purpose. | Cannot import data from any other data source into the same workspace in which Live Connect from Google Cloud SQL PostgreSQL is setup. |
| Changes made to the columns such as addition/deletion will be synchronized automatically. | Any changes such as column addition/deletion/renaming will not be reflected. You will have to manually map the data using the Sync Design option. |
| When importing multiple tables, the foreign keys defined between the tables in Google Cloud SQL PostgreSQL database will be linked in Zoho Analytics. The foreign keys will be created as Look-up columns in Zoho Analytics. If you import data from one table at a time (choosing single table option) then the foreign keys will not be defined. However, you can manually link the tables in Zoho Analytics using the Look-up column feature. | Look-up relationship will be automatically created for tables that are linked via foreign keys in Google Cloud SQL PostgreSQL. However, you cannot manually link the tables in Zoho Analytics using Look-up column feature. |
| Users can create query tables. | Users cannot create query tables. |
| Report loading time will be fast as the data is stored in Zoho Analytics. | Report loading time directly depends on the Google Cloud SQL PostgreSQL server response time and the amount of data in Google Cloud SQL PostgreSQL. |
5. How long does it take for me to visualize my data in Zoho Analytics?
As there is no data import process involved, the loading time depends upon the amount of data stored in your Google Cloud SQL PostgreSQL database and also the response time of your Google Cloud SQL PostgreSQL server.
6. Will the reports/dashboards query hit my database server every time I open it or can it be cached in Zoho Analytics?
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
7. Can I connect Views created in Google Cloud SQL PostgreSQL (apart from Tables) to Zoho Analytics?
Yes, you can connect with both Views and Tables created in Google Cloud SQL PostgreSQL to Zoho Analytics.
8. Will foreign keys defined between my tables in Google Cloud SQL PostgreSQL database be linked in Zoho Analytics as well?
Yes. In case you have linked two or more tables in your Google Cloud SQL PostgreSQL database using foreign keys, they will be linked automatically using a Look-up column in Zoho Analytics as well.
9. I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
This alert message will be displayed when Zoho Analytics is not able to access the information from Google Cloud SQL PostgreSQL. This could be because the tables/columns that you are trying to access in Zoho Analytics is deleted or renamed in Google Cloud SQL PostgreSQL.
In this case, it is recommended that you remap the table/column. Refer to this presentation to know how to remap a table.
10. What is a Mismatch?
When you have created reports in Zoho Analytics over the tables or columns which no longer have a direct mapping in Google Cloud SQL PostgreSQL database, it will be listed as mismatch.
So, ensure that the tables/columns in Zoho Analytics workspace and Google Cloud SQL PostgreSQL database matches. The tables/columns that do not match will be listed in the Mismatch tab of the Google Cloud SQL Connection Settings page. Refer the next question to know more about mismatch.
11. When do Mismatches occur and how to resolve them?
12. Can I connect new columns added in my Google Cloud SQL PostgreSQL database to Zoho Analytics?
Yes, you can connect the new columns that are added in your Google Cloud SQL PostgreSQL database to Zoho Analytics from the Google Cloud SQL Connection Settings page. Refer to this presentation to know more.
Note:
If there exists a mismatch between the already available data in your Zoho Analytics workspace and your Google Cloud SQL PostgreSQL database, Zoho Analytics will NOT be able to fetch the new column information. In this case, you need to first resolve the mismatches to connect to the new columns.
13. Can I change the data-type of the columns in Zoho Analytics?
No, you cannot change the data type of the columns in Zoho Analytics.
14. Can I import data from other data sources into the same workspace that I have used to connect with Google Cloud SQL PostgreSQL?
No, you cannot import data from other data sources into the same workspace that you have used to connect with Google Cloud SQL PostgreSQL.
15. Can I create Query Tables over the Google Cloud SQL PostgreSQL data?
No, you will not be able to create Query Tables if you have setup the workspace using the Google Cloud SQL PostgreSQL Live Connect option. This is because this option does not fetch and store the data locally in Zoho Analytics. If you wish to create Query Tables, we request you to use the Data Import option.
16. What happens when I delete or rename the database in Google Cloud SQL PostgreSQL?
When you delete or rename a database in Google Cloud SQL PostgreSQL, Zoho Analytics loses its connectivity with Google Cloud SQL PostgreSQL. Thereafter, a warning message, as shown below, would be displayed. This error message will also be displayed if there are any connectivity issues or if your Google Cloud SQL PostgreSQL credentials have expired.
For more information regarding the same, refer to the Edit Connection presentation.
17. How do I remove the Setup?
You have to delete the workspace in Zoho Analytics to remove the connection setup.
To delete the workspace,
- Log in to Zoho Analytics
- Click the More Actions icon that appears on mouse hover adjacent to the workspace name that you want to delete
- Click the Delete Workspace option
18. What are the limitations of using the Google Cloud SQL PostgreSQL Live Connect?
Given below are a few shortcomings that one might face while using the Google Cloud SQL PostgreSQL Live Connect option.
- Data from your Google Cloud SQL PostgreSQL database will NOT be locally stored in Zoho Analytics. Zoho Analytics will generate appropriate queries to fetch the required data live from Google Cloud SQL PostgreSQL and show you the report. Hence, the loading time will directly depend on the performance of Google Cloud SQL PostgreSQL.
- Any changes such as column addition/deletion/renaming will not be mapped automatically. The user must manually map the updates made.
- Users cannot combine data from other data sources into the same workspace in which you have connected the Google Cloud SQL PostgreSQL database.
- Users cannot create query tables.