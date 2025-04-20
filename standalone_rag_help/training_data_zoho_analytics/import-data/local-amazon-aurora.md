Importing from Amazon Aurora using Zoho Databridge
If you have data in a local /hosted Amazon Aurora database, then you can easily import your data into Zoho Analytics using the Zoho Databridge. The Zoho Databridge bridges your local Amazon Arora database and Zoho Analytics server to fetch data from your local /hosted Amazon Aurora database. With this, you can also automate the import process to synchronize the data from your local /hosted Amazon Arora database into Zoho Analytics at a periodic interval.
- How do I install Zoho Databridge?
- How do I import data from the Amazon Aurora database using Zoho Databridge?
- How long does it take for the data to be imported into Zoho Analytics?
- How can I edit the Import setup?
- How can I schedule import from Amazon Aurora database?
- Will I be notified on import failures?
- Import from Amazon Aurora database that is hosted in the cloud has failed. How to solve this?
- Can I import data from Amazon Aurora database into an existing Zoho Analytics Workspace?
- I have synced data from Amazon Aurora database into a table. Can I change the data source of this table?
- Can I import data from Amazon Aurora which are hosted in various networks/private cloud?
- Will foreign keys defined between my tables in Amazon Aurora database be linked in Zoho Analytics as well?
- Can I change the data-type of the columns imported in Zoho Analytics?
- How do I remove the import setup?
- I am unable to establish the connection between the local Amazon Aurora database and Zoho Analytics server. How do I solve this?
1. How do I install Zoho Databridge?
2. How do I import data from the Amazon Aurora database using Zoho Databridge?
To import data from local Amazon Aurora database, it is mandatory to install Zoho Databridge. Refer to the previous question to know how to Install.
3. How long does it take for the data to be imported into Zoho Analytics?
Import will take from a few minutes to hours depending on the volume of the data. Please note that, if you access the Workspace before the initial fetch, it will not display any data.
4. How can I edit the Import setup?
You can edit the import setup anytime needed by following the steps below.
- Open the Workspace.
- Click Data Source from the left bar.
- All data sources for this Workspace will be listed. Click the Amazon Aurora data source you want to edit.
- The Data Source page will open. Modify the settings as needed.
5. How can I schedule Import from Amazon Aurora database?
Zoho Analytics allows you to schedule the import anytime. You can schedule the import for an existing table by following the steps below.
- Open the Workspace.
- Click Data Source from the left bar.
- All data sources for this Workspace will be listed. Click the Amazon Aurora data source which you want to schedule the import.
- The Data Source page will open. Click Sync Setting.
- The Local Database - Synchronization Settings will open.
- Select the schedule interval you need in the Repeat drop-down. Supported intervals are:
- Not Scheduled
- Every 'N' Hours
- Every Day
- Weekly Once
- Monthly Once
- Select when the data need to be imported in Perform option.
- In the Notify me after every 'N' Import Failure (s) option, set the number of consecutive import failure after which you need to be notified.
- Click Save. The data for your Amazon Aurora database will be imported into Zoho Analytics in the set interval.
You can also schedule the import while initial import using the Schedule Setting option in the Step 4 of Import Wizard.
6. Will I be notified on import failures?
Yes, you will be notified after consecutive import failure, in case it occurs. You can set the number of consecutive import failures after which you need to be notified in the Notify me after every 'N' Import Failure (s) option of the schedule import.
6. Import from Amazon Aurora database that is hosted in the cloud fails. How to solve this?
Import from the cloud database may fail when the Databridge does not have the privilege to access the data. In case your cloud database security system only allows access from restricted IP Addresses, then it will blacklist the server/machine where Databridge is installed. Ensure that you have whitelisted the IP Address of the machine/ server where the Databridge is installed.
7. Can I import data from Amazon Aurora database into an existing Zoho Analytics Workspace?
Yes, you can import your data from Amazon Aurora into an existing Workspace.
Follow the below steps to import data into an existing workspace:
- Open the Workspace into which you wish to import the data.
- Click Create > New Table / Import Data.
- The Import Your Data section will open. Click Local Databases option.
- The Import Wizard will open. Configuring the import will be similar to the steps followed in this presentation.
7. I have synced data from database into a table. Can I change the data source of this table?
Yes, you can change the data source of a table, into which the Amazon Aurora database has been synced.
Follow the below steps to import if the source is available in the same Amazon Aurora database that is imported into the table.
- Open the Workspace.
- Click Import Data> Import into this Table.
- The Select Data to Import tab of the Import wizard will open.
- You can choose to import from a different table using the Select Table option or import using the Custom Query.
Follow the below steps to import if the source is available in a different local database.
- Open the Workspace.
- Click Data Source from the left bar.
- All data sources for this Workspace will be listed. Click the data source you want to edit.
- The Data Source page will open. Click Edit Connection.
- In the Local Database - Edit Connection dialog that open, modify the data source. You can also change the Databridge that fetches the data.
8. Can I import data from the Amazon Aurora which are hosted in various networks/private cloud?
Yes, you can import from various databases that you have hosted in different networks by installing multiple Databridge. You need to install various Databridge for each network. To link all the Databridge installations to your account, use the same installation key available in the Download dialog.
Note:
- Single Databridge installation can import data from various data sources available in the same network.
- You can install only one Databridge per machine.
9. Will foreign keys defined between my tables in Amazon Aurora database be linked in Zoho Analytics as well?
No, the tables will not be directly linked in Zoho Analytics. You need to link the required tables in Zoho Analytics using the Look-up feature. Click here to learn about look-up.
10. Can I change the datatype of the columns imported in Zoho Analytics?
Yes, you can change the datatype of the columns imported into Zoho Analytics. However, it is necessary that the datatype of your column is compatible with the datatype of the column in your Amazon Aurora database for successful data synchronizations. It is always recommended that you change the data type in both your Amazon Aurora database as well as your Zoho Analytics Workspace.
11. How do I remove the import setup?
You can remove the import setup by following the steps below.
- Open the Workspace.
- Click Data Sources from the left bar.
- All data sources for this Workspace will be listed. Click the data source you want to remove.
- In the Data Sources tab that opens click the Settings icon and then click the Remove Data Source.
Please do note that this only removes the connection. You can still continue accessing the Workspace in Zoho Analytics.
12. I am unable to establish the connection between the local Amazon Aurora database and Zoho Analytics server. How do I solve this?
This may happen due to various factors such as connectivity issues or privileges to access the protected data source. Refer to our Zoho Databridge Troubleshooting tip section to solve the specific issue you are facing.