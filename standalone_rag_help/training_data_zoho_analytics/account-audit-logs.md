Audit Logs
Zoho Analytics allows you to track the activity of all users -- Administrators, Users, Shared Users, Viewers and Public Visitors -- in your account, through Audit Logs. You can track the following information through the Audit Logs.
- Access Logs - This enables you to monitor access of all the views present in your organization, by users (including public visitors).
- Activity Logs - This enables you to monitor the activities performed in your organization by users.
- API Logs - This enables you to monitor the API call usage in your organization.
When you set up Audit Logs, a workspace named Zoho Analytics Audits will automatically be created in your account. Rows added in this workspace will not be counted in your account usage & subscription pricing.
Access Logs
You can choose to log information such as who accessed your account, when was it accessed, what view was accessed, and from where it was accessed.
You can enable the access logs using the Access Logs toggle button in the Audit tab.
An Access Log table will be created in the Zoho Analytics Audits workspace with the below columns.
- Accessed Time - Date and time, when the view was accessed.
- Accessed By - Email address of the user who accessed the view.
- Workspace Name - Name of the workspace accessed.
- View Name - Name of the view accessed.
- View Type - View type of the view accessed i.e., Chart, Pivot View, Table, Dashboard etc.
- IP Address - IP Address from where the view was accessed.
- User Agent - OS and the browser information of the accessing user.
You can export the access logs in one the supported formats with password protection.
An insightful Access Log Analytics dashboard capturing the essentials of the access log such as Daily Access Trend, Access Count by View Type and by Users, etc., will also be automatically created.
Note: Users with Zoho Analytics Basic plan and above can avail this option. Click here to learn more about Zoho Analytics Pricing Plan.
Activity Logs
You can choose to log the users' activities or actions in your account such as importing data, creating reports, sharing reports etc. Through Activity Logs, you will know who performed these activities, when they were performed, and from where your account was accessed to perform these activities.
You can enable the activity logs using the Activity Logs toggle button in the Audit tab.
The Activity Log table will be created in the Zoho Analytics Audits workspace with the below columns.
- Date & Time - Date and time when the activity was performed.
- Performed By - Email address of the user who performed the activity.
- Action - Name of the activity performed.
- Category - Module in Zoho Analytics where the activity was performed.
- Workspace Name - Workspace name where the activity was performed.
- View Name - View name on which the activity was performed.
- More Details - Additional details about the activity e.g., when you share a view, this column lists which views were shared, and to whom it was shared.
- Remarks - Description of the activity performed.
- IP Address - IP Address from where the user performed the activity.
- User Agent - OS and Browser of the user.
| Module | Actions |
| Import | Import data into a new or an existing table. |
| Workspace Actions | Actions at workspace level which includes:
|
| View Actions | Actions at View level which includes:
|
| Table Actions | Actions at Table level which includes:
|
| User Management | Actions to manage your users which include:
|
| Share | Sharing related actions which include:
|
| Publish | Publishing actions which include:
|
| Export and Email | Exporting and emailing actions which include: |
| Whitelabel Actions | Actions performed in white labeled portals
|
An Activity Insights Dashboard capturing the essentials of user activity such as Daily Activity Trend, Activities Distribution by Category, etc., will also be automatically created.
API Logs
You can choose to log information such as what is the API action done, who has done it, when it is done, and the API units consumed by the action. You can enable the API logs using the API Logs toggle button in the Audit tab.
An API Log table will be created in the Zoho Analytics Audits workspace with the below columns.
- Date - Date when the activity was performed.
- API Name - Name of the API call
- User EmailID - Email address of the user who performed the activity.
- Rows Processed - Number of rows imported or exported.
- Units Consumed - API Units consumed by the call.
- API Count - Number of API count.
- IP - IP Address from where the user performed the activity.
- Version - Zoho Analytics API Version used.
- API Group - The API group that the API action falls under, such as Bulk, Metadata, Embed etc.
An insightful API Log Analytics Dashboard capturing the essentials of the API log such as Units Consumed - By Day, Request Count - By API Groups and Top 10 APIs - By Units Consumed or By Request Count, etc., will also be automatically created.
Note: Users with Zoho Analytics Standard plan and above can avail this option. Click here to learn more about Zoho Analytics Pricing Plans.