Advanced Analytics for Qualtrics
The Advanced Analytics Connector for Qualtrics enables you to proactively research, manage, and extract useful insights from the data collected through Qualtrics. With this integration, you can seamlessly analyze your survey responses, uncover key metrics, and transform these insights into strategic actions to enhance experiences and outcomes across various areas of your organization.
- Setting up the Integration
- Handling Data Synchronization Failure
- Managing Data Sources
- Data Modeling & Preparation
- Data Visualization/Analysis
- Sharing & Collaboration
- Help & Support
Setting up the Integration
A user with administrator privileges (Account admin and Org admin) can configure the integration.
Note:
- The initial fetch might take a few minutes depending on the volume of the data to be imported. An email and an in-app notification will be sent, once the initial fetch is complete.
- The setup process can sometimes fail for a variety of reasons. In this case we request you to access the Data source tab and click the Retry link to import again. If the issue persists then write to support@zohoanalytics.com.
Data Sync Frequency
Zoho Analytics offers flexible sync schedules to ensure that your data is always up-to-date for effective analysis. These schedules allow you to automate the process of updating your data, ensuring that your analysis are based on the latest information.
- 1 Hour (Enterprise plan)
- 3 Hours (Standard plan and above)
- 6 Hours (Standard plan and above)
- 12 Hours (Standard plan and above)
- Daily (Basic plan and above)
Handling Data Synchronization Failure
Data synchronization can fail,
- If the data type of a field is changed in the Qualtrics Application.
- If the Modules and Field selected for analysis are deleted in the source application.
- If the user who configured the integration no longer has permission to access the modules.
In any of the above mentioned cases, the data sync will be paused. You will be notified via email and in- app notification with the exact reason for failure along with the solution.
To resolve the sync failure, delete or restructure the views, or restore the specific modules and fields from the source application. Refer to Data Sync failure and solutions article for more details.
Once you have made the changes, click the Sync now option in the data source tab to resume data sync. If the issue persists, mail us at support@zohoanalytics.com
Managing Data Sources
The Data Sources tab provides essential information to monitor and manage the integration setup. It also allows you to edit the settings as needed. Users with administrator privileges will be able to view and modify the connection settings.
Data Source Permalink
The Data Source Permalink helps you easily access the data source tab. Only the Organization Admin and Account Admin can make changes in the Data sources page, other users can know the synchronization details like whether the last data sync was successful or not, when the last data sync happened, when the next sync is scheduled to happen, etc. This link can also be pasted in dashboards so that everyone accessing the dashboard can know about the sync status.
Note: Additionally, users with Organization Admin and above privileges can do the following actions :
- Edit Setup
- Re-Authenticate
- Audit History
Edit Setup
The Edit Setup tab allows you to add or delete modules or fields, change the schedule interval, and modify other settings specific to the business application.
To modify the settings,
- Click Data Sources > Edit Setup.
- The Edit Setup - Qualtrics dialog will open. Modify the settings as needed and click Save.
Re- Authenticate
Re-authentication will be helpful when the API key or password is changed. In this case, the data sync will be paused, and the administrator who configure the connector setup must re-authenticate to resume the data sync.
To re-authenticate,
- Click Data Sources > Re-Authenticate.
- The Re-Authenticate Qualtrics dialog will open. Click Authenticate Qualtrics and enter the Qualtrics credentials to re-authenticate.
Sync History
The Sync History tab provides details about the data sync for the last 45 days. A successful data sync is marked in green, and a sync failure is marked in red.
To view the Sync history,
- Click Data Sources > Sync History.
- A calendar with the Sync History of the last 45 days will open. The date when the data sync has happened will be highlighted. Hover to view the number of times the data had got synced on a specific date.
- Click the date to view more details.
- Time - Displays the time when the data is synced.
- Status - Shows whether the sync was a success or a failure.In case of failure, the reason will be displayed. Refer to this page to learn how to resolve the issue and avoid further failure.
Audit History
Zoho Analytics logs all the user activities and system events within the Qualtrics workspace. The following actions are logged in Zoho Analytics,
- User Action: Create, Modules Added, Modules Removed, Fields Added, Fields Removed, Schedule Change and Entities Modified, Delete, Take Ownership, Re-authenticate, Sync Now, Retry.
- System Action: Plan upgrade or downgrade.
To view the audit history,
- Click Data Sources > Audit History.
- A dialog with the activities for the last 180 days will open.
Remove Data Source
Zoho Analytics allows you to remove the integration if needed. Removing the integration will suspend further data synchronization. However, the data tables and the reports will be available.
Click the Settings icon in the Data Sources tab, and select Remove Data Source from the drop-down menu.
Data Modeling & Preparation
Zoho Analytics allows you to combine data from various sources such as Files, Feeds, Databases and Business Applications for an in-depth analysis. Query Tables allow you to combine data from different tables to create reports. The SQL Query Suggester helps to build complex queries.
Zoho Analytics auto identifies similar columns and provides suggestions for lookup while importing. Click here to learn more about Joining Tables.
Data Visualization / Analysis
Zoho Analytics offers a wide range of visualization types to conduct your analysis. Refer to the Creating Reports section to learn more.The below table lists the range of visualizations supported in Zoho Analytics.
| Visualization | Types |
Bar | Stacked bar, Histogram, Horizontal bar |
Stacked Bar | Horizontal Stacked bar, 100% vertical and horizontal stacked bar |
Area | Area with markers, Smooth Area, Smooth area with Markers |
Line and Bar Combination chart | Bar with Line, Bar with Bubble, Bar with Scatter, Bar with Area, Area with Bubble, Line with Bubble and Custom Combination |
Bubble Chart | Bubble Pie, Packed Bubble, Word Cloud |
Stacked Area | Stacked area with markers, Smooth stacked area, Smooth stacked area with markers |
Map | Heat Map, Map Scatter, Map Bubble, Map Pie, Map Bubble Pie, Map Filled, Geo Heat Map |
Pie | Pie, Ring, Semi Pie, Semi Ring |
Tree map | Default View |
| Sankey | Default View |
Sunburst | Default View |
Race Chart | Default View |
Doughnut | Default View |
Matrix View | Pivot table |
Tabular | Summary and Tabular view |
Dashboards and KPI widgets | Single Numeric Widget, Dial Chart Widget Bullet, Chart Widget |
Sharing and Collaboration
- Use fine-grained permission control over your shared data and reports, while collaborating with your colleagues & friends.
- Efficiently collaborate with your users by setting up real-time commenting on a shared view.
- Publish reports for wider consumption. Embed reports/dashboards within your websites, web applications, and blogs.
- Export, email, and print reports in a variety of formats.
- Use Zoho Analytics mobile apps (optimized for both IOS and Android platform) and access data, reports, and dashboards on the go.
Help & Support
We offer 24x5 technical support (Monday to Friday). In case if you need our assistance kindly do mail us your questions to support@zohoanalytics.com.
You can also reach out to us on our toll-free numbers.
United States: +1 (888) 900 9646
United Kingdom: +44 (20) 35647890
Australia: +61-2-80662898
India: +91 44 6965 6060