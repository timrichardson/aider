Import data from Microsoft Azure Maria DB
If you have your data stored in Microsoft Azure Maria DB Cloud Database, then you can easily import your data into Zoho Analytics for reporting & analysis. You can also set up schedules to fetch the latest data from your Microsoft Azure Maria DB database periodically.
Data Import
- Preamble: Why should I allowlist Zoho Analytics IP address and how do I do it?
- How do I import data from the Microsoft Azure Maria DB database?
- How can I edit the setup?
- How long does it take for the data to be imported into Zoho Analytics?
- Can I import data from Views created in Microsoft Azure Maria DB (apart from Tables) into Zoho Analytics?
- Will foreign keys defined between my tables in the Microsoft Azure Maria DB database be linked in Zoho Analytics as well?
- Can I change the data-type of the columns in Zoho Analytics?
- I have synced data from a database into a table. Can I change the data source of this table?
- Can I import data from my Microsoft Azure Maria DB database into an existing Zoho Analytics workspace?
- Can I synchronize the data from my Cloud Database instantly?
- How do I remove the Setup?
Troubleshooting Tips
1. Preamble: Why should I allowlist Zoho Analytics IP addresses and How do I do it?
2. How do I import data from the Microsoft Azure Maria DB database?
3. How can I edit the setup?
4. How long does it take for the data to be imported into Zoho Analytics?
After setup, you might have to wait sometime for the initial fetch to happen. This depends upon the amount of data to be imported into Zoho Analytics and also the response time of your Microsoft Azure Maria DB server. You will receive an email notification once the import is complete. Please note that, if you access the workspace before the initial fetch, it will not display any data.
5. Can I import data from Views created in Microsoft Azure Maria DB (apart from Tables) into Zoho Analytics?
Yes, you can import data from both Views and Tables into Zoho Analytics.
6. Will foreign keys defined between my tables in the Microsoft Azure Maria DB database be linked in Zoho Analytics as well?
When importing multiple tables, the foreign keys defined between the tables in Microsoft Azure Maria DB database will be linked in Zoho Analytics. The foreign keys will be created as Look-up columns in Zoho Analytics.
If you import data from one table at a time (choosing single table option) then the foreign keys will not be defined. However, you can manually link the tables in Zoho Analytics using the Look-up column feature. Click here to learn about the Look-up column feature.
7. Can I change the data-type of the columns imported in Zoho Analytics?
Yes, you can change the datatype of the columns imported into Zoho Analytics. However it is necessary that the data-type of your column is compatible with the data-type of the column in your Microsoft Azure Maria DB database for successful data synchronizations. It is always recommended that you change the data type in both your Microsoft Azure Maria DB database as well as your Zoho Analytics workspace.
8. I have synced data from a database into a table. Can I change the data source of this table?
Yes, you can change the data source of a table, into which the Microsoft Azure Maria DB database has been synced.
Follow the below steps to import if the source is available in the same Microsoft Azure Maria DB database that is imported into the table.
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
9. Can I import data from my Microsoft Azure Maria DB database into an existing Zoho Analytics workspace?
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
Troubleshooting Tips
1. I get this error message, "Login failed, please check the username and password" when I try to authenticate the Microsoft Azure Maria DB database. How do I resolve it?
The above message will be displayed when
- the Username and/or the Password provided for authentication is incorrect,
- or the Zoho Analytics IP addresses are not allow listed.
To resolve this,
- provide the correct Username and Password
- write a query to add a new user to the database, and allow list the Zoho Analytics IP addresses.
The below query explains how to add users.
CREATE USER 'username'@'host' IDENTIFIED WITH mysql\_native\_password BY 'password'
In the place of 'host', you can provide Zoho Analytics IP addresses. % can be provided as a wildcard character to connect from any IP address.
CREATE USER 'username'@'136.143.%.%' IDENTIFIED WITH mysql\_native\_password BY 'password'
%can be provided as a wildcard character to connect from any IP address.
CREATE USER 'username'@'%' IDENTIFIED WITH mysql\_native\_password BY 'password'