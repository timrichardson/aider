Import Data into Zoho Analytics from popular CRM Services using Flatly
Flatly is a web automation app that allows you to seamlessly integrate data from popular CRM services such as Insightly CRM, Pipedrive and Base CRM into Zoho Analytics using Google Drive.
Data Import Process using Flatly
Flatly allows to import your CRM data (only from Insightly, Pipedrive and Base) into Zoho Analytics in two simple and easy steps.
Step 1: Flatly copies the data from the above mentioned CRM services and publishes it in Google Drive as a Google sheet or CSV file.
Step 2: You can then import the data stored in Google Drive into Zoho Analytics using the Import from Cloud Storage option available in Zoho Analytics.
Step 1: Importing Data from the CRM Service into Google Drive using Flatly
In order to import data into Zoho Analytics using Flatly, you first need to sign up for a Flatly account.
Once you create an account you will be redirected to the Flat file scheduler page as shown below. Let us now see how to import data from Insightly CRM into Zoho Analytics.
- Select the Data Source as Insightly.
- Select the Destination as Google Drive.
- Provide the Insightly CRM API token in the Enter API Token/Key field and authenticate the connection. Refer the below help links to learn about generating an API token from different CRM solutions.
- Insightly - https://support.insight.ly/hc/en-us/articles/204864594-Finding-or-resetting-your-API-key
- Pipedrive - https://support.pipedrive.com/hc/en-us/articles/207344545-How-to-find-your-personal-API-key
- Base - https://support.getbase.com/hc/en-us/articles/203868725-Does-Base-have-an-API-
Once that is authenticated, select the Target folder in Google Drive. Data from Insightly will get published in this folder. In case you do not have a separate folder in Google Drive you need to create one.
- Select the CRM module that you wish to copy into Google Drive from the Select file to flatten option.
- Select the File format in which the data from the module must be copied/written. Available options are Google Sheets and CSV.
- Select the copy method as Replace Old File.
- Enter a file name.
- Set Email Notification. Choosing Email me after every job will trigger an email to your inbox after each job. In case you do not wish to be notified select Don't email me.
- Setting a Frequency, creates a schedule to periodically fetch your data from Insightly and update it in Google Drive. This way you will have your latest data updated automatically in Google Drive. The available options are 10 minutes, hourly, daily, and weekly.
- Once you have selected all the options, click Run per schedule. This will trigger the import process and periodically update the data from the CRM service.
- Data import into Google Drive might take some time and the duration will be mentioned in the timer as shown below.
You can similarly import the data from Pipedrive and Base CRM as well. Click to learn more.
Step 2: Importing Data from Google Drive into Zoho Analytics
Once the data gets stored in the Google Drive you can easily import it into Zoho Analytics using the Import from Cloud Storage option. Watch the below Zoho Analytics video to learn how.
Related Topics
To know more about using Flatly, refer to this Flatly help document.