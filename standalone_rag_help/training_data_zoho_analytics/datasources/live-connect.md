Live Connect
Live Connect enables direct, real-time connection to the data source, ensuring that up-to-the-minute data is used for analysis. In this method, the data is not imported or stored within the Zoho Analytics application.
Meta information about the data is obtained, and queries are generated based on the user action and executed directly on the source database. Each time a view is created or accessed, the data is directly fetched from the source database.
On this Page
- Why Choose Live Connect
- Data Import vs Live Connect
- Configuring a Live Connection
- Manage Data Source - Live Connect
- Limitations
- Frequently Asked Questions
Why choose Live Connect?
Faster and Real-time Insights: As live connections reflect data changes instantly, this ensures reports and dashboards are always up to date, enabling faster decision-making.
Single Source of truth: Since the data is queried in real time, it eliminates the need to sync different copies of the data which significantly reduces data discrepancies.
Security compliance: Many organizations prefer not to have their data stored in external applications. Live Connect helps mitigate this risk by ensuring that sensitive data remains in its original location, minimizing the possibility of exposure. Additionally, Zoho Analytics deploys robust encryption mechanisms like SSL (Secure Sockets Layer) and SSH (Secure Shell Protocol) for secure data transmission.
Data Import vs Live Connect
| Data Import | Live Connect |
| Data is imported and stored in Zoho Analytics. | Data will be fetched live using appropriate reporting queries whenever you create or access a report in Zoho Analytics. |
| Filtered data set can be imported from the data source using customized queries. | Custom Query feature is not available in Live Connect. However, you can create Views in the source database and connect the same to Zoho Analytics. |
| Multiple data sources can be imported into the same workspace, and they can be combined for reporting & analysis purposes. | Multiple data sources can be imported into the same workspace, and they can be combined for reporting & analysis |
| Changes made to the columns, such as addition/deletion, will be synchronized automatically. | Any changes, such as column addition, deletion, or renaming, will not be reflected. You will have to manually map the data using the Sync Design option. |
| When importing multiple tables, the foreign keys defined between the tables in the source database will not be linked in Zoho Analytics. However, you can manually link the tables in Zoho Analytics using the Lookup column feature. | Lookup relationship will be automatically created for tables that are linked via foreign keys in the source database. You can also manually link the tables in Zoho Analytics using Lookup column feature. |
| Users can create query tables. | Users cannot create query tables. |
| Report loading time will be fast as the data is stored in Zoho Analytics. | Report loading time directly depends on the server response time and the amount of data in the source database. |
Configuring a Live Connection
Zoho Analytics allows you to configure Live Connect both as a new connection or as an additional data source to an existing workspace.
Follow the below steps to set up a live connection:
- Click Import Your Data from the Zoho Analytics home page.
- Choose Databases and Data lakes.
- Select the Data source; here, we are using the Amazon RDS data source for demo.
- Specify the End Point, Username, Password, and the Database Name (as in Amazon Redshift)
- Choose Live Connect from the Connection Type.
- Click Next.
- Choose the tables you want to connect live with Zoho Analytics and click Connect.
Note:
- As there is no data import process involved, the loading time depends upon the amount of data stored in the source and response time of the source database.
- Currently, lookup rules can be defined only for the tables within the same live connect data source. Lookups cannot be defined for other data sources. However, the reports of both Live Connect and other data sources can be combined by creating dashboards.
Manage Data Source - Live Connect
The Data Sources tab is the central hub that helps manage all the connection settings of the data sources in the workspace. User with the Administrator Privilege can access the data sources tab and make necessary changes when needed.
Access the Data Sources tab from the side navigation panel and choose the live connection for which you want to view and modify the settings.
This tab provides the general details like the Database Type, Database Name, Created On date, Sync Status, Sync Time, number of Tables accessible in Zoho Analytics.
Edit Connection
Enables admins to re-authenticate and update the connection details such as credentials or configuration settings without causing any interruption to the connection.
Sync Design
In live connect, changes made to the data, such as a data type change, renaming of tables or columns, addition or deletion of tables in the source application, are not synced automatically. This Sync Design option allows you to accommodate all the changes made. In the case of any dissimilarity between Zoho Analytics and the source application, the corresponding tables are listed in the Mismatch tab. Refer to the Mismatch section to learn more.
Add Tables
To connect more tables, click the Add More Tables option and choose the tables to connect.
Manage Tables
- To include the recent changes made to the data source, click the Sync option adjacent to the table name.
- To remove a table, Click the Delete option adjacent to the table name.
Audit History
Audit logs are crucial for maintaining security and troubleshooting issues. They provide a comprehensive record of User and System Actions, including details of the time when the action occurred and information about the administrator who performed the action. Audit logs are maintained for each data source configured in the workspace.
Select any action in the audit history to view complete information about the tables on which the action is performed.
The following are the User Actions and the System Actions that are logged in Zoho Analytics
| User Actions | Description |
| Data Source Creation | Provides the details of the admin who configured the connection. |
| Table level Sync Design | Provides the details of the admin who synced the table design |
| Sync Design | Provides the details of the admin who synced the design |
Mismatch
When the reports are created over the tables or columns that no longer have a direct mapping in the source database, it will be listed as a mismatch.
So, ensure that the tables/columns in Zoho Analytics workspace and the source application always match. The tables/columns that do not match will be listed in the Mismatch tab. Refer to the below presentation to resolve mismatches.
Removing Connection
Zoho Analytics allows you to remove a connection from the workspace if it is not required for analysis. All the tables and its related reports will be deleted along with the source.
Access the data source tab and click the Settings icon and choose Remove Data Source from the drop-down menu.
Limitations
- Data from your source database will NOT be locally stored in Zoho Analytics. Zoho Analytics will generate appropriate queries to fetch the required data live from source and show you the report. Hence, the loading time will directly depend on the performance of source database.
- Any changes, such as column addition/deletion/renaming, will not be mapped automatically. The user must manually map the updates made.
- Lookup rules can only be defined between tables in a live connection.
- Users cannot create query tables.
- Users cannot change the data type of the columns in Zoho Analytics.
Frequently Asked Questions
1.I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
This alert message will be displayed when Zoho Analytics is not able to access the information from source. This could be because the tables/columns that you are accessing in Zoho Analytics are deleted or renamed in the source database. Refer to the Mismatch section to learn more.