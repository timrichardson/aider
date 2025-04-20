Import data from Common Cloud Services into Zoho Analytics
If you have your data stored online in cloud services such as Hostgator, Amazon EC2, Linode etc, then you can seamlessly import your data into Zoho Analytics for reporting and analysis. You can also easily set up schedules to periodically fetch the latest data from your cloud database.
- Data Import: Data from Other Cloud Services will be imported and stored in Zoho Analytics. You can setup periodic schedules to fetch the latest data automatically from your database. Report loading time will be faster as the data is stored in Zoho Analytics.
- Live Connect: In this mode, data will not be fetched from Other Cloud Services and stored in Zoho Analytics. Instead for the reports that you create Zoho Analytics will generate appropriate queries that will connect the required data live from your database to Zoho Analytics and show you the report. In this case the loading time will directly depend on the performance of your database.
- Zoho Analytics currently has direct connections with cloud services such as Amazon RDS, Amazon Redshift, Microsoft Azure, Google Cloud SQL, and Heroku. If you have your data stored in any of them you can import your data into Zoho Analytics directly by using the appropriate options.
- The Live Connect option is exclusively available for paid plans and trials only. Refer to the Live Connect section to learn.
Data Import
- Preamble: Why should I whitelist Zoho Analytics IP addresses?
- How do I import data from common cloud services?
- How long does it take for the data to be imported into Zoho Analytics?
- Will foreign keys defined between my tables in common cloud services be linked in Zoho Analytics as well?
- Can I change the data-type of the columns in Zoho Analytics?
- How can I edit the setup?
- Can I import data from any of the cloud services into an existing Zoho Analytics workspace?
- How do I remove the Setup?
Live Connect [Beta]
- Preamble: Why should I whitelist Zoho Analytics IP address and how do I do it?
- How do I connect live with common cloud services?
- How can I edit the live connect setup?
- How is Live Connect different from Data Import?
- How long does it take for me to visualize my data in Zoho Analytics?
- I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
- What is a Mismatch?
- When do Mismatches occur and how to resolve them?
- Can I connect the new columns added in my cloud service database to Zoho Analytics?
- Can I change the data-type of the columns in Zoho Analytics?
- Can I import data from other data sources into the same workspace that I have used to connect with the cloud service?
- Can I create Query Tables over the common cloud service data?
- What happens when I delete or rename the database in my cloud service database?
- How do I remove the Setup?
- What are the limitations of cloud service Live Connect?
Troubleshooting Tips
- I get an error message "Sorry, there is a problem in connecting to your cloud data source. Check your connection details and try again." What should I do?
- I am unable to find the Live Connect option while importing data into Zoho Analytics. What could be the possible reasons?
1. Preamble: Why should I whitelist Zoho Analytics IP addresses?
It is mandatory that you whitelist Zoho Analytics IP addresses in your cloud service. This is because only post whitelisting will Zoho Analytics be allowed to access the information stored in the database. Click here to get the complete list of IP addresses that need to be whitelisted.
Please do note that trying to import data into Zoho Analytics before whitelisting the IP addresses will result in import failure.
2. How do I import data from the common cloud databases such as Hostgator, Amazon EC2, Linode etc?
3. How long does it take for the data to be imported into Zoho Analytics?
After setup, you might have to wait sometime for the initial fetch to happen. This depends upon the amount of data fetched from the cloud database and also the response time of the server. You will receive an email notification once the import is complete. If you access the Workspace before the initial fetch, it will not display any data.
4. Will foreign keys defined between my tables in common cloud services be linked in Zoho Analytics as well?
When importing multiple tables, the foreign keys defined between the tables in your cloud service database will be linked in Zoho Analytics. The foreign keys will be created as Look-up columns in Zoho Analytics.
If you import data from one table at a time (choosing single table option) then the foreign keys will not be defined. However, you can manually link the tables in Zoho Analytics using the Look-up column feature. Click here to learn about the Look-up column feature.
5. Can I change the data-type of the columns imported in Zoho Analytics?
Yes, you can change the datatype of the columns imported into Zoho Analytics. However, it is necessary that the datatype of your column is compatible with the datatype of the column in your Cloud database for successful data synchronizations. It is always recommended that you change the data type in both your cloud service as well as your Zoho Analytics database.
6. How can I edit the setup?
7. Can I import data from any of the cloud services into an existing Zoho Analytics workspace?
Yes, follow the below steps to import data into an existing workspace:
- Open the Workspace into which you wish to import the data.
- Click the Import Data button in the Explorer tab.
- Click Cloud Databases option.
Configuring the import will be similar to the steps followed in this Setup presentation.
8. How do I remove the Setup?
To remove the setup,
- Login to your Zoho Analytics account.
- Open the corresponding Workspace.
- In the Explorer tab, click Data Sources button.
- In the Data Sources tab that opens click the Settings icon and select Remove Data Source as shown in the snapshot.
Please do note that this only removes the connection. You can still continue accessing the Workspace in Zoho Analytics.
Live Connect [Beta]
1. Preamble: Why should I whitelist Zoho Analytics IP addresses and How do I do it?
It is mandatory that you whitelist Zoho Analytics IP addresses in your cloud service. This is because only post whitelisting will Zoho Analytics be allowed to access the information stored in the database. Click here to get the complete list of IP addresses that need to be whitelisted.
Please do note that trying to import data into Zoho Analytics before whitelisting the IP addresses will result in import failure.
2. How do I connect live with common cloud services?
3. How can I edit the live connect setup?
4. How is Live Connect different from Data Import?
Tabulated below are the differences between the Data Import feature and Live Connect feature.
| Data Import | Live Connect |
| Data in the cloud service will be imported and stored in Zoho Analytics. | Data from cloud service will be fetched live using appropriate reporting queries whenever you create or access a report in Zoho Analytics. |
| Filtered data set can be imported from cloud service using customized queries. | Custom Query feature is not available in cloud service Live Connect. |
| Multiple data sources can be imported into the same workspace and they can be combined for reporting & analysis purposes. | Cannot import data from any other data source into the same workspace in which Live Connect from the cloud service is setup. |
| Changes made to the columns such as addition/deletion will be synchronized automatically. | Any changes such as column addition/deletion/renaming will not be reflected. You will have to manually map the data using the Sync Design option. |
| Users can create query tables. | Users cannot create query tables. |
| Report loading time will be fast as the data is stored in Zoho Analytics. | Report loading time directly depends on the cloud service server response time and the amount of data in cloud service. |
5. How long does it take for me to visualize my data in Zoho Analytics?
As there is no data import process involved, the loading time depends upon the amount of data stored in your cloud service database and also the response time of your cloud service server.
6. I got an alert message "This view cannot be accessed due to some changes made in the table" while accessing my tables/reports in Zoho Analytics. What should I do?
This alert message will be displayed when Zoho Analytics is not able to access the information from the cloud service. This could be because the tables/columns that you are trying to access in Zoho Analytics is deleted or renamed in cloud service.
In this case, it is recommended that you remap the table/column. Refer to this presentation to know how to remap a table.
7. What is a Mismatch?
When you have created reports in Zoho Analytics over the tables or columns which no longer have a direct mapping in cloud service database, it will be listed as mismatch.
So, ensure that the tables/columns in Zoho Analytics workspace and cloud service database matches. The tables/columns that do not match will be listed in the Mismatch tab of the Amazon RDS Connection Settings page. Refer the next question to know more about mismatch.
8. When do Mismatches occur and how to resolve them?
9. Can I connect new columns added in my cloud service database to Zoho Analytics?
Yes, you can connect the new columns that are added in your cloud service database to Zoho Analytics from the Amazon RDS Connection Settings page. Refer to this presentation to know more.
Note:
If there exists a mismatch between the already available data in your Zoho Analytics workspace and your cloud service database, Zoho Analytics will NOT be able to fetch the new column information. In this case, you need to first resolve the mismatches to connect to the new columns.10. Can I change the data-type of the columns in Zoho Analytics?
No, you cannot change the data type of the columns in Zoho Analytics.
11. Can I import data from other data sources into the same workspace that I have used to connect with cloud service?
No, you cannot import data from other data sources into the same workspace that you have used to connect with the cloud service.
12. Can I create Query Tables over the common cloud service data?
No, you will not be able to create Query Tables if you have setup the workspace using the Other Cloud Service Live Connect option. This is because this option does not fetch and store the data locally in Zoho Analytics. If you wish to create Query Tables, we request you to use the Data Import option.
13. What happens when I delete or rename the database in my cloud service database?
When you delete or rename a database in your cloud service, Zoho Analytics loses its connectivity with your cloud service. Thereafter, a warning message, as shown below, would be displayed. This error message will also be displayed if there are any connectivity issues or if your cloud service credentials have expired.
For more information regarding the same, refer to the Edit Connection presentation.
14. How do I remove the Setup?
You have to delete the workspace in Zoho Analytics to remove the connection setup.
To delete the workspace,
- Log in to Zoho Analytics
- Click the More Actions icon that appears on mouse hover adjacent to the workspace name that you want to delete
- Click the Delete Workspace option
15. What are the limitations of using the cloud service Connect?
Given below are a few shortcomings that one might face while using the Other Cloud Services Live Connect option.
- Data from your cloud service database will NOT be locally stored in Zoho Analytics. Zoho Analytics will generate appropriate queries to fetch the required data live from your cloud service and show you the report. Hence, the loading time will directly depend on the performance of your cloud service.
- Any changes such as column addition/deletion/renaming will not be mapped automatically. The user must manually map the updates made.
- Users cannot combine data from other data sources into the same workspace in which you have connected the common cloud service database.
- Users cannot create query tables.
Troubleshooting Tips
1. I get an error message "Sorry, there is a problem in connecting to your cloud data source. Check your connection details and try again." What should I do?
This error occurs in the following scenarios:
| Scenario | Solution |
| Incorrect connection settings are specified | Ensure that the correct Endpoint/Hostname, Port, and user credentials are specified. |
| Your cloud database service does not recognize Zoho Analytics as an authenticated agent to fetch the data | To import data from your cloud service, you need to whitelist Zoho Analytics IP address. |
2. I am unable to find the Live Connect option while importing data into Zoho Analytics. What could be the possible reasons?
You will be able to connect live in Zoho Analytics only if,
- You have a paid or trial plan.
- You are importing data into a new Workspace in Zoho Analytics.