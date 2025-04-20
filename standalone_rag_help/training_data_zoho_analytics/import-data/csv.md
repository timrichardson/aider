Importing from Large CSV using Zoho Databridge
If you have data in large CSV files above 100MB, then you can easily import your data into Zoho Analytics using the Zoho Databridge. The Zoho Databridge bridges your local data source and Zoho Analytics server to fetch data from Large CSV files you have saved on your premises. With this, you can also automate the import process to synchronize the data into Zoho Analytics at a periodic interval.
- How do I install Zoho Databridge?
- How do I import data from the Large CSV files using Zoho Databridge?
- How long does it take for the data to be imported into Zoho Analytics?
- How can I edit the Import setup?
- How can I schedule import from the CSV file?
- Will I be notified on import failures?
- Import from CSV file stored in the cloud has failed. How to solve this?
- Can I import data from CSV files into an existing Zoho Analytics Workspace?
- I have synced data from CSV files into a table. Can I change the data source of this table?
- Can I import data from CSV files which are hosted in various networks/private cloud?
- Can I change the data-type of the columns imported in Zoho Analytics?
- How do I remove the import setup?
- I am unable to establish the connection between the local data source and Zoho Analytics server. How do I solve this?
1. How do I install Zoho Databridge?
2. How do I import data from the large CSV files using Zoho Databridge?
To import data from large CSV files, it is mandatory to install Zoho Databridge. Refer to the previous question to know how to Install.
3. How long does it take for the data to be imported into Zoho Analytics?
Import will take from a few minutes to hours depending on the volume of the data. Please note that, if you access the Workspace before the initial fetch, it will not display any data.
4. How can I edit the Import setup?
You can edit the import setup anytime needed by following the steps below.
- Open the Workspace.
- Click Data Source from the left bar.
- All data sources for this Workspace will be listed. Click the data source you want to edit.
- The Data Source page will open. Modify the settings as needed.
5. How can I schedule Import from CSV files?
Zoho Analytics allows you to schedule the import anytime. You can schedule the import for an existing table by following the steps below.
- Open the Workspace.
- Click Data Source from the left bar.
- All data sources for this Workspace will be listed. Click the data source of the CSV file which you want to schedule the import.
- The Data Source page will open. Click Sync Setting.
- The Local File - Synchronization Settings will open.
- Select the schedule interval you need in the Repeat drop-down. Supported intervals are:
- Not Scheduled
- Every 'N' Hours
- Every Day
- Weekly Once
- Monthly Once
- Select when the data need to be imported in Perform option.
- In the Notify me after every 'N' Import Failure (s) option, set the number of consecutive import failure after which you need to be notified.
- Click Save. The data for your CSV file will be imported into Zoho Analytics in the set interval.
You can also schedule the import while initial import using the Schedule Setting option in the Step 3 of Import Wizard.
6. Will I be notified on import failures?
Yes, you will be notified after consecutive import failure, in case it occurs. You can set the number of consecutive import failures after which you need to be notified in the Notify me after every 'N' Import Failure (s) option of the schedule import.
6. Import from CSV files stored in the cloud fails. How to solve this?
Import from private cloud may fail when the Databridge does not have the privilege to access the data. In case your private cloud security system only allows access from restricted IP Addresses, then it will blacklist the server/machine where Databridge is installed. Ensure that you have whitelisted the IP Address of the machine/ server where the Databridge is installed.
7. Can I import data from CSV files into an existing Zoho Analytics Workspace?
Yes, you can import your data from CSV files into an existing Workspace.
Follow the below steps to import data into an existing workspace:
- Open the Workspace into which you wish to import the data.
- Click Create > New Table / Import Data.
- The Import Your Data section will open. Click Local Databases option.
- The Import Wizard will open. Configuring the import will be similar to the steps followed in this presentation.
7. I have synced data from CSV files into a table. Can I change the data source of this table?
Yes, you can change the data source of a table, into which the CSV file has been synced.
Follow the below steps to change the file to be imported
- Open the Workspace.
- Click Import Data> Import into this Table.
- The Step 1 of Import wizard will open.
- Specify the Full File Path of the new file.
Note: You can only change the source which is accessible to the concerned Databridge.
8. Can I import data from the CSV file which are stored in various networks/private cloud?
Yes, you can import from CSV files that are stored in different networks by installing multiple Databridge. You need to install various Databridge for each network. To link all the Databridge installations to your account, use the same installation key available in the Download dialog.
Note:
- Single Databridge installation can import data from various data sources available in the same network.
- You can install only one Databridge per machine.
10. Can I change the datatype of the columns imported in Zoho Analytics?
Yes, you can change the datatype of the columns imported into Zoho Analytics. However, it is necessary that the datatype of your column is compatible with the datatype of the column in your local CSV file for successful data synchronizations. It is always recommended that you change the data type in both your local CSV file as well as your Zoho Analytics Workspace.
11. How do I remove the import setup?
You can remove the import setup by following the steps below.
- Open the Workspace.
- Click Data Sources from the left bar.
- All data sources for this Workspace will be listed. Click the data source you want to remove.
- In the Data Sources tab that opens click the Settings icon and then click the Remove Data Source.
Please do note that this only removes the connection. You can still continue accessing the Workspace in Zoho Analytics.
12. I am unable to establish the connection between the local datasource and Zoho Analytics server. How do I solve this?
This may happen due to various factors such as connectivity issues or privileges to access the protected data source. Refer to our Zoho Databridge Troubleshooting tip section to solve the specific issue you are facing.