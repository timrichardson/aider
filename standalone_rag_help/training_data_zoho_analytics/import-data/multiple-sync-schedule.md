Maintain Data freshness with multiple sync intervals
Access to the most recent data is crucial to staying ahead in your analytical efforts. Outdated data can lead to incorrect analysis and decision-making. This article covers the data sync intervals available and the methods to configure.
On this Page
- Data Sync Intervals in Zoho Analytics
- Multiple Sync Intervals
- Configuring Multiple Sync Intervals
- Manage Sync Schedules
Data Sync Intervals in Zoho Analytics
Zoho Analytics offers flexible sync schedules to ensure that the data is always up-to-date for effective analysis. The following are the data frequency supported in Zoho Analytics.
- Every 'N' hour (Enterprise plan)
- Everyday (Standard plan and above)
- Weekly Once (Standard plan and above)
- Monthly Once (Standard plan and above)
Multiple Sync Intervals
While analyzing data, there might arise a need to sync different tables at different intervals. Zoho Analytics allows you to configure multiple sync schedules within a connection, enabling you to set different tables to sync at various intervals. For example, some tables can be set to sync every hour, while others can be synced daily or weekly, based on your needs.
Configuring Multiple Sync Intervals
Multiple Sync Intervals can be configured in the following two ways in Zoho Analytics:
- From the Data sources tab
- Creating a new sync interval when all the tables in a connection have the same data sync interval.
- Creating a new sync interval when there are more than one sync interval configured for a connection.
While importing data as a new table in an existing connection
- While importing data as a new table in an existing connection.
From the Data Sources Tab
Case 1: When all the tables in a connection have the same data sync interval
To configure multiple sync intervals,
- Access the Data Sources tab from the side navigation panel.
- Choose the connection (database) for which you need to modify the sync schedules.
- Click Sync Settings.
- The Cloud Database - Synchronization Settings will open; click Set Multiple Sync Intervals.
- Select the tables that should be moved to a new sync interval.
- In the Schedule Settings section, choose the interval in which the data should be synced from the Repeat option drop-down menu. Zoho Analytics provides multiple sync intervals such as Every N hours, Every Day, Weekly Once, Monthly once. Selecting Not Scheduled will import the data only once, i.e., at the time of import.
- Specify the other related settings, such as the time of day (for daily syncs), day of the week (for weekly syncs), and date of the month (for monthly syncs) can be configured based on the selected interval.
- The Notify Me After Every option keeps you informed by sending updates whenever there are consecutive import failures, ensuring you are aware of any issues with data synchronization.
- You can also choose to notify Account Admins, Workspace Admins, Organization Admins, and Custom users (selected users).
- Click Save.
Once multiple sync schedules are configured for a connection, the tables are grouped according to their respective sync schedules.
Case 2: Creating a new sync interval when there is more than one sync interval configured for a connection
Once multiple sync schedules are configured for a connection, the tables are grouped according to their respective sync schedules.
- Access the Data Sources tab from the side navigation panel.
- Choose the connection (database) for which you need to modify the sync schedules.
- Select the tables you want to add to a new interval and click Move table.
- Choose the Schedule to which the tables should be moved and click Move. The tables will be moved to the chosen sync interval.
Alternately, you can also create a New Sync Interval using the steps given below:
- Choose the Schedule from which you want to move tables to a new schedule.
- Click the Edit option adjacent to the Schedule field.
- The Cloud Database - Synchronization Settings will open; click Create New Sync Interval.
- Select the tables that should be moved to a new sync interval.
- In the Schedule Settings section, choose the interval in which the data should be synced from the Repeat option drop-down menu.
- The successive steps are similar to the steps mentioned in the above section.
Configuring Multiple Sync Intervals While Importing a New Table in an Existing Connection
- Click the Create icon on the side navigation panel and choose New Table or Import Data.
- Choose existing connections and the tables to be imported. Click Next.
- By default, the existing schedule will be applied to the new tables that are set to import. Click Edit Schedule to modify the schedule interval.
- Choose the preferred data fetch method and click Next. Refer to this article to learn more.
- The existing data sync schedules will be listed; click Create New Sync Interval.
- In the Schedule Settings section, choose the interval in which the data should be synced from the Repeat option drop-down menu. Zoho Analytics provides multiple sync intervals such as Every N hours, Every Day, Weekly Once, Monthly once. Selecting Not Scheduled will import the data only once, i.e., at the time of import.
- The other related settings, such as the time of day (for daily syncs), day of the week (for weekly syncs), and date of the month (for monthly syncs) can be configured based on the selected interval.
- The Notify Me After Every option keeps you informed by sending updates whenever there are consecutive import failures, ensuring you are aware of any issues with data synchronization.
- You can also choose to notify Account Admins, Workspace Admins, Organization Admins, and Custom users (selected users) in the case of sync failures.
- Click Save.
Managing Sync Schedule for Tables
Zoho Analytics allows you to move tables from different sync intervals to another schedule. This feature enables you to efficiently manage data updates and ensure related tables are refreshed at the desired intervals.
Follow the below steps to change the schedule interval of tables:
- Choose the schedule to which you wish to move the tables. Here we are moving tables from other schedules to schedule 1.
- Choose the Schedule 1 and click Add tables.
- All the data sync schedules configured for the data source will be listed. Select the tables you want to move from other schedules (2 and 3) and click Save.