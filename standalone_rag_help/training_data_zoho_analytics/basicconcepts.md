Basic Concepts of Zoho Analytics
Zoho Analytics is a self-service BI and data analytics software that lets you analyze your data, create stunning data visualizations, and discover hidden insights in minutes.
This guide will help you to learn the concepts specific to Zoho Analytics. The following topics will be discussed in this guide.
Components
Zoho Analytics provides different components to enable you to store and analyze data. This section elaborates on all the components and how they are connected to each other, to get a better understanding of them.
Organization
Zoho Analytics allows you to manage all your data and analysis in a segregated space called Organization. You can have only one own Organization in your account. You can have unlimited workspaces in an organization.
All the Feature Control or Security Control options you have configured at the Organization level will be applied over all the workspaces in your organization.
Refer to the Admin Guide to learn more about Organization.
Workspaces
All information in Zoho Analytics are organized into logical entities called Workspace. A Workspace is a logical grouping of data sets (stored in entities called Tables) and all the reports & dashboards created over this data. The Workspace also contains structural information on how the entities are related to each other. It also offers methods to create metrics on the data for further analysis.
You can have one or more Workspace in your account which can be owned by you or shared to you by other users.
Click here to learn more about workspace and how to manage them.
Tables
Tables contain the actual data that needs to be analyzed. A Workspace contains a collection of tables. A table is similar to a spreadsheet and consists of columns and actual data rows.
Each column has a name and a type (data type) associated with it. A Workspace typically contains one or more tables with logically related data. For example, a Sales Workspace might contain Products, Sales, and Purchases tables.
If you wish to define a logical relationship between two different data, you can easily do so by creating a lookup (Refer to Relating tables using Lookup columns for more information). Once this is done you can create any type of report, using the columns from the tables.
Click here to learn more about working with tables.
What are Query Tables?
- Query table is a feature that enables you to create specific data views for easy reporting and analysis.
- You can create query tables for use cases like batching data together (union), transform data, apply SQL query functions etc.
- You can create query tables using the standard SQL queries.
- Zoho Analytics currently supports SQL queries written in Oracle, SQL Server, IBM DB2, MySQL, Sybase, Informix, PostgreSQL, and ANSI SQL dialects.
Formulas
Formulas are calculations that help you derive key business metrics that can be used in reporting and analysis. Zoho Analytics provides a powerful formula engine to create any type of calculations required to assist in creating the required reports.
Zoho Analytics supports different types of formulas:
- Custom Formula Columns: These are formula types that will help you add a new column to your data table. The values are derived based on the calculation/formula defined. The output of the formula adds a new column in the table.
- Aggregate Formulas: These formula types use aggregate functions (SUM, AVG.. etc.) in the calculation. These are typically used to derive business metrics. The result of Aggregate Formulas will not be added as another column in the base table, but they can be used while creating reports.
Click here to learn about Formulas in Zoho Analytics.
Reports
Zoho Analytics offers a wide variety of reporting options such as Charts, Pivot Tables, Summary Views, and Tabular Views. This enables you to easily analyze your data and derive great insights. Creating reports is made easy using the intuitive drag and drop interface of Zoho Analytics.
A report can be created by joining one or more tables.
The following types of reports are supported in Zoho Analytics:
- Chart is a visual representation of data which allows you to effectively analyze and interpret data. Zoho Analytics supports over 25+ chart types such as Area, Line, Bar, Stacked, Pie, Scatter, Combination, Funnel, Web, Bubble etc.
- Pivot Table (also known as matrix view) allows you to dynamically rearrange, group, and summarize data for easy analysis of large sets of data. You can filter, sort, customize the appearance and content of your Pivot Table just the way you want it by using the wide range of options provided by Zoho Analytics.
- Tabular View helps you to display the raw data in a simple tabular format. Using this view, you can create a spreadsheet-like report that contains all of your data. You can see your raw data along with summaries and grouping.
- Summary View enables you to view your summarized data in tabular formats. This report is extremely useful when you need to analyze huge amount of data with logical grouping and appropriate summarizations in a visually intuitive manner.
Dashboards
A Dashboard is an effective way of organizing reports into a single page for a quick insight into the Key Metrics at a glance. Zoho Analytics provides a simple and intuitive drag and drop interface for creating dashboards in minutes. You can easily create a visually rich and interactive dashboard by adding reports, widgets, user filters, and rich-formatted text in single or double column layout. You can have any number of reports in a dashboard.
Zoho Analytics also offers a widget-based model for creating single number charts (headline charts) within dashboards. These are called KPI Widgets. This is feature highlights any key metric in a dashboard for easy comprehension. The key metric can also be accompanied with associated comparison indicators to highlight the trend.
Roles
Zoho Analytics supports a role based model, enabling users controlled access over your organization's data, reports and dashboards. To make it easier, Zoho Analytics provides the following roles to collaborate with your users.
Account Administrator
Account Administrator is the person who owns the Zoho Analytics account and has the authority to perform all possible operations available. There can be only one Account Administrator for an account. Account Administrator alone can manage the account subscription.
Organization Administrators
Organization Administrators manage an organization. Organization Administrators have access to all the workspaces within the organization. They can perform all the operations inside their Organization, except add, activate, and deactivate another Organization Administrator.
The Organization Administrator can only be added by the Account Administrator.
Refer to the topic Managing Organizations to learn how to add an Organization Administrator to an account.
This option is available only from the Standard plan and above.
Workspace Administrators
Workspace Administrators are the admin of specific Workspaces in the Organization. Workspace Administrators can perform all the operations in a Workspace, except deleting or renaming the Workspace, and backing up the Workspace.
Workspace Administrators can be added by the Account Administrator and the Organization Administrators.
Refer to the topic Multiple Workspace Administrators, to learn how to add a Workspace Administrator to an account.
This option is available only from the Standard plan and above.
Custom Role
Custom Roles are account level roles that can be defined with a customized set of permissions for your users. This allows you to grant permissions that are only necessary for their job without being over permissive that are bundled in the pre-defined role.
Users associated to these custom roles inherit all the defined permissions over the workspaces shared with them.
Users
Users are the ones who can access the views shared to them with defined permission in the Organization.
Refer to the topic Sharing and Collaboration, to learn more about sharing views.
Viewers
Viewers are the ones who can access the views shared to them by one of the Administrators or Users, in read-only mode.