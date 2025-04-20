Data Formatting
Zoho Analytics offers various options to format the data in your columns. This allows you to standardize the data in your table, thereby enabling easy interpretation and analysis.
The Data Formatting options selected for the data values in your columns are applied across all visualizations in Zoho Analytics.
Let us now see an example.
In the below image the data in the 'Sales' column are not formatted. This can be a major step back while analyzing a large amount of data.
Let us now create a report using this data. We are going to create a report to show the total sales done in each month.
In the above chart, the data labels with extended decimal values make it difficult to interpret the chart. This is where data formatting comes in handy.
Let us now see how to resolve this issue.
- Open the table.
- Right-click the Sales column and select Format Column
- In the format column dialog that appears, choose '2' from the drop-down that is available next to Decimal Places. This will limit the units after the decimal point to two.
Apart from decimal places, there are various other options that you can use to customize your data. Also, please do note that the formatting options in this dialog will change based on the data type of the column. Click here to learn more.
- Click OK.
Now, this is how the report will look like.
Note:
- Option to format columns will be disabled for shared users.
As mentioned earlier, the formatting options provided in the dialog box changes based on the data type of the selected column. The following table gives a brief description of these options.
| Numeric Data Type | |
| Option | Description |
| Alignment | This option can be used to horizontally align the value in the cell. Possible options are Left, Right and Center. |
| Separator | This option allows you to pick a decimal and thousand separators to be used. Apply User Locale Settings - You can select this option to use separators based on the locale settings of the user. For example, in US locale a comma will be used for a thousand separator and in case of German locale a dot will be used. Thousand - This option can be used to select the type of thousand separator. This option will be enabled for a number and decimal type columns. This option will be disabled when you have chosen. Apply User Locale Settings mentioned above. Available options include: Comma, Dot, Space and Single Quote Decimal - This option can be used to select the type of decimal separator. This option will be available only for decimal, currency and percentage columns. Also, this option will be disabled when you have chosen. Apply User Locale Settings mentioned above. Available options include Dot and Comma. |
| Currency Symbol | This option enables you to choose the type of currency symbol displayed. You can select the currency symbol you want from the wide variety of symbols available in the drop-down list. This option will be enabled for currency type columns. |
| Negative Number Display | This options allows you to specify how negative numbers are to be displayed Options available are:
|
| Decimal Places | You can use this option to set the number of decimal places to display for decimal, currency and percentage columns. |
| Date Data Type | |
| Alignment | This option can be used to horizontally align date value in the cell. Possible options are Left, Right and Center. |
| Choose Date Format | This option allows you to pick the date format you want, for displaying dates values, from the given list. Enter Your Date Format: Zoho Analytics provides this option to allow you to specify a custom date format if the required format is not available as part of the default list provided. Refer here to know how to construct custom date format string. |
| Duration Data Type | |
| Alignment | This option can be used to horizontally align duration value in the cell. Possible options are Left, Right and Center. |
| Choose Duration Format | This option allows you to pick the duration format you want, for displaying duration values, from the given list. Enter Your Duration Format: Zoho Analytics provides this option to allow you to specify a custom duration format if the required format is not available as part of the default list provided. Refer here to know how to construct custom duration format string. |
| String/Category Data Type | |
| Alignment | This option can be used to horizontally align the text in the cell. Possible options are Left, Right and Center. |
| Associate Image/ URL | This option can be used to hyperlink a column of Text (string) data type with a column of URL data type. Refer to Dynamic URLs section to learn more. |
| URL Data Type | |
| Alignment | This option can be used to horizontally align the text in the cell. Possible options are Left, Right and Center. |
| Alternate Text | This option allows you to provide a substitute reader-friendly text that will be shown instead of the actual URL. |
| Image | You can convert the URL links pointing to images in your Zoho Analytics table to the corresponding images. Learn more. |
| Geo Location Data Type | |
| Alignment | This option can be used to horizontally align the text in the cell. Possible options are Left, Right and Center. |
| Display Format (latitude and longitude) | This option allows you to choose the format in which the data should be displayed. Decimal
Degrees Minutes Seconds (DMS)
|
Points to be noted on the behavior of the Alternate text (for URL data type columns) feature in various scenarios
- Sorting - When you sort the URL data type column in a table, sorting will be done based on the actual URLs in the column.
- Copy and Paste - When you copy and paste the Alternate text and Image in a column, the actual URL corresponding to it will be pasted.
- Exporting - When a view with Alternate Text is exported, the view will be exported with the actual URLs.