Working with Tables
- Searching
- Filtering
- Sorting
- Find and Replace
- Split Column
- Show/Hide Columns
- Freeze Columns
- Reorder and Resize Columns
- Changing Column Properties
- Analyze this Column
- Copying a Table
- Exporting a Table
- Sharing a Table
- Publishing a Table
Zoho Analytics offers a range of interactive options to work with a table. Some of the options include Filter, Sort, Format, Find and Replace values, Freeze and Show/Hide Columns. Zoho Analytics also allows to Export, Share and Publish a table.
Note:
- These options will be enabled only to users who have been provided with appropriate permissions during sharing by the Administrator. Refer to the topic Sharing and Collaboration to know more about sharing.
Searching
Zoho Analytics allows you to quickly search for specific records within a large set of data. The Search box on the toolbar can be used to locate records in a table that matches the keyword that you specify.
To search for records, type the keyword that you want to search for in the search box and click on the magnifying glass icon ( ) next to the search box. All the records containing the specified keyword will be filtered and displayed as shown below. Note that the search operation will search across data contained in all columns of the table.
Filtering
Zoho Analytics provides a Filter option to easily filter records in your table based on criteria that you specify. You can also apply filters on multiple columns at a time.
To filter data, click Filter. The filter panel will open.
Depending on the data type of the column, Zoho Analytics offers various filtering options like filter based on specific numeric ranges, date ranges, individual values, partial match etc. You will also find some filter panel option to apply the filter.
The following is a brief description of various options provided in the Filter Pane when you apply filters.
- Hide: Click this option to hide filter pane. You can also use icon at the column header to hide/show filter pane.
- Clear: Click this option to remove all the filters applied.
- Save/Save as: Click this option and type the name in the dialog box that appears to save your filter for later/repeated use. How to save a filter for repeated usage is discussed below.
- Delete Rows: Select this option to permanently delete the filtered rows from the table.
Sorting
Zoho Analytics allows you to rearrange rows in a table by sorting values in one or more of its columns. You can sort a column numerically, alphabetically or by date depending on its data type. For example, you can sort a column of dates by their date order, while a column of numbers can be sorted numerically.
To sort the columns, click Sort and then select the required options. The sort options available in Zoho Analytics are:
- Sort Ascending - Sorts text data in ascending alphabetical order (A to Z), numbers from smallest to largest (0-9) and dates from oldest to latest.
- Sort Descending - Sorts text data in descending alphabetical order (Z to A), numbers from largest to smallest(9-0) and dates from latest to oldest.
- Remove Sort - Removes sorting.
You can also sort the columns using the arrow icon in the column header.
Find and Replace
Find and replace option can help you to locate a value in a column and replace it with another value. This feature can be very useful especially when you are working with large sets of data and have the need to quickly correct/rectify issues in your data set.
Note:
- This option will be enabled only to users who have been provided Write permission by the Administrator.
To find and replace data click More > Find and Replace. The Find and Replace dialog will open.
Specify the following details to replace data.
- Column Name - Select the column where you want to find and replace data.
- Find - Specify the data to be searched in this field.
- Replace With - Specify the data to replace in this field.
- Bulk Update: Select this option if you want to replace all the values in the column with the value specified in the Replace With text box. On selecting this option the Find what text box will be disabled.
- Match entire cell: Select this option to limit your search results only to cells whose entire contents match with the Find What value that you have provided. This option is selected by default for number and currency type columns.
- Do not replace null values: Select this option when you do not want to replace existing null values in the column with the value specified in Replace With. This is applicable only when you use the Bulk Update option.
Couple of Points to Note:
- Find & Replace operation is Case Sensitive i.e., upper and lower letters are not considered as equivalent.
- To find a cell with empty/null value or to replace a cell value with an empty/null value you have leave the corresponding boxes empty.
- Currency (Ex :-$) and Percentage(%) symbols cannot be used in Find & Replace fields for currency and percentage data types.
- Find & Replace will be applied over Filtered data, if you have already applied a Filter on the table
Split a Column
Zoho Analytics allows you to split a column into multiple columns. This will be useful to split concatenated data value into individual columns for better analysis.
To split a column you need to specify a column separator to indicate how the column should be split. This can be a string not exceeding 10 characters. Split columns will be created as a Formula column of string data type. You can split a column into ten individual columns at a time.
The Split Column can be applied over columns with the following data type:
- Text
- Multiline
- URL
Refer to the following video to know how to split a column.
Show/Hide Columns
Zoho Analytics let you show or hide columns in the table. To show or hide columns, click More > Show/Hide Column. The Show/Hide/Reorder dialog will open. Ensure that only column that you want to show are selected. You can rearrange the column order using the arrow icons.
Freeze Column
Freeze Column option allows you to keep specific columns always visible in the table even when you scroll horizontally across the screen. For example, you can freeze columns that identify the records (Ex:- Customer Name, Product ID) in a table so that you can keep track of a record that you are looking, even when you scroll off to the right-most column in the table. You can easily freeze columns by clicking More > Freeze Column.
Reorder and Resize Columns
Zoho Analytics allows you to rearrange the order of columns in a table using drag and drop.
Drag the column into the required position.
Change Column Properties
Each column has a set of properties like the format, name, data type etc. Column Properties option in the toolbar provides you with options to change these properties any time you want after creating a column.
Format a Column
Choosing the right format is crucial for both analysis and interpretation of the data. Zoho Analytics provides numerous options to format a column based on the data type. This helps ensure all the data points in the column have the same consistent format.
To format column click Column Properties > Format Column.
Note: Option to format columns will be disabled for shared users.
Formatting options provided in the dialog box changes based on the data type of the selected column. The following table gives a brief description of these options.
| Numeric Data Type: | |
| OPTION | DESCRIPTION |
| Alignment | This option can be used to horizontally align the value in the cell. Possible values are left , right and center. |
| Currency Symbol | This option enables you to choose the type of currency symbol displayed. You can select the currency symbol you want from the wide variety of symbols available in the drop down list. This option will be enabled for currency type columns. |
| Units | This option enables you to format the unit value in thousands (K), millions (M) and billions (B).
|
| Decimal Places | You can use this option to set the number of decimal places to display for decimal, currency and percentage columns. |
| Negative Number Display | This option allows you to specify how negative numbers are to be displayed Options available are:
|
| Separator | This section allows you to pick the decimal and thousand separators to be used and where to add them. Apply User Locale Settings - Select this option to use separators based on the locale settings of the user. For example, in US locale a comma will be used for a thousand separator and in case of German locale a dot will be used. The following options are used to specify the decimal and thousand separators to be used. These options will be disabled when you have selected the Apply User Locale Settings mentioned above.
Display Format - Select the format to place the thousand separators. Available options are:
|
| Date Data Type: | |
| OPTION | DESCRIPTION |
| Alignment | This option can be used to horizontally align date in the cell. Possible values are left, right and center. |
| Choose Date Format | This option allows you to pick the date format you want, for displaying dates values, from the given list. Enter Your Date Format: Zoho Analytics provides this option to allow you to specify a custom date format, if the required format is not available as part of the default list provided. Refer here to know how to construct custom date format string. |
| Duration Data Type: | |
| OPTION | DESCRIPTION |
| Alignment | This option can be used to align the value in the cell horizontally. Possible values are Left, Right and Center. |
| Choose Duration Format | This option allows you to pick the duration format in which you want to display the duration format. Enter Your Duration Format: In case the required format is not available as part of the default list. You can enter the custom format in this field. Refer here to know how to construct a custom duration format string. |
| String/Category Data Type: | |
| OPTION | DESCRIPTION |
| Alignment | This option can be used to horizontally align the text in the cell. Possible values are left, right and center. |
| URL Data Type | |
| Alignment | This option can be used to horizontally align the text in the cell. Possible values are left, right and center. |
| Alternate Text | This option allows you to provide a substitute reader-friendly text that will be shown instead of the actual URL. |
| Image | You can convert the URL links pointing to images in your Zoho Analytics table to the corresponding images. Learn more. |
Note:
- Sorting - When you sort the URL data type column in a table, sorting will be done based on the actual URLs in the column.
- Copy and Paste - When you copy and paste the Alternate text and Image in a column, the actual URL corresponding to it will be pasted.
- Exporting - When a view with Alternate Text is exported, the view will be exported with the actual URLs.
Dynamic URLs
Zoho Analytics allows you to associate or hyperlink a column of Text (string) data type with a column of URL data type. This is useful for creating dynamic hyperlinks to records such as client or lead details, help desk tickets, or project information. You can also associate image URL with the text column.
Follow the below steps to format the column,
- Right-click the Plain text column (a column whose data type is plain text) and choose Format Column from the drop-down menu.
- Select the Alignment of the text column. Available options are left, right, and center.
- Choose the column to hyperlink from the Associate URL drop-down menu.
- In some cases, you might want to display the image alongside the data and hyperlink it to specific records, such as displaying a product image with a link to access its details. Since image addresses are imported as a URL data type in Zoho Analytics, select the same column (Product Image) from the Associate Image drop-down menu that you used for the Associate URL field.
- Customize the Image Position as needed. Available options are left, right, center, bottom, and top. The Auto option is selected by default.
- Choose the Image dimension or specify a custom Image Dimension.
- Click Ok.
Note:
- The Associate URL and Associate Image configurations cannot be changed in the report settings.
- Association is not supported for Sankey, Sunburst, table and Web charts.
- The associated details will be displayed on hover for charts.
Conditional Formatting
Conditional formatting feature allows you to highlight cells in a column with different background and font colors based on a condition. You have to specify the required conditions/criteria for formatting. When data in a cell meets the condition, Zoho Analytics applies the corresponding formatting style that you have specified. Conditional formatting is currently supported in Tables, Tabular Views and Query Tables.
To apply conditional formatting:
- Select the column (by clicking the header) on whose cells you want to apply conditional formatting.
- Either right click to get the pop-up menu or invoke Column Properties option in the toolbar.
In the menu, select Conditional Formatting option a shown below.
- A dialog box appears with options for specifying the conditions and selecting colors for font and background.
- Click the drop down arrow under Condition header and select the type of the condition that you want to apply.
Type the matching value that you want to use for the condition in the Value text box.
- Select the required colors for the font and background.
- You can add any number of conditions using +Add Another Rule option at the bottom of the dialog box.
- Click OK after you have added all the conditions.
All the cells that meets the criteria will be formatted accordingly.
Note: Conditional Formatting option will be disabled for shared users.
Set Chart Drill Down Path
Zoho Analytics allows you to drill down on your chart, enabling you to do powerful exploratory analytics. With this, You can click on any point in the chart and visualize the underlying data points as a new chart.
You need to configure the drill down path for any given column in the table/query table. For Date columns, Zoho Analytics will set a default path. You can change this as needed. Once the path is configured whenever you use this column in the chart, the corresponding drill path will be followed on drill down.
Follow the steps given below to define the drill down path for a column in a table.
- Open the table over which you want to create the chart.
- Click the corresponding column to drill down and then select Set Drill Down path.
- The Drill Down Path Settings dialog will open. Select the next column to drill down (the next jump) from the current column using the drop box.
- Click OK to set the path.
When you use the column (for which the drill down path has been defined) in a chart, then clicking its corresponding data point will drill down to the next level based on the path defined.
The following screenshot illustrates a drill down path set for a text column "Product Category".
Renaming a Column
You can easily change the column's name by double-clicking the column header. You can also rename by clicking Column Properties > Rename Column or by clicking the edit icon in the column header.
Note: Rename Column option will be disabled for shared users.
Change DataType of a Column
After creating a table, it is common for you to feel the need to change an already existing column's data type. Let us suppose you initially defined a column to hold text data, you realize later that it actually contains numeric data. In such cases, Zoho Analytics provides you with an option to change the columns data type without losing data in it. However, when changing a column's data type, all the data existing in the column must be compatible with the new data type.
To change data type, click Column Properties > Change Data Type.
- Change Datatype dialog box lists
- Click OK. Data type of the column will be modified.
Note:
- Remember that you cannot change the data type of a lookup column. You have to remove its lookup reference before changing the data type.
- This option will be disabled for shared users.
Changing a Column to Lookup
Lookup column relationships in Zoho Analytics are similar to Foreign key relationships in Relational Database. A lookup column is a type of column whose values will be referenced from a column in another table in the same workspace i.e., it can be used to cross-reference tables in a workspace. Refer to the topics Relational Data Modeling and Joining Tables to know more about lookup column.
Zoho Analytics provides you with an option to change a column to a lookup column. To change a column to a Lookup column:
- Open the required table from the workspace.
- Select the column that you want to change to a lookup column.
- Select More > Change to Lookup Column option on the toolbar or right click on the column and choose Change to Lookup Column option.
The Change to Lookup Column dialog box will open as shown below with Column to Lookup option which lists all the tables and their columns in the workspace as drop-down list.
Note: Change to Lookup column option will be disabled for shared users.
Analyze Column
Zoho Analytics can automatically analyze your column's data and create sample reports by picking the meaningful metrics. You can get started with these reports or modify them or create your own. To analyze your column and create reports.
- Select a column by clicking on its header and right click on the header.
- In the right click pop-up menu select Analyze Column option as shown below.
- On successful completion of analysis, tables reports will be generated.
Note:
- Analyze Column option will be disabled for shared users of the workspace.
Copying a Table
Zoho Analytics allows you to save a copy of a table in your workspace. On copying, all formatting, formulas etc., will be retained in the new table too.
Follow the steps given below to copy a table.
- Open the table you want to copy.
- Save As icon will appear when you mouse-over on the title of the table. Click this to open the Save As dialog.
- Specify a name to the new table in the Name field.
- Select the folder to save the new table in Save in folder drop-down.
- The Copy with Data option allows you to choose whether to copy the table with or without data.
- Select this to backup the data. By default, this will be selected.
- Unselect this to copy the table design, where you can import similar data.
e.g., you have a sales table for last year and want to create a new table for the current year. You can copy the table design and import the current year data instead of creating from scratch.
- The Retain Lookup option allows you to choose whether to retain the lookup columns defined in the original table.
- Click OK. The table will be copied as you have set.
Exporting a Table
Zoho Analytics allows you to export tables that you have into various file formats like CSV, PDF, XLS or HTML files.
To export a table:
- Open the table that you would like to export.
- Select Export in the toolbar.
- Select one of the five export format options:
- CSV -Exports the table's data as a Comma Separated Value (CSV) file.
- PDF- Exports the table's data in Portable Document Format (PDF) file format.
- HTML - Exports the table's data in HTML file format.
- Excel (XLS)- Exports table as a Excel file.
In the Export Settings window that opens, set the required options and then click Export button at the bottom to export.
Sharing a Table
In Zoho Analytics you can easily share your table for other users access. You can also set specific permissions on the shared tables, so that the users would be allowed to do only permitted actions when they access the table. The various share options are provided under the Share menu in the toolbar.
Refer to the topic Sharing and Collaboration to know how to share a table.
Note: Share option will be enabled only to users who have been provided that permission during sharing by the Administrator.
Publishing a Table
Zoho Analytics allows you to publish/embed tables into your websites/web pages or as iGoogle Gadgets or as easy to access URLs. Zoho Analytics also allows you to control the access privileges and permissions provided to the users who access the table.
Refer to the topic Publishing Options to know how to publish a table.
Note: This option will be enabled only to Administrator and Workspace Owners of the workspace.