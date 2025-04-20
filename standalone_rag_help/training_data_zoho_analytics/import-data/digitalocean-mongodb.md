Import Data from DigitalOcean MongoDB
The data stored in DigitalOcean MongoDB Cloud Database can be analyzed using Zoho Analytics. You can either import your data into Zoho Analytics or connect directly with the DigitalOcean MongoDB server. You can set up periodic schedules to fetch the latest data automatically from your DigitalOcean MongoDB database. The reports loading time will load faster as the data is stored in Zoho Analytics.
Data Import
- How do I import data from the DigitalOcean MongoDB database?
- How can I edit the setup?
- How long does it take for the data to be imported into Zoho Analytics?
- Can I import data from Views created in DigitalOcean MongoDB (apart from Tables) into Zoho Analytics?
- Will foreign keys defined between my tables in the DigitalOcean MongoDB database be linked in Zoho Analytics as well?
- Can I change the data type of the columns imported in Zoho Analytics?
- I have connected to a database and imported a few tables into Zoho Analytics. Can I add more tables from the same source to the existing connection?
- Can I import data from DigitalOcean MongoDB database into an existing table in Zoho Analytics?
- I have synced data from DigitalOcean MongoDB database into a table. Can I change the data source of this table?
- I have synced data from a database into multiple tables in this workspace? Can I remove the data source for a single table?
- Can I import data from my DigitalOcean MongoDB database into an existing Zoho Analytics workspace?
- Can I synchronize the data from my Cloud Database instantly?
- The Last Data Sync Status in Data sources page shows Sync Failed. How do I resolve it?
- How do I remove the Setup?
Data Import
1. How do I import data from the DigitalOcean MongoDB database?
2. How can I edit the setup?
3. How long does it take for the data to be imported into Zoho Analytics?
After setting up, you might have to wait for sometime for the initial fetch to finish. This depends on the amount of data to be imported into Zoho Analytics and also the response time of your DigitalOcean MongoDB server. You will receive an email notification once the import is complete. Please note that if you access the workspace before the initial fetch, it will not display any data.
4. Can I import data from Views created in DigitalOcean MongoDB (apart from Tables) into Zoho Analytics?
Yes, you can import data from Tables as well as Views available in your DigitalOcean MongoDB database into your Zoho Analytics workspace.
5. Will foreign keys defined between my tables in the DigitalOcean MongoDB database be linked in Zoho Analytics as well?
When importing multiple tables, the foreign keys defined between the tables in DigitalOcean MongoDB database will be linked in Zoho Analytics. The foreign keys will be created as Lookup columns in Zoho Analytics.
If you import data from one table at a time (choosing the single table option) then the foreign keys will not be defined. However, you can manually link the tables in Zoho Analytics using the Lookup column feature. Click here to learn about the Lookup column feature.
6. Can I change the data type of the columns imported in Zoho Analytics?
Yes, you can change the data type of the columns imported into Zoho Analytics. However, it is necessary that the data type of your column is compatible with the data type of the column in your DigitalOcean MongoDB database for successful data synchronizations. It is always recommended that you change the data type in both your DigitalOcean MongoDB database as well as your Zoho Analytics workspace.
7. I have connected to a database and imported a few tables into Zoho Analytics. Can I add more tables from the same source to the existing connection?
Yes, you can add tables from the same source to the existing connection. Follow the below steps:
- From your DigitalOcean MongoDB workspace, navigate to Create > New Table / Import Data.
- Click the Cloud Databases option. The Connect to Cloud Database wizard will open.
- From the Connection Name drop-down menu, select the existing DigitalOcean MongoDB database name.
- The rest of the steps are similar to importing data from cloud database.
8. Can I import data from DigitalOcean MongoDB database into an existing table in Zoho Analytics?
Yes, you can import data into an existing table if you are importing from the same source database as the imported table.
- From the required table, click Import Data > Import Data into this Table.
- The Select Data to Import tab of the Import wizard will open.
- You can choose to import from the same table or a different table using the Select Collection option.
- The rest of the steps are similar to importing from a single table.
9. I have synced data from DigitalOcean MongoDB database into a table. Can I change the data source of this table?
Yes, you can change the data source of the [Zoho Analytics] table into which the DigitalOcean MongoDB database has been synced. To do this,
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
11. Can I import data from my DigitalOcean MongoDB database into an existing Zoho Analytics workspace?
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
- All the data sources for this workspace will be listed. Click the DigitalOcean MongoDB data source that you want to remove.
- In the Data Sources tab that opens, click the Settings icon inline to the data source name on the right.
- Click the Remove Data Source option from the drop-down menu.
Please note that the data source connection will be removed, but the tables and the data will be retained in the workspace. As the data source connected is removed, no further synchronization will happen.