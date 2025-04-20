Managing Data Sources
Zoho Analytics allows you to easily view and manage all the data sources set up in a Workspace. This enables you to keep track and manage all the sources from which the data has been imported in a Workspace.
This section briefs you on managing different data sources from which data is imported into Zoho Analytics.
General
- What are the information available on the Data Sources page?
- How do I manage multiple data sources associated with my workspace?
- How do I remove the data source setup?
Feeds/Cloud Storage
- Can I import data from other data sources into the table in which I have imported the Feeds/Cloud Storage data?
- I have synced data from Feeds/Cloud Storage into a table. Can I change the data source of this table?
- Can I modify the schedule interval of the imported Feeds/Cloud Storage database?
- Can I synchronize data from the data source instantly?
- How do I check the Data Sync Status of the imported data?
- The Last Data Sync Status in Data Sources page shows Sync Failed. How do I resolve it?
Cloud Database/Local Database
- Can I import data from other data sources into the table in which I have imported the Cloud/Local database data?
- I have synced data from Cloud/Local database into a table. Can I change the data source of this table?
- Can I modify the schedule interval of the imported Cloud/Local Database?
- Can I synchronize the data from my Cloud/Local database instantly?
- How do I check the Data Sync Status of the imported data?
- The Last Data Sync Status in Data Sources page shows Sync Failed. How do I resolve it?
Connectors
- Can I edit the connector's Synchronization setting?
- Can I synchronize my connector data instantly?
- How do I re-authenticate my connector account in Zoho Analytics?
- I got this email which said 'Setup Process Failed'/'Synchronization Process Failed'. What should I do?
General
1. What are the information available on the Data Sources page?
The information available on the Data Sources page differs based on the data source that you connect to get data.
The Data Sources page usually contains the following information:
- Source Database Name
- Last Data Sync Status
- Last Data Sync Time
- Schedule Interval
- Next Schedule Time
- Synchronizations Done
- Table details such as Table Name, Source File Name, Last Fetched Time, Last Imported Status
You can perform the following actions from this page:
- Edit Connection/Re-Authenticate
- Sync Settings/Edit Setup
- Sync Now
- Remove Data Source
2. How do I manage multiple data sources associated with my workspace?
To manage multiple data sources,
- Open the workspace for which you wish to view the data source.
- Click the Data Sources button from the left menubar.
- The Data Sources page will open, listing all the sources from which data has been imported into this workspace.
Here, we are getting data from multiple data sources. As shown in the above snapshot, this page will display the
- Data Source name
- Table Name in Zoho Analytics
- Last Data Import/Sync Status
- Next Schedule Time,
- Sync/Refetch option
Clicking a Data Source name will open that particular Data Source details.
3. How do I remove the data source setup?
To remove the data source setup:
Method 1:
- Open the Data Sources page.
- Hover the mouse over the corresponding data source you wish to remove. The Settings icon will appear.
- Click the Settings icon.
- From the drop-down that appears, select Remove Data Source.
Method 2:
- Open the respective Data Sources page.
- Hover the mouse over the data source name in the left corner. The Settings icon will appear.
The rest of the steps are similar to Method 1.
Feeds/Cloud Storage
1. Can I import data from other data sources into the table in which I have imported the Feeds/Cloud Storage data?
Yes, you can import data into an existing table. Follow the given steps to import data into an existing table:
- Open the table into which you want to import data.
- Click Import Data > Import Data into this Table.
All the relevant data sources for the corresponding table will be displayed in the Import Your Data page. Select the required data source from here.
You will be navigated to the Exist Import page. The fields on this page vary based on the selected data source.
Provide the requested details and click Import.
Refer to the following video to know more about this.
2. I have synced data from Feeds/Cloud Storage into a table. Can I change the data source of this table?
Yes, you can change the data source of the table. The steps are same as the previous question.
3. Can I modify the schedule interval of the imported Feeds/Cloud Storage database?
Yes, you can modify the schedule interval of a Feeds/Cloud Storage database. To do this,
Method 1:
- Open the required Feeds/Cloud Storage Data Sources page.
- In the Data Sources page that opens, click the Edit Setup link.
- The Edit Setup dialog will open. Modify the settings as needed and click Save.
Method 2:
- Open the corresponding table.
- Click Import Data > Refetch/Schedule Import.
- In the Schedule Import Details dialog that opens, click Edit.
- The Schedule Import Settings page will open. Modify the settings as needed and click Save.
The synchronization setting will be modified and data will be synced from the next synchronization interval.
4. Can I synchronize data from the Feeds/Cloud Storage data source instantly?
Yes, you can synchronize data from the Feeds/Cloud Storage data source instantly. To do this:
Method 1:
- Open the required Data Sources page.
- Click the Refetch Now link.
Method 2:
- Open the corresponding table.
- Click Import Data > Refetch/Schedule Import.
- In the Schedule Import Details dialog that opens, click Refetch Data Now.
5. How do I check the Data Sync Status of the imported data?
To check the Data Sync Status of the imported data, follow the below steps:
Method 1:
- Open the required Data Sources page.
- Click the Click to view Last Import Details link inline with the Last Data Sync Status.
- The Import Details dialog appears listing the details of the particular table.
Method 2:
- Open the corresponding table.
- Click Import Data > Last Import Details.
- The Import Details dialog appears listing the details of the particular table.
6. The Last Data Sync Status in Data Sources page shows Sync Failed. How do I resolve it?
You can resolve your sync failure by understanding the reason behind the failure. To know the reason for the sync failure:
- Open the corresponding Data Sources page.
- Click the Click to view Last Import Details link inline with the Last Data Sync Status.
- The Import Details pop-up page will open listing the reason for your failure in the Details section. Take the necessary action based on the reason provided.
Alternatively, as mentioned in the previous question, you can also open the Import Details dialog from the corresponding table as well.
Cloud Database/Local Database
1. Can I import data from other data sources into the table in which I have imported the Cloud/Local Database data?
Yes, you can import data from other data sources into the table, into which the Cloud/Local database has been synced.
Follow the below steps to import if the source is available in the same database that is imported into the table.
- Open the corresponding table.
- Click Import Data > Import into this Table.
- The Select Data to Import tab of the Import wizard will open.
- You can choose to import from a different table using the Select Table option or import using the Custom Query.
Follow the below steps to import if the source is available in a different Cloud/Local database.
- Open the required Data Sources page.
- Click the Edit Connection link available at the top of the page.
- In the Edit Connection dialog that opens, modify the data source. For a local database, you can also change the Zoho Databridge that fetches the data.
- Modify the connection settings with the details of your new data source and click Save.
2. I have synced data from Feeds/Cloud Storage into a table. Can I change the data source of this table?
Yes, you can change the data source of the table. The steps are same as the previous question.
3. Can I modify the schedule interval of the imported Cloud/Local database?
Yes, you can modify the schedule interval of the imported database from the Sync Settings option if you are the administrator of the workspace. To do this,
- Open the required Data Sources page.
- Click the Sync Settings link available at the top of the page.
- The Sync Settings dialog will open. Modify the settings as needed and click Save.
The synchronization setting will be modified and data will be synced from the next synchronization interval.
4. Can I synchronize the data from my Cloud/Local database instantly?
Yes, you can synchronize data from the data source instantly when needed. To synchronize your data instantly:
Method 1:
- Open the required Data Sources page.
- Click the Sync Now link available inline with the Synchronizations Done option.
Method 2:
- From the corresponding table, click Import Data > Refetch/Schedule Import.
- In the Schedule Import Details dialog, click Sync This Table.
5. How do I check the Data Sync Status of the imported data
To check the Data Sync Status of the imported data, follow the below steps:
Method 1:
- Open the required Data Sources page.
- The tables fetched from the data source will be displayed.
- Click the information icon that appears on mouse over the table name.
- The Import Details dialog appears listing the details of the particular table. dialog appears listing the details of the particular table.
Method 2:
- Open the corresponding table.
- Click Import Data > Last Import Details.
- The Import Details dialog appears listing the details of the particular table.
6. The Last Data Sync Status in Data Sources page shows Sync Failed. How do I resolve it?
You can resolve your sync failure by understanding the reason behind the failure. To know the reason for the sync failure:
- Open the corresponding Data Sources page.
- Click the Click to view Last Import Details link inline with the Last Data Sync Status.
- The Import Details pop-up page will open listing the reason for your failure in the Details section. Take the necessary action based on the reason provided.
Connectors
1. Can I edit the connector's Synchronization setting?
Yes, you can edit the connector's synchronization setting if you are the administrator of the Advanced Analytics Connector. To do this,
- Open the corresponding Data Sources page and click the Edit Setup link.
- The Edit Setup dialog will open. Modify the settings as needed.
- Click Save.
The synchronization setting will be modified and data will be synced in the next synchronization interval.
2. Can I synchronize my connector data instantly?
Yes, you can synchronize your connector data instantly when needed.
To synchronize your data instantly:
- Open the corresponding Data Sources page.
- Click the Sync Now link inline with the Synchronizations Doneoption. The data will get instantly synchronized.
3. How do I re-authenticate my connector account in Zoho Analytics?
You can re-authenticate the setup by following the below steps.
- Open the corresponding Data Sources page.
- Click Re-Authenticate.
Your account will be successfully authenticated.
4. I got this email which said 'Setup Process Failed'/'Synchronization Process Failed'. What should I do?
The import/sync process of your connector data can sometimes fail, due to a variety of reasons. Hence, you may receive such emails occasionally. The Zoho Analytics team will look into it immediately and get back to you, after taking the required corrective action.
Case 1: You will receive the Setup Process Failed mail when there is a failure during the initial fetch. In this case, we request you to:
- Open the corresponding Data Sources page.
- In the Data Sources page that opens click the Retry Now link.
- If the issue persists please do write to support@zohoanalytics.com. We will look into it and get back to you immediately.
Case 2: You will receive the Synchronization Failed mail if there is any failure during the data synchronization process between Connector and Zoho Analytics, after the initial setup & import of data. This might be a momentary failure due to any internal issues. This import schedule will get suspended if there are five successive failures.