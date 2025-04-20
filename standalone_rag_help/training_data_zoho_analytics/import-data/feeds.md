Importing Data from Web Feeds
Often you would have data locally stored in tabular file formats like CSV, XLSX (Excel), JSON, Statistical file and HTML files. The data in such formats could also be available as a URL or Web feed or even some application generated. Zoho Analytics offers easy import and copy-paste options of such data for jump-starting your reporting and analysis. This section explains how to import such data into Zoho Analytics.
Note: You can also import data stored in Web URL or Cloud Storage. To know how to import from these locations, refer to the Importing from Local Files and Importing from Cloud Storage sections.
Watch the below video to get a quick overview on importing data from feeds into Zoho Analytics.
File Types
- What are the file formats that can be imported into Zoho Analytics?
- What are the sources from which I can import data into Zoho Analytics using the files and feeds option?
- How do I import data from a CSV file into Zoho Analytics?
- How do I import data from Excel into Zoho Analytics?
- How do I import data from an HTML file into Zoho Analytics?
- How do I import data from JSON into Zoho Analytics?
- How do I import data from XML into Zoho Analytics?
- How do I import data from Statistical File into Zoho Analytics?
- How do I import data from Microsoft Access Database files into Zoho Analytics?
- How can I import data using an OData feed?
Import Data
- How can I import data from an email attachment?
- Can I import data into an existing table?
- Can I import huge files into Zoho Analytics?
- Can I import data in batches (Pagination) into Zoho Analytics?
- Can I import files from my cloud storage?
- Can I import files stored in my local drive or FTP server?
Import Data from Feeds/URLs with Parameters
- What are the URL methods supported in Zoho Analytics?
- How can I pass parameters while importing data from feed/URL in Zoho Analytics?
- How can I pass headers while importing data from feed/URL in Zoho Analytics?
- Can I import data from a dynamic URL?
- Can I pass multiple parameters while importing data from feeds/URLs in Zoho Analytics?
- Can I import data using Payload?
Import Data from a Secured Feeds/URL
- Can I import data from secured/authenticated URLs?
- How do I import data from URL feeds authenticated via Basic HTTP Authentication?
- How do I import data from URL feeds authenticated via OAuth 1 Authentication?
- How do I import data from URL feeds authenticated via OAuth 2 Authentication?
- How do I import data from URL feeds authenticated via AWS Signature?
- How do I import data from URL feeds authenticated via Digest Authentication?
- How do I import data from URL feeds authenticated via Hawk Authentication?
Import Settings
- How do I set a custom date format?
- Can I map a column from my file into a column in Zoho Analytics table while importing?
- Can I re-fetch/schedule data import?
- Why do I see Warning Details in Import Summary?
- How do I set On Import Error options?
- Can I retain the relational data modeling from my source?
- Can I schedule importing data?
File Types
1. What are the file formats that can be imported into Zoho Analytics?
Zoho Analytics supports importing data from the following sources.
- Comma Separated Value (CSV)
- Excel (XLS and XLSX) /SXC
- HTML
- Tabular Text files
- JSON
- XML
- Statistical File
- OData
2. What are the sources from which I can import data into Zoho Analytics using the Files and Feeds option?
Zoho Analytics allows you to import data from the following sources using the Files and Feeds option:
- Web URL
- Email Attachment
3. How do I import data from a CSV file into Zoho Analytics?
4. How do I import data from Excel into Zoho Analytics?
5. How do I import data from an HTML file into Zoho Analytics?
6. How do I import data from JSON into Zoho Analytics?
7. How do I import data from XML into Zoho Analytics?
8. How do I import data from Statistical File into Zoho Analytics?
9. How do I import data from MS Access Database files into Zoho Analytics?
10. How can I import data using an OData feed?
Import Data
1. How can I import data from an email attachment?
2. Can I import data into an existing table?
Yes, you can import data into an existing table. Follow the given steps to import data into the existing table.
- Open the table into which you want to import data.
- Click Import Data > Import Data into this Table. Import wizard to import data into that table will open.
- In the Import Your Data page, choose the data source from which you want to import.
- The rest of the steps varies based on the data source selected. Refer to the respective help sections to know more.
3. Can I import huge files into Zoho Analytics?
Zoho Analytics has the following restrictions on the size of data import. You can upload a maximum of 1,000,000 rows and the file size should not exceed 100 MB.
However, you can upload huge CSV files using the Zoho Databridge. This is a packaged downloadable tool that is to be installed in your machine. You can also schedule the import of data periodically.
4. Can I import data in batches (Pagination) into Zoho Analytics?
Yes, Zoho Analytics provides the following Pagination options to import data in batches.
- Page Number: You can use this option when your data is stored in multiple pages and you want to import them in the same sequence into Zoho Analytics. You need to provide the following details in the Parameters section of the Import page when using this option:
- Parameter Name: Enter the page parameter name. You can get this name from your API/URL provider.
- Initial Value: Provide the initial page number from which you want to start importing.
- No. of Requests: Provide the number of requests you want to execute in sequence.
In the above screenshot, we are fetching 10 pages. The URL will be executed 10 times as follows:
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?Page=1
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?Page=2
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?Page=3
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?Page=4
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?Page=5
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?Page=6
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?Page=7
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?Page=8
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?Page=9
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?Page=10
Here, the Parameter Name is Page and the No. of Requests is 10.
- Next Page URL: You can use this option when your data is delivered in pages with each page providing the URL for the next page to import. You need to provide the following details in the Parameters section of the Import page when using this option:
- URL Property Path: Provide the property name that will fetch the URL of the next page.
In the above screenshot, the next page URL Property is /next\_page\_URL. The next page will be fetched from the JSON property /next\_page\_URL. This execution will continue until the /next\_page\_URL property is empty or null.
Note: The Next Page URL pagination is applicable only for JSON and XML files.
- URL Property Path: Provide the property name that will fetch the URL of the next page.
- Offset and Limit: You can use this option when you have a huge dataset and want to import them in batches, by providing the start position and batch size of each batch, into Zoho Analytics. You need to provide the following details in the Parameters section of the Import page when using this option:
- Offset Parameter: Enter the Offset Parameter Name given by your API provider.
- Initial Value: Provide the initial value of offset.
- Limit Parameter: Enter the Limit Parameter Name given by your API provider.
- Limit Value: Provide the total number of records to be fetched from the offset.
- No. of Requests: Provide the number of sequential requests to be made.
To fetch 1000 records from the URL http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData which supports Offset and Limit parameters (100 records per API call), we have to invoke it 10 times as follows:
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?limit=100&offset=0
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?limit=100&offset=100
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?limit=100&offset=200
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?limit=100&offset=300
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?limit=100&offset=400
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?limit=100&offset=500
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?limit=100&offset=600
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?limit=100&offset=700
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?limit=100&offset=800
http://reports-ubuntu2.csez.zylker.com/Pagination\_Data/JSONData?limit=100&offset=900
From the 2nd request, the Offset Parameter value is the previous offset value + limit.
Here the Offset Parameter name is Offset, Limit Parameter name is Limit. The Limit Value is 100 and the No. of Requests is 10.
Note:
- These pagination options can be used in Zoho Analytics only if your API provider permits you to do so.
- As of now, you can only paginate files in CSV, JSON, XML.
5. Can I import files from my cloud storage?
Yes, you can import files from cloud storage. Zoho Analytics allows you to import data from CSV, Excel (XLS and XLSX), JSON, HTML, and zipped files stored in different Cloud Storages/Drives such as Zoho Docs, Google Drive, Dropbox, Box and OneDrive.
Refer to the Importing Data from Cloud Storage/Drive section to know more on this.
6. Can I import files stored in my local drive or FTP server?
Yes, you can import files stores in local drive. Zoho Analytics allows you to import data from CSV, Excel (XLS and XLSX), JSON, HTML, Microsoft Access Database file stores in local drive or in FTP server. You can also import data by pasting data.
Refer to the Importing Data from files section to know more about this.
Import Data from Feeds/URLs with Parameters
1. What are the URL methods supported in Zoho Analytics?
The following URL methods are supported in Zoho Analytics:
- Get: Your parameters will be passed as request URLs.
- Post: Your parameters will be passed in the body of the request URLs.
2. How can I pass parameters while importing data from a feed/URL in Zoho Analytics?
You can pass parameters under the Parameters section of the Import dialog in Zoho Analytics. To pass parameters, provide the following:
- Provide a Method type
- Parameter Name
- Value
- Choose Parameter in the Send request as drop-down
- If applicable, you can provide Pagination and Authentication Type
3. How can I pass headers while importing data from a feed/URL in Zoho Analytics?
You can pass headers under the Parameters section of the Import dialog in Zoho Analytics. To pass headers, provide the following:
- Parameter Name
- Value
- Choose Header in the Send request as drop-down
- If applicable, you can provide Pagination and Authentication Type
4. Can I import data from a dynamic URL?
Yes, you can import data from a dynamic URL using the parameter. In case the URL from which you import contains the current date and time, then you can fill this using the Current Date, Current Time and Current Date & Time parameter value. This will import data from URL which changes dynamically based on date.
5. Can I pass multiple parameters while importing data from feeds/URLs in Zoho Analytics?
Yes, you can pass multiple parameters/headers while importing data from a feed/URL in Zoho Analytics. Click the Add Parameter link available in the Import dialog under the Parameters section to add multiple parameters/headers.
6. Can I import data using Payload?
Yes, you can import data using Payload. You can send the raw payload data (like JSON, XML) in the body of the request to import data.
Follow the below steps to do this.
- Open the Import wizard.
- Provide the URL to import data from.
- Set the Method as Post.
- In the Body section, select the Custom checkbox.
- Select the Payload type. Supported types are:
- JSON
- XML
- Text
- In the Request body payload field, enter your payload data/value.
JSON Format
{" name":"sales",="" "password":"pa$$w0rd123"}
XML Format
xml version="1.0"?
Salespa$$w0rd123
- Click Next to proceed with the Import.
Import Data from a Secured Feeds/URL
1. Can import data from secured/authenticated URLs?
Yes, Zoho Analytics supports importing data from secured URLs. You can import data from the authenticated URL supporting the following authentication methods.
2. How do I import data from URL feeds authenticated via Basic HTTP Authentication?
3. How do I import data from URL feeds authenticated via OAuth 1 Authentication?
4. How do I import data from URL feeds authenticated via OAuth 2 Authentication?
5. How do I import data from URL feeds authenticated via AWS Signature?
6. How do I import data from URL feeds authenticated via Digest Authentication?
7. How do I import data from URL feeds authenticated via Hawk Authentication?
Import Settings
1. How do I set custom date format?
By default, Zoho Analytics tries to identify the date format of the given date column from the data provided, and display the same. If you find that to be incorrect or if Zoho Analytics had failed to recognize any date column, then you can set the date format in the Format of Date Column(s) option. This date format will be applied to all date columns in the data being imported.
You can also set different date formats for each date column. Click the Settings icon in the preview column header and select the Change Date Format option.
Now set the date format of the column.
To know more on how to construct a custom date format, refer to this link.
2. Can I map a column from my file with a column in Zoho Analytics table while importing?
Yes, you can map columns while importing. In the Data Preview of the Import Setting, a drop-down will list all the columns in the Zoho Analytics table. You can choose whether this is a new column or the data need to be mapped to an existing column in the Zoho Analytics table in this drop-down.
3. Can I Re-fetch/Schedule data import?
Zoho Analytics allows you to re-fetch data or schedule import only if,
- You have imported your data from the Web or FTP server
- Your data has a column header. If your data does not have a column header you will not be able to re-fetch or schedule an import.
To learn more about this refer Question No. 7.
4. Why do I see Warning Details in Import Summary?
Specifying a wrong data type for your column will generate errors on import. Zoho Analytics will handle the errors condition as you have set in On Import Errors option.
In case of such errors, the details of the same would be shown in the Import Summary dialog.
5. How do I set On Import Error option?
You can specify how Zoho Analytics should handle errors (in case an error occurs during import of data) in the Import settings dialog of the Import Wizard.
The following are the possible options:
- Set Empty Value for the Column (default) - Select this option to set empty value to the corresponding column value which had problems while importing.
- Skip Corresponding Rows - Select this option to skip the corresponding rows in which an error occurs while importing.
- Don't Import the data - Select this option to abort the import process, if any error occurs during importing.
In case any error occurs during import, the details of the same would be shown in the Import Summary dialog (refer to the below question) which would be shown on Import process completion.
6. Can I retain the relational data modeling from my source?
You cannot retain the relational data modeling from your source. However, Zoho Analytics allows you to auto-join tables.
While importing a new table into an existing Workspace, Zoho Analytics auto-identifies columns with the same column name and datatype and provides suggestions for lookup. You can create this lookup by following the steps in the below slide.
7. Can I schedule data import?
Yes, you can schedule your import. Zoho Analytics supports scheduling import when you have stored your data in a web URL or FTP Server. It is mandatory that your data has a column header.
Refer to this slide show to know how to import data.