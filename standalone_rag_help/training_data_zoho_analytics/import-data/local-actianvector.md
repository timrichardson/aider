Importing from Actian Vector using Zoho Databridge
If you have data in a local /hosted Actian Vector database, then you can easily import your data into Zoho Analytics using the Zoho Databridge. The Zoho Databridge bridges your local Actian Vector database and Zoho Analytics server to fetch data from your local /hosted Actian Vector database. With this, you can also automate the import process to synchronize the data from your local /hosted Actian Vector database into Zoho Analytics at a periodic interval.
- How do I install Zoho Databridge?
- How do I import data from the Actian Vector database using Zoho Databridge?
- How long does it take for the data to be imported into Zoho Analytics?
- How can I edit the Import setup?
- How can I schedule import from Actian Vector database?
- Will I be notified on import failures?
- Import from Actian Vector database that is hosted in the cloud has failed. How to solve this?
- Can I import data from Actian Vector database into an existing Zoho Analytics Workspace?
- I have synced data from Actian Vector database into a table. Can I change the data source of this table?
- Can I import data from Actian Vector which are hosted in various networks/private cloud?
- Will foreign keys defined between my tables in Actian Vector database be linked in Zoho Analytics as well?
- Can I change the data-type of the columns imported in Zoho Analytics?
- How do I remove the import setup?
- I am unable to establish the connection between the local Actian Vector database and Zoho Analytics server. How do I solve this?
1. How do I install Zoho Databridge?
2. How do I import data from the Actian Vector database using Zoho Databridge?
To import data from local Actian Vector database, it is mandatory to install Zoho Databridge. Refer to the previous question to know how to Install.
3. How long does it take for the data to be imported into Zoho Analytics?
Import will take from a few minutes to hours depending on the volume of the data. Please note that, if you access the Workspace before the initial fetch, it will not display any data.
4. How can I edit the Import setup?
You can edit the import setup anytime needed by following the steps below.
- Open the Workspace.
- Click Data Source from the left bar.
- All data sources for this Workspace will be listed. Click the Actian Vector data source you want to edit.
- The Data Source page will open.
- Click the Edit Connection link and modify the settings as needed.
5. How can I schedule Import from Actian Vector database?
Zoho Analytics allows you to schedule the import anytime. You can schedule the import for an existing table by following the steps below.
- Open the Workspace.
- Click Data Source from the left bar.
- All data sources for this Workspace will be listed. Click the Actian Vector data source for which you want to schedule the import.
- The Data Source page will open. Click Sync Settings.
- The Local Database - Synchronization Settings will open.
- Select the schedule interval you need in the Repeat drop-down. Supported intervals are:
- Not Scheduled
- Every 'N' Hours
- Every Day
- Weekly Once
- Monthly Once
- Select when the data needs to be imported in Perform every option.
- In the Notify me after every 'N' Sync Failure(s) option, set the number of consecutive import failure after which you need to be notified.
- Click Save. The data for your Actian Vector database will be imported into Zoho Analytics in the set interval.
You can also schedule the import while initial import using the Schedule Settings option in the Step 4 of Import Wizard.
6. Will I be notified on import failures?
Yes, you will be notified after consecutive import failure, in case it occurs. You can set the number of consecutive import failures after which you need to be notified in the Notify me after every 'N' Sync Failure(s) option of the schedule import.
7. Import from Actian Vector database that is hosted in the cloud fails. How to solve this?
Import from the database may fail when the Databridge does not have the privilege to access the data. In case your database security system only allows access from restricted IP Addresses, then it will blacklist the server/machine where Databridge is installed. Ensure that you have whitelisted the IP Address of the machine/ server where the Databridge is installed.
8. Can I import data from Actian Vector database into an existing Zoho Analytics Workspace?
Yes, you can import your data from Actian Vector into an existing Workspace.
Follow the below steps to import data into an existing workspace:
- Open the Workspace into which you wish to import the data.
- Click Create > New Table / Import Data.
- The Import Your Data section will open. Click Local Databases option.
- The Import Wizard will open. Configuring the import will be similar to the steps followed in this presentation.
9. I have synced data from database into a table. Can I change the data source of this table?
Yes, you can change the data source of a table, into which the Actian Vector database has been synced.
Follow the below steps to import if the source is available in the same Actian Vector database that is imported into the table.
- Open the Workspace.
- Click Import Data > Import into this Table.
- The Select Data to Import tab of Import wizard will open.
- You can choose to import from a different table using the Select Table option or import using the Custom Query.
If the source is available in a different local database, follow the below steps:
- Open the Workspace.
- Click Data Source from the left bar.
- All data sources for this Workspace will be listed. Click the data source you want to edit.
- The Data Source page will open. Click Edit Connection link.
- In the Local Database - Edit Connection dialog that opens, modify the data source. You can also change the Databridge that fetches the data.
10. Can I import data from the Actian Vector which are hosted in various networks/private cloud?
Yes, you can import from various databases that are hosted in different networks by installing multiple Databridges. You need to install various Databridges for each network. To link all the Databridge installations to your account, use the same installation key available in the Download dialog.
- Single Databridge installation can import data from various data sources available in the same network.
- You can install only one Databridge per machine.
11. Will foreign keys defined between my tables in Actian Vector database be linked in Zoho Analytics as well?
No, the tables will not be directly linked in Zoho Analytics. You need to link the required tables in Zoho Analytics using the Look-up column feature. Click here to learn about look-up.
12. Can I change the datatype of the columns imported in Zoho Analytics?
Yes, you can change the datatype of the columns imported into Zoho Analytics. However, it is necessary that the datatype of your column is compatible with the data type of the column in your Actian Vector database for successful data synchronizations. It is always recommended that you change the data type in both your Actian Vector database as well as your Zoho Analytics Workspace.
13. How do I remove the import setup?
You can remove the import setup by following the steps below.
- Open the Workspace.
- Click Data Sources from the left bar.
- All data sources for this Workspace will be listed. Click the data source you want to remove.
- In the Data Sources tab that opens, click the Settings icon.
- Click the Remove Data Source.
Please do note that this only removes the connection. You can still continue accessing the Workspace in Zoho Analytics.
14. I am unable to establish the connection between the local Actian Vector database and Zoho Analytics server. How do I solve this?
This may happen due to various factors such as connectivity issues or privileges to access the protected data source. Refer to our Zoho Databridge Troubleshooting tip section to solve the specific issue you are facing.