Importing Data from Files
Often you would already have data locally stored in tabular file formats like CSV, XLS (Excel), JSON, Statistical file, and HTML files in your local drive or FTP. Zoho Analytics offers easy import and copy-paste options of such data for jump-starting your reporting and analysis. This section explains how to import data into Zoho Analytics.
Note: You can also import data stored in Web URL or Cloud Storage. To know how to import from these locations, refer to the Importing from Feeds and Importing from Cloud Storage sections.
Watch the below video to get a quick overview of importing data from files into Zoho Analytics.
- What are the file formats that can be imported into Zoho Analytics?
- What are the sources from which I can import data into Zoho Analytics using the files and feeds option?
- How do I import data from a CSV file into Zoho Analytics?
- How do I import data from Excel into Zoho Analytics?
- How do I import data from an HTML file into Zoho Analytics?
- How do I import data from JSON into Zoho Analytics?
- How do I import data from XML into Zoho Analytics?
- How do I import data from Statistical File into Zoho Analytics?
- How do I import data from Spatial Data File into Zoho Analytics?
- How do I import data from MS Access Database files into Zoho Analytics?
- How can I Import data from a Local File?
- How can I Import data from an FTP Server?
- How can I Import data by pasting data in Import wizard?
- How can I import data from an email attachment?
- Can I import data into an existing table?
- Can I import huge files into Zoho Analytics?
- How do I set custom date format?
- Can I map a column from my file into a column in Zoho Analytics table while importing?
- Can I re-fetch/schedule data import?
- Why do I see Warning Details in Import Summary?
- How do I set On Import Error options?
- Can I retain the relational data modeling from my source?
- Can I schedule importing data?
- Can I import files from my cloud storage?
- Can I import files stored in the Web?
1. What are the file formats that can be imported into Zoho Analytics?
Zoho Analytics supports importing data from the following sources.
2. What are the sources from which I can import data into Zoho Analytics using the Files and Feeds option?
Zoho Analytics allows you to import data from the following sources using the Files and Feeds option:
3. How do I import data from a CSV file into Zoho Analytics?
4. How do I import data from Excel into Zoho Analytics?
5. How do I import data from an HTML file into Zoho Analytics?
6. How do I import data from JSON into Zoho Analytics?
7. How do I import data from XML into Zoho Analytics?
8. How do I import data from Statistical File into Zoho Analytics?
9. How do I import data from Spatial File into Zoho Analytics?
10. How do I import data from MS Access Database files into Zoho Analytics?
11. How can I import data from a Local Drive?
12. How can I import data from an FTP Server?
13. How can I import data by pasting data into Import wizard?
14. How can I import data from an email attachment?
15. Can I import data into an existing table?
Yes, you can import data into an existing table. Follow the given steps to import data into the existing table.
- Open the table into which you want to import data.
- Click Import Data > Import Data into this Table. Import wizard to import data into that table will open.
- In the Import Your Data page, choose the data source from which you want to import.
- The rest of the steps varies based on the data source selected. Refer to the respective help sections to know more.
The rest of the steps are similar to Schedule Import.
16. Can I import huge files into Zoho Analytics?
Zoho Analytics has the following restrictions on the size of data import. You can upload a maximum of 1,000,000 rows and the file size should not exceed 100 MB.
However, you can upload huge CSV files using the Zoho Databridge. This is a packaged downloadable tool installable in your machine. You can also schedule import periodically.
17. How do I set custom date format?
By default, Zoho Analytics tries to identify the date format of the given date column from the data provided and display the same. If you find that to be incorrect, or if Zoho Analytics had failed to recognize any date column, then you can set the date format in the Format of Date Column(s) option. This date format will be applied to all date columns in the data being imported.
You can also set different date formats for each date column. Click the Settings icon in the preview column header and select the Change Date Format option.
Now set the date format of the column.
To know more on how to construct custom date format, refer to this link.
18. Can I map a column from my file with a column in Zoho Analytics table while importing?
Yes, you can map columns while importing. In the Data Preview of the Import Setting, a drop-down will list all the columns in the Zoho Analytics table. You can choose whether this is a new column, or if the file's column needs to be mapped to an existing column in the Zoho Analytics table in this drop-down.
19. Can I Re-fetch/Schedule data import?
Zoho Analytics allows you to re-fetch data or schedule import only if,
- You have imported your data from the Web or FTP server
- Your data has a column header. If your data does not have a column header you will not be able to re-fetch or schedule an import.
To learn more about this refer Question No.16.
20. Why do I see Warning Details in Import Summary?
Specifying a wrong data type for your column will generate errors on import. Zoho Analytics will handle the error condition as you have set in On Import Errors option.
In case of such errors, the details of the same would be shown in the Import Summary dialog.
21. How do I set On Import Error option?
You could specify how Zoho Analytics should handle errors condition (in case it occurs) in the Import settings dialog of Import Wizard.
The following are the possible options:
- Set Empty Value for the Column (default) - Select this option to set empty value to the corresponding column value which had problems while importing.
- Skip Corresponding Rows - Select this option to skip the corresponding rows in which an error occurs while importing.
- Don't Import the data - Select this option to abort the import process, if any error occurs during importing.
In case any error occurs during import, the details of the same would be shown in the Import Summary dialog (refer to the below question) which would be shown on Import process completion.
22. Can I retain the relational data modeling from my source?
You cannot retain the relational data modeling from your source. However, Zoho Analytics allows you to auto join tables.
While importing a new table into an existing database, Zoho Analytics auto identifies columns with the same column name and datatype and provides suggestions for lookup.
23. Can I schedule data import?
Yes, you can schedule your import. Zoho Analytics supports scheduling import when you have stored your data in a web URL or FTP Server. It is mandatory that your data has a column header.
Refer the slide to know how to import data.
24. Can I import files from my cloud storage?
Yes, you can import files from cloud storage. Zoho Analytics allows you to import data from CSV, Excel (XLS and XLSX), JSON, HTML and zipped files stored in different Cloud Storage/Drive such as Zoho Docs, Google Drive, Dropbox, Box and OneDrive.
Refer to the Importing Data from Cloud Storage/Drive section to know more on this.
25. Can I import files stored in the Web?
Yes, you can import files stored in the Web. Zoho Analytics allows you to import data from CSV, Excel (XLS and XLSX), JSON, HTML, MS Access Database files data stored in web.
Refer to the Importing Data from Feeds section to know more on this.