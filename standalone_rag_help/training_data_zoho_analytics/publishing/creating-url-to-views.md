Creating URL/Permalink to Views
Zoho Analytics allows you to easily create a stand alone Permanent URLs (Permalink) for all your reports and dashboards in a few clicks. These URL's can be made accessible with a secured login or a private permalink or with public access. Users visiting these links will be able to see the latest live version of the view. Permalink enables easy and quick access of the report/dashboard through bookmarking.
- What are the views for which I can generate a permanent URL?
- What are the access modes available when generating a URL for a report/dashboard?
- What are the differences between the three available access modes?
- How to generate a secured URL for a report/dashboard?
- How to generate a Private URL/permalink for a report/dashboard?
- Can I protect my Private URL (without Login) with a password?
- Can I set an expiry date for my Private URL (without Login)?
- How to generate Public access URL for a view?
- Can the published reports and dashboards be shared across social handles?
- How to share published reports and dashboards across social handles?
- What are the interaction options that are supported on a report/dashboard while accessing the URL?
- I regenerated the Private URL, now I cannot access my previously embedded views or URL's of that report/dashboard. What should I do?
- What are the permissions that can be granted while sharing the report/dashboard?
- How do I edit the permissions of the URL accessed?
- How do I remove the access of the URL?
- Can I pass a dynamic filter while generating the URL?
1. What are the views for which I can generate a permanent URL?
You can generate individual permanent URL's for all types of views such as tables, charts, pivots, tabular view, summary view, query tables and dashboards that you create using Zoho Analytics. Refer to this question to learn about generating a URL.
2. What are the access modes available when generating a permalink/URL for a report/dashboard?
The following are the three access models that you can choose while generating a URL for a report/dashboard.
- Secured Login (with login): This is the most secure mode. Only the users with whom you have shared the report will be able to view it upon logging into Zoho Analytics.
- Private permalink (without login): When this setting is selected Zoho Analytics will generate a URL which will contain a big randomly generated private key (private link), making them secure and very hard (if not impossible) to guess. Users can view the report without logging in to Zoho Analytics. This is available only in the Premium and Enterprise plans of Zoho Analytics.
- Public Access: In case you want your report to be accessible to the users within your organization or to the users who visit your web page and do not require any random key based link generation or logging into Zoho Analytics, you can use the public access mode.
3. What is the difference between the three available modes?
Generating a URL with secured login allows the highest level of security to the view. Selecting "Private Access with Login", would prompt the users to login to Zoho Analytics to access the view. Also, only users to whom you have shared the view would be able to access the view, on successful login.
When selecting "Private Access without Login", Zoho Analytics will generate a private permalink/URL making it secure and very hard to guess. Users need not login to Zoho Analytics to view the report. Although this is secure, the randomly generated key is not impossible to guess.
In case you want your report to be accessible to the users within your organization or to the users who visit your web page and do not require any random key based link generation or logging into Zoho Analytics, you can use the public access mode.
4. How to generate a secured URL for a report/dashboard?
Click to learn about editing permissions.
5. How to generate a Private Permalink/URL for a report/dashboard?
Click to learn about editing permissions.
6. Can I protect my Private URL (without Login) with a password?
Yes, you can protect your private URLs (without Login) with password. When you generate a permalink with Private Access (Without Login) Zoho Analytics will generate a private permalink making it secure and very hard to guess. You can also protect it with a password by selecting Set access password checkbox in Access URL dialog.
7. Can I set an expiry date for my Private URL (without Login)?
Yes, you can set an expiry date for your URL by checking the Set expiry checkbox in the Access without Login section. The shared URL will be valid only for the specified time frame. After the mentioned date, the URL will expire. After the set time, you can extend the expiry date, if you want to extend the validity.
8. How to generate a Public access permalink/URL for a report/dashboard?
Click to learn about editing permissions.
9. Can the published reports and dashboards be shared across social handles?
Yes, you can share the published reports and dashboards in your social handles using the Social Widget option. Learn more.
10. How to share the published reports and dashboards across social handles?
Follow the below steps to share the published reports and dashboards in your social handles:
- Click the Share button from the top-right corner.
- Select the URL/Permalink option from the drop-down menu.
- Select the Access Permission as Access without Login or Access within the Organization/External Users.
- Choose the Social Widgets checkbox available in the Options section.
- When you access the published report/dashboard, you will notice the Facebook, Twitter, and LinkedIn icons. Using these icons, you can share/tweet them.
11. What are the interaction options available?
Zoho Analytics allows you to generate URL's of reports/dashboards in an interactive mode. The following interactions are possible when generating a URL in interactive mode:
1. Tooltips & highlights.
2. View the underlying data
3. Drill down
4. Change chart type
5. Apply User Filters, if the chart contains user filters
6. Interact with legend
You can also generate URL's for reports to display it as a image. This feature is only available for charts. As a result of this, the chart will be generated as a static image and hence the URL will load faster.
12. I regenerated the Private URL, now I cannot access my previously embedded views or URL's of that report/dashboard. What should I do?
When you reset/regenerate the URL, the previously shared URL's will become invalid. You will have to update the latest URL to continue accessing the report/dashboard. In case you have used the URL in the embed snippet that will become invalid as well. You will have to regenerate the new embed snippet and update the page.
13. What are the Permissions that can be granted while sharing the URL of a report/dashboard?
The following permissions can be granted while sharing the URL of a report/dashboard.
14. How do I edit the permission of the URL accessed?
You can edit the previously granted permissions by following the below steps:
- Open the corresponding view that has been published and invoke the Publish > Embed in Website/Blog.
- From the Embed / Publish URL page that opens, click the Edit link at the top right corner or the Edit Permissions link in line with Access without Login menu.
\
15. How do I remove the access of the URL?
You can easily remove the permissions by following the below steps:
- Open the corresponding report that has been embedded and invoke the Publish > Embed in Website/Blog.
- From the Embed / Publish URL page that opens, click the Edit link at the top right corner.
- Click the Remove icon in line with the respective access to remove the permission.
16. Can I pass a dynamic filter for the view?
Zoho Analytics allows you to apply dynamic filters to your views when sharing it to your users.
Using this feature, you can share the same permalink to different set of users by applying different set of filter criteria, to suit the allowed permission, context and profile of the user who is accessing the URL.
Filters can be applied by passing the required filter criteria to the parameter named ZOHO\_CRITERIA and appending it as a part of the URL/Permalink. The view's data is filtered and displayed based on the criteria specified, whenever a user access the link.
Example:
The generated Permalink/URL for a chart would look like as shown below.:
https://analytics.zoho.com/open-view/1156972000001226026
The above URL displays Store Sales bar chart when accessed by the users. To limit the view to just show the Store Sales for the year 2016, add ?ZOHO\_CRITERIA=year("Store Sales"."Date")='2016' to the URL as shown below. Here in the example Year function is used to extract year from the column Date.
https://analytics.zoho.com/open-view/1156972000001226026?ZOHO\_CRITERIA=Year("Store Sales"."Date")='2016'
Filter Criteria Format
The filter criteria that is passed follows the same format as that of the SQL SELECT Query's WHERE clause. You can also use SQL in-built functions as part of the criteria. These built-in functions should be the functions supported by any of Oracle, MS SQL Server, MySQL, DB2, Sybase, ANSI SQL, Informix and PostgreSQL databases.
The generalized format of simple criteria is given below.
| ZOHO\_CRITERIA="(<[tablename].[columnname]/SQL expression/SQL function calls>  )" |
Description:
| Column name | Refers to the name of the column on which you are applying the criteria |
| SQL Expression | Any valid SQL Expression. Eg: "Store Sales"."Sales"-"Store Sales"."Cost">1000 Supported Arithmetic Operators are: +, -, \*, / |
| SQL Function call | In-built standard functions from Oracle, MS SQL Server, MySQL, DB2, Sybase, ANSI SQL, Informix and PostgreSQL databases Eg.: year([table\_name].[date\_column]) = 2016 |
| Relational operator | Any relational operator to compare values supported in an SQL SELECT Query WHERE clause. The following operators can be used:
|
| Value | Refers to the exact value to match Eg.: "Accounts"."Department" = 'Finance" here 'Finance' is a literal value to match. |
You can also define filters containing multiple columns as the example given below
(("Store Sales"."Region"='South' AND "Store Sales"."Sales" < 10000) OR ("Store Sales"."Region='West' AND "Store Sales"."Sales" < 10000))
Notes for Criteria formation:
- You can combine any number of criteria defined in the above-specified format using Logical Operators like AND and OR to form complex criteria, the same way as in SQL SELECT WHERE clause. Also, use Braces '()' to group the criteria for ordering.
- Enclose string literals (i.e. values) in single quotes.
- Enclose column names in double quotes.
- Eg.: ("Store Sales"."Date Of Birth" = '2016-01-31 00:00:00')
- Currency symbols (or) percent symbol can't be used in criteria
- Eg.: [table\_name].[currency\_column] = 75.66 is valid
- Eg.: [table\_name].[percent\_column] = 100 is valid
- [table\_name].[currency\_column] = 75.66$ (or) [table\_name].[percent\_column] = 100% is not valid
Refer to the SQL SELECT WHERE clause documentation to know more on how to construct the filter criteria.