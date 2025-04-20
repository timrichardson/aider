Import Data from Atlas Data Federation
Connect MongoDB Atlas Data Federation with Zoho Analytics, for an in-depth data analysis and uncover insights and trends.
- How do I import data from Atlas Data Federation?
- How do I schedule Import?
- How can I edit the setup?
- What happens when data import or data sync fails?
- Can I import data from Views created in Atlas Data Federation (apart from Tables) into Zoho Analytics?
- Can I blend data from other data sources into the Atlas Data Federation workspace?
- How do I remove the setup?
Data Import
1. How do I import data from Atlas Data Federation?
2. How do I schedule Import?
Zoho Analytics provides flexible sync frequencies like hourly, daily, weekly, and monthly to ensure that your data is always up-to-date for effective analysis.
Users can schedule import,
Additionally, it also provides the following options to customize the data import settings:
- Incremental Fetch (new records or modified records): In this method, only the newly added records are imported in each sync schedule. This is useful when the data source has transactional data that gets updated frequently. Refer to the Incremental Fetch article, to learn how to more.
- All records: In this method, all the records are imported in each sync schedule.
3. How can I edit the setup?
Users with administrator privileges can view and edit the connection settings by accessing the Data Sources tab.
The Data Sources tab includes the following details:
- Data Sync Status: Indicates whether the synchronization is currently active, completed, or if there are any errors/issues.
- Last Sync Time: Displays the timestamp of the most recent synchronization.
- Next Sync Time: Displays the timestamp of when the next sync is set to occur.
- Sync frequency: Displays how often the synchronization happens.
Modify Connection Details and Sync Settings
- Access the Data Sources tab on the side navigation bar.
- All the data sources in the workspace will be listed. Choose the data source you want to edit
- Click Edit Connection to modify the connection details and then click Save.
- Click Sync Settings to schedule import or modify the sync frequency.
Modify import synchronization settings
Zoho Analytics provides comprehensive details about the table settings like the Table Name, Source Table Name, What data is fetched, Time and Sync status.
To modify the Table level settings,
- Access the Data Sources tab
- Hover the mouse over the table where you want to modify the settings.
- Sync Now: Click the Sync Now icon to include the recent changes made in the data source.
- Edit synchronization settings: Click the Edit icon to change the import settings.
- Delete table: Click the Delete icon to remove the connection.
- Last Import Details: Click the Information icon to view the last import details of the table.
4. What happens when data import or data sync fails?
In the case of continuous import failure, an email will be sent to the registered address with the reason for failure and solution. The Data Sources tab will also list the sync failure details. Refer to Edit Connection section to resolve import and sync failures.
You can also choose to notify other administrators and custom users about the data sync failure.
5. Can I import data from Views created in Atlas Data Federation (apart from Tables) into Zoho Analytics?
Yes, you can import data from Tables as well as Views available in your Amazon Light sail MySQL database into your Zoho Analytics workspace.
6. Can I blend data from other data sources into the Atlas Data Federation workspace?
Yes, Zoho Analytics allows you to blend data from various sources.
Import data into an existing table
- Click Import > Import data into this table.
- Select the table you want to import.
- Choose how you want to import the records.
Import Data into an existing Workspace:
Refer to the setup presentation, for importing data into an existing workspace.
7. How do I remove the setup?
When you remove a data source, there will be no connection between the source application and Zoho Analytics. However, the tables and the data will be available in the workspace and no further synchronization will happen.
To remove the data source,
- Click Data Sources > Settings.
- Choose Remove Data Source from the drop-down list.