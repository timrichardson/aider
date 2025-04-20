Creating a New Table
- Create Table by Importing data from Files & Feeds
- Create Table by Importing data from Cloud Storage
- Design a New Table from Scratch
- Enter Data Right Away
Zoho Analytics provides different options to create a table to store your tabular data. As already discussed, once you create a workspace you can create any number of tables within it.
When you create a table in a workspace using any of the options provided, you need to provide a name which is mandatory and it should be unique in that workspace. You can optionally provide a description about the table.
Click the Create in the right top corner of the workspace or every report/table in the workspace and then choose New Table/Import Data. On clicking, various options to create a table will be listed which are discussed below.
Create Table by Importing data from Files & Feeds
Often you would already have data locally stored in tabular file formats like CSV, TSV, XLS & XLSX (Excel), XML, JSON and HTML files. The data in such formats could also be available as a URL or Web feed. You would like to import or copy and paste such data into Zoho Analytics to jumpstart your analysis and reporting.
The following video shows how to create a table by importing the data from files that you have stored locally.
You can read detailed step-by-step instruction on how to create a table by importing data from files and importing data from feeds.
Create Table by Importing data from Cloud Storage
Zoho Analytics also allows you to import data different Cloud Storage/Drive such as Zoho Docs, Google Drive, Dropbox, Box and OneDrive, where you have stored your data in the CSV, Excel (XLS and XLSX), JSON, HTML and zip files.
To know how to import data from a cloud storage, refer here.
Design a New Table from scratch
Use this option if you would like to create a new table from scratch, by defining the columns to be present along with its properties (like type, default value etc.,). You might add data subsequently into this table or import data from an external file into this table.
The following video show how to create a table from scratch.
The following list explains the fields to be filled while designing a table:
- Column Name: Provide the name of the column. Name should be unique in a table.
- Data Type (Column Type): Choose the data type/column type of the column.
- Mandatory: If the column should have a mandatory value and cannot be empty, set this value as Yes. If not, set this to No.
- Default: Provide any default value that has to be present in the column, incase no data is entered. Refer to the specific data type document to know about the possible default values that could be provided for each column type.
- Lookup column: In case this column is of type Looked Up column, where it refers (or lookup) to a column in another table, then you need to choose the column to be looked up from the corresponding table as value to this column. Lookup columns are useful to relate two tables in a workspace and thus enabling you to create reports combining data from columns across the related tables (Refer Auto Joining Tables for Reporting). The Lookup column option is also the way for creating a workspace which is relational. Read more about Lookup Column.
- Formula: You can add a formula only after saving the table once. After saving the table once you will see an Add Formula link in this column to add a formula column. Refer to Creating Formula Columns document.
- Description: Provide a description to explain the purpose of the corresponding column.
Once you have added the necessary columns in the table, click Save in the toolbar. Provide a name and description for the table and click OK to save the table.
Upon saving, the Edit Design page will get segmented into the below sections:
- Columns: You can view your data table structure from the Columns section. From here, you can modify your table structure, and export your data table.
- Lookups: You can get a unified view of all the lookup relationships available for the table from the Lookups page. You can also create new lookups from here by clicking the Add Lookup link.
- Formulas: You can get a unified view of all the formula columns and aggregate formulas available for the table from the Formulas section. You can also add new formulas and aggregate formulas from here using the Add Formula Column and Add Aggregate Formula link.
Enter Data Right Away
If you are a Microsoft Excel or spreadsheet user who would like to first enter the data into the tables and then worry about naming the columns or formatting them, then this is the option that you have to choose.
Refer the following video to know how to create a table by directly entering data into it.
In the sheet, you can start entering the data that you wish to add under the respective columns named Column1, Column2 etc., You can also rename the column headers by double-clicking on them and providing a name. As mentioned already, do ensure that column names are unique in a table.
Once you are done with your data entry, click on the Save button in the toolbar. This will prompt the Save dialog where you need to provide the name of the table (mandatory) and description (optional). The new table will be created with the given name, including the newly added data and columns.
Note:
- Anytime you can rename a table by clicking on the Edit icon seen in the top-left corner of the tab in which the table is displayed. The edit icon will be visible only when you mouse over the tab. Clicking on the icon, the table name will become editable. You can modify the name and press the Enter key to save the table with the new name.