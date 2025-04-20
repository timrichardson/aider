Import data from SingleStore
If you have your data stored in SingleStore Cloud Database, then you can easily import your data into Zoho Analytics for reporting & analysis. You can setup periodic schedules to fetch the latest data automatically from your SingleStore database. Report loading time will depend on the amount of data stored in Zoho Analytics.
Data Import
- Preamble: Why should I allowlist Zoho Analytics IP address and how do I do it?
- How do I import data from the SingleStore database?
- How can I edit the setup?
- How long does it take for the data to be imported into Zoho Analytics?
- Can I import data from Views created in SingleStore (apart from Tables) into Zoho Analytics?
- Will foreign keys defined between my tables in the SingleStore database be linked in Zoho Analytics as well?
- Can I change the data type of the columns in Zoho Analytics?
- I have connected to a database and imported a few tables into Zoho Analytics. Can I add more tables from the same source to the existing connection?
- Can I import data from SingleStore database into an existing table in Zoho Analytics?
- I have synced data from a database into a table. Can I change the data source of this table?
- Can I import data from my SingleStore database into an existing Zoho Analytics workspace?
- Can I synchronize the data from my Cloud Database instantly?
- The Last Data Sync Status in Datasources page shows Sync Failed. How do I resolve it?
- How do I remove the Setup?
1. Preamble: Why should I allowlist Zoho Analytics IP addresses and How do I do it?
It is mandatory that you allowlist Zoho Analytics IP addresses before you setup the import process. This is important because SingleStore will allow Zoho Analytics to access the data only after you allowlist these IP addresses.
To allowlist Zoho Analytics IP, go to SingleStore Home page > Firewall.
2. How do I import data from the SingleStore database?
3. How can I edit the setup?
You can edit the import setup anytime by following the steps below.
- Open the workspace.
- Click the Data Sources tab from the left bar.
- All data sources for this workspace will be listed. Click the SingleStore data source that you want to edit.
- The Data Sources page will open. Click the Edit Connection link.
- Modify the settings as needed and click Save. The connection details will be saved.
4. How long does it take for the data to be imported into Zoho Analytics?
After setup, you might have to wait sometime for the initial fetch to happen. This depends upon the amount of data to be imported into Zoho Analytics and also the response time of your SingleStore server. You will receive an email notification once the import is complete. Please note that, if you access the workspace before the initial fetch, it will not display any data.
5. Can I import data from Views created in SingleStore (apart from Tables) into Zoho Analytics?
Yes, you can import data from Tables as well as Views available in your SingleStore database into your Zoho Analytics workspace.
6. Will foreign keys defined between my tables in the SingleStore database be linked in Zoho Analytics as well?
When importing multiple tables, the foreign keys defined between the tables in SingleStore database will be linked in Zoho Analytics. The foreign keys will be created as Look-up columns in Zoho Analytics.
If you import data from one table at a time (choosing single table option) then the foreign keys will not be defined. However, you can manually link the tables in Zoho Analytics using the Look-up column feature. Click here to learn about the Look-up column feature.
7. Can I change the data type of the columns imported in Zoho Analytics?
Yes, you can change the data type of the columns imported into Zoho Analytics. However it is necessary that the data type of your column is compatible with the data type of the column in your SingleStore database for successful data synchronizations. It is always recommended that you change the data type in both your SingleStore database as well as your Zoho Analytics workspace.
8. I have connected to a database and imported a few tables into Zoho Analytics. Can I add more tables from the same source to the existing connection?
Yes, you can add tables from the same source to the existing connection. Follow the below steps:
- From your SingleStore workspace, navigate to Create > New Table / Import Data.
- Click the Cloud Databases option. The Connect to Cloud Database wizard will open.
- From the Connection name drop down menu, select the existing SingleStore database name.
- The rest of the steps are similar to importing data from cloud database.
9. Can I import data from SingleStore database into an existing table in Zoho Analytics?
Yes, you can import data into an existing table if you are importing from the same source database as the imported table.
- From the required table, click Import Data > Import Data into this Table.
- The Select Data to Import tab of the Import wizard will open.
- You can choose to import from the same table or a different table using the Select Table option, or import using the Custom Query.
- The rest of the steps are similar to importing from a single table.
10. I have synced data from SingleStore database into a table. Can I change the data source of this table?
Yes, you can change the data source of a table, into which the SingleStore database has been synced. To do this,
- Open the workspace.
- Click the Data Sources tab from the left bar.
- All the data sources for this workspace will be listed. Click the data source you want to edit.
- The Data Sources page will open. Click the Edit Connection link.
- In the Cloud Database - Edit Connection dialog that opens, modify the data source.
- Click Save to implement the changes made.
11. Can I import data from my SingleStore database into an existing Zoho Analytics workspace?
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
- All the data sources for this workspace will be listed. Click the SingleStore data source that you want to remove.
- In the Data Sources tab that opens, click the Settings icon inline to the data source name on the right.
- Click the Remove Data Source option from the drop-down menu.
Please note that the data source connection will be removed, but the tables and the data will be retained in the workspace. As the data source connected is removed, no further synchronization will happen.