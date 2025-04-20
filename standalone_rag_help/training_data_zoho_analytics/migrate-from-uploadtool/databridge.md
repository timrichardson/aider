Migration from Upload Tool to Zoho Databridge
Zoho Databridge is an enhanced utility by Zoho Analytics that enables you to import data from on-premise databases and local files into Zoho Analytics. If you are currently using the Upload Tool, we strongly recommend you to try the Zoho Databridge. This section provides you a guide on how to migrate from Upload Tool to Zoho Databridge.
- What is Zoho Databridge?
- Why should I migrate from Upload Tool to Zoho Databridge?
- What are the pre-checks to be done before migrating to Zoho Databridge?
- How to migrate from Upload Tool to Zoho Databridge?
- How to verify whether the settings from the Upload Tool are successfully migrated to Zoho Databridge?
- How do I manage all my databridges?
FAQ and Troubleshooting Tips
- Is it necessary to install the Zoho Databridge in the same network as that of the Upload Tool?
- I am having the Upload Tool in Windows OS. Can I migrate it to Zoho Databridge in Mac/Linux OS?
- Do I need to retain the Upload Tool after migrating?
- I get an error message "{Database Type} not supported in Databridge" while migrating. How to overcome this?
- I get an error message "No such file or directory" while migrating. How to overcome this?
- I get an error message "Connection already exists with another Databridge, Please check Workspace -> Data Source page " while migrating. How to overcome this?
- I get an error message "Workspace "{Name}" is not found in the given account, Please check credentials and try again" while migrating. How to overcome this?
- I get an error message "Table "{Name}" is not present in Workspace {Name}, Please check credentials and try again" while migrating. How to overcome this?
1. What is Zoho Databridge?
Zoho Databridge is a lightweight independent utility that bridges your on-premise data sources and Zoho Analytics service. With Databridge you can easily automate the import process from your local databases and privately hosted databases into Zoho Analytics right from the Zoho Analytics user interface. You can also easily manage and monitor the import process.
For more information on Zoho Databridge, go through the Zoho Databridge documentation.
2. Why should I migrate from Upload Tool to Zoho Databridge?
In Zoho Databridge, you can upload, configure, and manage the data import from the Zoho Analytics interface. Whereas in Upload Tool it is done in the terminal/command line interface.
With Zoho Databridge, you can also monitor all your upload processes right from your Zoho Analytics user interface and also get notified on failures through emails.
To sum it up, managing the data import using Zoho Databridge is a very straightforward and user-friendly process with a minimal requirement of technical expertise.
3. What are the pre-checks to be done before migrating to Zoho Databridge?
- You must have the Zoho Databridge downloaded and installed in the same network as that of Upload Tool. Refer to the Zoho Databridge documentation to know how to install Zoho Databridge.
- You must ensure the data source of your Upload Tool is one of the following:
- MySQL
- Oracle
- SQL Server
- Sybase
- PostgreSQL
- Maria DB
- Amazon Aurora MySQL
4. How to migrate from Upload Tool to Zoho Databridge?
You can easily migrate from Upload Tool to Zoho Databridge executing the migration tool as described below.
Before migrating, ensure that the corresponding data source of the Upload Tool is supported by Zoho Databridge and the Zoho Databridge is installed in the same network as that of Upload Tool. Refer to the list of data sources that can be migrated section.
Follow the below steps to migrate from Upload Tool to Zoho Databridge:
- Download the Migration Tool given below appropriate to your OS:
| Download Migration Tool | ||
| Windows Download | Linux Download | Mac Download |
- Unzip the MigrateToDatabridge zip file and place the files available in the bin and lib folder of the MigrateToDatabridge folder into the bin and the lib folders of your existing Upload Tool respectively.
- Invoke the below script from the Upload Tool/bin folder by executing it in the command line/terminal:
- The script will do all the pre-checks for the migration. Incase, you have multiple databridges, you will be prompted to select a Zoho Databridge after executing the Migration Tool. You can choose a Zoho Databridge by entering the index of the Zoho Databridge displayed in the terminal.
- Specify a schedule interval at which Databridge should execute the data import process from your local/hosted databases to Zoho Analytics.
You can choose a schedule interval from the listed options by entering a number from 1 to 4, which is described below:
- 1 - DO NOT Schedule
- 2 - Schedule DAILY at 12 AM in your timezone
- 3 - Schedule WEEKLY on every Sunday at 12 AM in your timezone
- 4 - Schedule MONTHLY on the 1st day of every month at 12 AM in your timezone
- The Upload Tool will be migrated to the Zoho Databridge and a success message will be displayed.
The synchronization will begin from the next sync schedule.
- Upload Tool used to sync data from Large CSV files cannot be migrated to Zoho Databridge.
- If you have multiple instances of Upload Tool, you can migrate them one-by-one to Zoho Databridge following the steps described above.
- On successful migration, refer to the below question, please stop the execution of the Upload Tool.
5. How to verify whether the settings from the Upload Tool are successfully migrated to Zoho Databridge?
On completion of all the steps mentioned in the above question, the Upload Tool configurations will be migrated, and a success message will be displayed. Your data will get synchronized from the next sync schedule.
You can verify whether your data is properly imported by following the below steps:
- Open the corresponding Workspace in Zoho Analytics.
- Click the Data Sources tab.
- From the list of available data sources, select the Data Source for which you want to make the modifications.
The Data Sources page that opens will list the following details:
- Sync status summary details such as:
- Databridge Name: Name of the Zoho Databridge
- Databridge Status: Status of the Zoho Databridge
- Source Database Name: Name of the database imported
- Last Data Sync Status: Status of the last synchronization, with the possible status being Success, Failure, In Progress, and Partial Success
- Last Data Sync Time: Time of the last synchronization
- Schedule information such as:
- Schedule: Interval in which the import is scheduled
- Next Schedule Time: Time of the next schedule
- Synchronizations Done: Number of instant syncs done in the day
- Table details: Details of the individual tables will be displayed, which includes, the Table Name, Source Table Name, Last Fetched Time, and Sync Status.
From the above details you can verify that the Zoho Databridge is successfully running after migration.
- You can instantly sync the data from here by clicking the Sync Now link if required.
- You can always Edit Connection details and Sync Settings as and when required. Refer to Import from Database using Zoho Databridge document to know more.
6. How do I manage all my databridges?
You can monitor and manage all installation right from Zoho Analytics user interface using the Manage Databridge tab in the Account Setup page. To know more about the same, refer Zoho Databridge document.
FAQ and Troubleshooting Tips
1. Is it necessary to install the Zoho Databridge in the same network as that of the Upload Tool?
Yes, it is manditory to install Zoho Databridge in the same network as that of the Upload Tool.
2. I am having the Upload Tool setup in Windows OS. Can I migrate it to Zoho Databridge setup in Mac/Linux OS?
Yes, you can migrate the Upload Tool setup in one OS (say Windows) to the Zoho Databridge setup in another OS (say Mac/Linux OS), as along as they are setup in the same network. There are no constraints regarding the same.
3. Do I need to retain the Upload Tool after migrating?
No, you can delete the Upload Tool after the migration is successfully complete.
4. I get an error message "{Database Type} not supported in Databridge" while migrating. How to overcome this?
This error occurs when the data source of the Upload Tool you are migrating is not supported by Zoho Databridge. Ensure that your data source is in the supported by Zoho Databridge list, before migrating.
5. I get an error message "No such file or directory" while migrating. How to overcome this?
This error occurs when the Migration Tool files are not placed in appropriate location. Ensure to place the files available in the bin and lib folder of the MigrateToDatabridge folder into the bin and the lib folders of your existing Upload Tool respectively.
6. I get an error message "Connection already exists with another Databridge. Please check Workspace -> Data Source page " while migrating. How to overcome this?
This error occurs when the Upload Tool is already migrated into another Zoho Databridge. You can verify the Zoho Databridge that you have migrated to from the corresponding Workspace by following the below steps.
- Log in to your Zoho Analytics.
- Open the corresponding Workspace.
- Click the Data Sources tab.
- From the list of available data sources, select the Data Source for which you want to make the modifications.
- The details of the selected Data Source appear. Refer successful migration section for more information regarding the same.
7. I get an error message "Workspace "{Name}" is not found in the given account, Please check credentials and try again" while migrating. How to overcome this?
This error occurs when the Workspace mentioned in the Upload Tool is not found in Zoho Analytics. Always ensure that there is no mismatch between the Workspace name mentioned in the Upload Tool and the one available in the Zoho Analytics.
8. I get an error message "Table "{Name}" is not present in Workspace {Name}, Please check credentials and try again" while migrating. How to overcome this?
This error occurs when the Table mentioned in the Upload Tool is not found in Zoho Analytics. Always ensure that there is no mismatch between the Table name mentioned in the Upload Tool and the one available in the Zoho Analytics.