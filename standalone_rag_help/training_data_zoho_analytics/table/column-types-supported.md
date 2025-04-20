Data/Column Types in Zoho Analytics
Data Type/Column Type of a column in a Table defines the nature of values a column could contain and the operations that could be done over the same. Eg., an Age column could be "Positive Number" type. This column can contain only positive numbers and you could apply arithmetic operations over the same.
The data type of a column also determines the formatting options that are possible for displaying the values in the column in various reports created in Zoho Analytics. To learn about changing the data type of a column, refer to this document.
Zoho Analytics supports the following data types (column types) currently.
Text | |
| Data Type | Description |
| Plain Text | Holds a line of simple text that contains less than 100 characters |
| Multi Line Text | Holds multiple lines of text. This data type can hold text of more than 100 characters |
| Holds an Email Address | |
| URL | Holds a clickable Hyperlink / Web URL address. eg., http://analytics.zoho.com |
Numeric | |
| Auto Number | Holds auto generated incremental numeric values, which are unique. This would be helpful when you need to have a unique identifier associated to each row/record in the table. Auto Number column value starts with 1 and each new value will be incremented by 1. Auto Number values will always be unique |
| Number | Holds an integer value (both positive and negative values) |
| Positive Number | Holds only positive integer values |
| Decimal Number | Holds decimal values (both positive and negative) |
| Currency | Holds a currency value in different country denominations |
| Percentage | Holds a percentage value |
Geo Location | |
| Continent | Holds the names of continents or their codes. |
| Country | Holds the names of countries or their codes (Alpha-2 code and Alpha-3 code). |
| State/Province | Holds the names of state or province. |
| County | Holds the names of counties. |
| District | Holds the names of districts. |
| City | Holds the names of cities. |
| Zip Code | Holds the postal code of the location or place |
| Airport | Holds the IATA's 3 letter unique code |
| Latitude | Holds the latitude of a location |
| Longitude | Holds the longitude of a location |
Others | |
| Date | Holds Date and Time value |
| Duration | Holds time duration value |
| Decision Box | Holds a binary value eg., Yes/No, True/False, On/Off |
| Looked Up Column | Refers to a column value in another table. Helps to relate two tables. Click to know How to create a Lookup Column. |
Formatting Columns
Zoho Analytics offers options to change the format of a column like an alignment, decimal places, date formats, currency symbol etc., depending on its data type. Using these options you can choose how you would like to have your column data displayed in your table.
Marking Columns as Personally Identifiable Information
Zoho Analytics allows you to mark columns as Personally Identifiable Information (PII). This could be any information that could potentially identify an individual, for example. Name, Email, Job role and Company name etc. When a column is marked as PII, additional care will be taken in handling such data. The data will be encrypted and saved in our servers. The below-animated image shows how to mark a column as PII.
Alternatively, you can also click the Edit Design button in the toolbar and change the value of the corresponding Column Name to 'Yes' under the Is Personal Data? column.