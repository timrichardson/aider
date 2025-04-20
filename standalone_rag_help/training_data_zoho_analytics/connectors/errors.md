Synchronization Failure Errors
Zoho Analytics allows you to synchronize data from various business applications automatically at specific time intervals. Sometimes, synchronizing data from your application may fail. In this page, we list down the reasons for failure and how to resolve them.
Note: You will be notified regarding sync failures through in-app notifications. If in case the sync continuously fails for more than 24 hours, you will be notified through email.
Initial Fetch Failure
Reason: Initial data fetch may fail for various reasons.
Solution:
Follow the below steps to solve this.
- Open the Workspace in which you have set up the connector.
- Click the Data Sources button in the Explorer.
- In the Data Sources page that opens, click the Retry Now link.
If problem persists, contact our support at support@zohoanalytics.com.
Business Application Connectors: All
Insufficient Permission
Reason: Your Business Application account does not have sufficient permission to use the connector.
Solution: Verify the respective Business Application connector document to know the necessary permission and ensure you have the permission to set up the connector.
Business Application Connectors: All
Authentication Failure
Reason: The login credentials you have used were invalid.
Solution:
Follow the below steps to solve this.
- Open the Data Sources page of the connector workspace.
- Click Re-authenticate.
- Login again with valid credentials to continue using the connector.
Business Application Connectors: All
Connection Error
Reason: A temporary error occurred while synchronizing data from your Business Application.
Solution: Zoho Analytics will automatically retry the data synchronization in the next schedule.
Business Application Connectors: All
Pricing Plan Mismatch
Reason: Your Business Application account pricing plan does not support Zoho Analytics integration.
Solution: Ensure you have upgraded to a pricing plan in your application that supports Zoho Analytics integration, before setting up the connector.
Business Application Connectors: All
API Rate Limit Error
Reason: The daily/hourly API limit in your Business Application account was exceeded.
Solution: The data synchronization will automatically resume on the next day.
Business Application Connectors: All
Row Count Exceeded
Reason: You have exceeded the row count allowed in your Zoho Analytics plan.
Solution: You can either upgrade your Zoho Analytics plan or buy Rows Add-on to continue using the connector.
Business Application Connectors: All
Connector Deactivated
Reason: The connector got deactivated as you have exceeded the allowed integration limit for your account. e.g., the Basic plan of Zoho Analytics supports only two Business App Connectors.
Solution: Upgrade your Zoho Analytics plan to continue using more than two connectors.
Business Application Connectors: All
Dependent Fields Deleted in Source Application
Reason: The data synchronization process will get stopped if any dependent fields of the synchronized data is being deleted in your Business Application.
Solution: You can either restore the dependent fields in your Business Application, or edit the integration setup and remove the fields that are dependent on the deleted fields.
Business Application Connectors: All
Connector Owner is no longer an Admin
Reason: User who has configured this connector has been deactivated or removed from the Admin role in the Business Application.
Solution:
Follow the below steps to solve this.
- Open the Data Sources page of the connector workspace.
- Click Re-authenticate.
- Login again as a user who has Admin rights, and continue using the connector.
Business Application Connectors: All
Zoho Suite Trial Expired (Zoho CRM Plus / Zoho One)
Reason: Trial for your Zoho Suite (Zoho CRM Plus / Zoho One) account has expired.
Solution: Subscribe to a sufficient pricing plan to continue using this integration.
Business Application Connector: All
Another Sync is in progress
Reason: The sync process could not be started since another sync is in progress.
Solution: Zoho Analytics will automatically retry in the next scheduled data synchronization.
Business Application Connectors: All
No Zoho Creator Default Workspace
Reason: No default workspace exists in Zoho Creator.
Solution: Ensure to create a default workspace in Zoho Creator to use this integration.
Business Application Connector: Zoho Creator
Accept Zoho Creator Invitation
Reason: Invitation to access this application is yet to be accepted.
Solution: Please accept the invitation, or contact your application admin.
Business Application Connector: Zoho Creator
Application Disabled or Permission revoked
Reason: The application you have selected in Zoho Creator might be deleted, or permission for the user who configured the connector setup is revoked.
Solution: Please get access to the application to resume the data synchronization.
Business Application Connector: Zoho Creator
Salesforce Connectivity Error
Reason: Zoho Analytics cannot connect to Salesforce.com due to an error from Salesforce.
Solution: For more details about this error, contact us at support@zohoanalytics.com.
Business Application Connector: Salesforce
Recruit Model Changed
Reason: Zoho Recruit model has changed
Solution: Reconfigure as a new integration setup between Zoho Recruit and Zoho Analytics.
Business Application Connector: Zoho Recruit
QuickBooks Desktop Different File Opened
Reason: A different QuickBooks Company file has been opened.
Solution: Open the correct QuickBooks Company file.
Business Application Connector: QuickBooks Desktop
Microsoft Dynamics CRM Audit Permission
Reason: You don't have permission to read audits in Microsoft Dynamics CRM Organization.
Solution: Request your System Administrator to enable audit read permission.
Business Application Connector: Microsoft Dynamics CRM
Twitter Access Denied
Reason: Protected handle(s) tweets cannot be fetched with your Access Token.
Solution: Remove Protected handle(s) from the connector.
Business Application Connector: Twitter
Invalid Organization
Reason: The selected organization in Business Application was either deleted or revoked.
Solution: Ensure you have selected a valid organization in the integration.
Business Application Connectors: Zoho Campaigns, Zoho Books, and Zoho CRM
Limit Exceeded
Reason: You have exceeded the allowed limit for organizations/modules/fields to be synced.
Solution: You can set up a new connector in the same workspace to add more entities.
Business Application Connector: Google Analytics, LinkedIn Pages, Eventbrite, and Mailchimp.
Selected Account Deleted
Reason: All the selected entities such as Zoho Projects, Zoho Campaigns and Zoho Survey are deleted in your Business Application.
Solution: Ensure you have selected active entities to resume the data synchronization.
Business Application Connectors: LinkedIn Pages, Zoho Survey, and Zoho Projects
User Removed
Reason: Your account is removed from the Business Application
Solution: Contact your Business Application account admin to add your account to resume the data synchronization.
Business Application Connector: LinkedIn Ads, and Zoho Survey
Account Error
Reason: Your Business Application account is not verified, disabled or deleted.
Solution: Ensure your Business Application account is verified and re-authenticate the connector.
Business Application Connector: LinkedIn Ads, and YouTube
No Active Entities
Reason: Your Business Application account does not have any active Organization, Accounts, or Projects to integrate with Zoho Analytics.
Solution: Please create an entity to use this integration.
Business Application Connectors: Bing Ads, Eventbrite, Exact Online, Facebook Ads, Google Analytics, Instagram, LinkedIn Pages, Mailchimp, Site24x7, Zoho Survey, Alchemer, SurveyMonkey, Teamwork, YouTube, Zoho Projects, and Zoho Sprints.
Zoho Finance Org Migrated or Deleted
Reason: Zoho Finance Organization might be removed or migrated from anyone of the Zoho Finance applications.
Solution: Edit the connector setup and choose a valid Organization to resume the data synchronization.
Business Application Connector: Zoho Finance