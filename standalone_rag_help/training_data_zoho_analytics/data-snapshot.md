Data Snapshots
Data Snapshots allows you to capture and maintain historical data from a report. It periodically snapshots the data from a chosen report, and stores them in a table for historical report creation & analysis.
Data Snapshots - Basics
- What is a Data Snapshot and what are its uses?
- What plans support Data Snapshots?
- Who can set up Data Snapshots?
- On what reports can I create a Data Snapshot?
- How can I set up/create a Data Snapshot?
- I have created a Data Snapshot over a report. I'm unable to edit it. Why?
- Can I edit or delete data from a snapshot table?
- Can I create multiple snapshots over a report?
- At what frequency can I snapshot a report?
- For what time span can I retain the snapshot data?
Managing Data Snapshots
- How do I manage all the Data Snapshots in my Workspace?
- How can I edit a Data Snapshot?
- How can I view the Data Snapshot settings?
- Can I see the Data Snapshot History?
- Can I execute a Data Snapshot schedule instantly?
- Can I remove the existing record from the Data Snapshot table and reinitiate the snapshot again?
- Can I pause a Data Snapshot schedule?
- Can I disconnect a Data Snapshot from the associated report?
- How can I delete a Data Snapshot Table?
- Can I restore the Data Snapshot?
Data Snapshots - Basics
1. What is a Data Snapshot and what are its uses?
Data Snapshot allows you to capture and maintain historical data from a report. It periodically snapshots the data from a chosen report, and stores them in a table for historical report creation & analysis. Let's say you have a report for Leads by Source and Status. With Data Snapshot, you can track the change in leads status across the time span like every month, week, day or hour.
2. What plans support Data Snapshots?
Data Snapshot is available for all the Zoho Analytics users with Standard plan and above. For more details, refer to our Pricing Page.
3. Who can set up a Data Snapshot?
The Account Administrator and the Workspace Administrators of a Workspace in Zoho Analytics can set up data snapshots.
4. On what reports can I create a Data Snapshot?
You can create data snapshots on the following reports.
Note:
- You cannot snapshot a Pivot View with Column grouping.
- In case you have set a default value for the user filter in the report, then you can snapshot only the report with the default value.
5. How can I set up/create a Data Snapshot?
The following video illustrates how to set up Data Snapshot.
The following presentation gives step by step explanation on how to set up Data Snapshot.
6. I have created a Data Snapshot over a report. I'm unable to edit the report. Why?
Once you create a Snapshot, editing the report will be restricted. You cannot remove a column or change the summary function applied over it. However, you can add more columns or rearrange the columns. Ensure all necessary modifications to the view are done before you set up a snapshot.
7. Can I edit or delete data from a Data Snapshot table?
No, you cannot edit or delete any data from a snapshot table. This is because the data in the snapshot table is the actual history of the reports columns, and it shouldn't be tampered with.
8. Can I create multiple Data Snapshots over a report?
Yes, you can create multiple snapshots over a report.
9. At what frequency can I snapshot a report?
You can snapshot a report in the following frequencies:
- Hourly
- Daily
- Weekly
- Monthly
You can also choose not to schedule the snapshot and run the snapshot manually.
10. For what time span can I retain the snapshot data?
You can retain the snapshot data for one of the following time span:
- Last 7 Days
- Last 30 Days
- Last 3 Months
- Last 6 Months
- Last 12 Months
- All Snapshots
Data for the specified time span will be retained in the table and older data will be removed.
Managing Data Snapshots
1. How do I manage all the Data Snapshots in my Workspace?
Data Snapshots is a data source for the corresponding table. So it will be listed as one of the data sources of the workspace. You can manage all Snapshots created in a Workspace from the Data Sources page.
Follow the steps below to view and manage all the Data Snapshots in your Workspace.
- Open the Workspace.
- Click Data Sources. The Data Sources page will open, and list all the data sources for the Workspace.
- Click Snapshots. All Snapshots in the Workspace will be listed.
- Mouse over the snapshot and a list of contextual options will appear. You can perform the below operations.
- Run - Click this to instantly run the Data Snapshot to import the report's columns.
- View History - Click this to view the history of Data Snapshot.
- View Snapshot Setting - Click this to view the Data Snapshot settings.
- Edit - Click this to edit the Data Snapshot settings.
- Reinitialize - Click this to remove all existing records from the snapshot table and reinitialize the import.
- Disconnect - Click this to disconnect the snapshot from the associated report.
- Delete - Click this to delete the snapshot and the corresponding data table.
2. How can I edit a Data Snapshot?
You can edit the snapshot setting anytime by following the below steps.
- Open the workspace in which you have set up a snapshot.
- Click Data Sources. The Data Sources page will open listing all the data sources for the workspace.
- Click Snapshots. All Snapshots in the Workspace will be listed.
- Mouse over the snapshot you want to edit. A contextual menu will appear.
- Click the More icon and then select Edit.
- The Edit Snapshot dialog will open. You can modify the following:
- Snapshot Table Name
- Interval to snapshot
- Time span to retain the data
3. How can I view the Data Snapshot settings?
Follow the below steps to view the snapshot settings.
- Open the corresponding workspace.
- Click Data Sources. The Data Sources page will open, listing all the data sources for the workspace.
- Click Snapshots. All Snapshots in the Workspace will be listed.
- Mouse over the snapshot for which you want to view the settings. A contextual menu will appear.
- Click the Info icon. The snapshot details will be displayed.
4. Can I see the Data Snapshot History?
Yes, you can view a detailed history of when the snapshots were taken. Follow the below steps to view the snapshot history:
- Open the corresponding workspace.
- Click Data Sources. The Data Sources page will open listing all the data sources for the workspace.
- Click Snapshots. All Snapshots in the workspace will be listed.
- Mouse over the snapshot for which you want to view history. A contextual menu will appear.
- Click the History icon. A calendar view will open, highlighting the days that the report's data were recorded. Snapshot history will be maintained for 45 days.
- Clicking the snapshot date will display the number of times the snapshot was run, the time of data fetch, and the number of rows & columns imported.
5. Can I execute a Data Snapshot schedule instantly?
Yes, you can run a snapshot instantly. Follow the below steps to do so.
- Open the corresponding workspace.
- Click Data Sources. The Data Sources page will open listing all the data sources for the workspace.
- Click Snapshots. All Snapshots in the workspace will be listed.
- Mouse over the Snapshot to run instantly. A contextual menu will appear.
- Click the Run icon. The Snapshot will run instantly and import the data from the report.
6. Can I remove the existing records from the snapshot table and reinitiate the snapshot again?
Yes, you can remove the existing records from the snapshot table and initiate the snapshot again. Follow the below steps to do so.
- Open the corresponding workspace.
- Click Data Sources. The Data Sources page will open listing all the data sources for the workspace.
- Click Snapshots. All Snapshots in the workspace will be listed.
- Mouse over the snapshot to restart. A contextual menu will appear.
- Click More icon and then select Reinitialize. The existing snapshot records in the table will be deleted and new snapshot record will be added in the scheduled interval.
7. Can I pause a Data Snapshot schedule?
Yes, you can pause the snapshot schedule and stop importing further data until you change the status. Follow the below steps to do so.
- Open the corresponding workspace.
- Click Data Sources. The Data Sources page will open listing all the data sources for the workspace.
- Click Snapshots. All Snapshots in the workspace will be listed.
- Mouse over the snapshot to pause. A contextual menu will appear.
- Click the Status toggle button to set this as inactive.
The snapshot will be paused and will not import further data until the status is changed to Active. You can set the status to Active anytime again.
8. Can I disconnect a snapshot from the associated report?
Yes, you can disconnect the snapshot from the associated report.
Follow the below steps to disconnect the snapshot.
- Open the corresponding workspace.
- Click Data Sources. The Data Sources page will open listing all the data sources for the workspace.
- Click Snapshots. All Snapshots in the workspace will be listed.
- Mouse over the snapshot. A contextual menu will appear.
- Click More icon and then select Disconnect. The Data Snapshot will be disconnected from the corresponding report. However, you will still be able to access this table with existing data.
Note: Once you disconnect, the Data Snapshot will be removed from the table forever. You will not be able to set up the data snapshot connection into this table.
9. How can I delete a Data Snapshot Table?
You cannot directly delete the snapshot table. To delete the snapshot table, you need to delete the Data Snapshot.
Follow the below steps to delete the snapshot.
- Open the corresponding workspace.
- Click Data Sources. The Data Sources page will open listing all the data sources for the workspace.
- Click Snapshots. All Snapshots in the Workspace will be listed.
- Click More icon and then select Delete. The Data Snapshot along with the dependent views will be deleted.
10. Can I restore the Data Snapshot table that is deleted?
Yes, you can restore the Data Snapshot, provided the corresponding report is still available. To restore the snapshot table, open the Trash page of the workspace and click Restore icon.
Note:
- In case the parent report is deleted or the involved columns are removed from the report, then you will not be able to restore the Data Snapshot.
- Data Snapshot in the Trash will be retained only for 45 days. You will not be able to restore it after that.