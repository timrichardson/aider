Customizing a Pivot Table
Zoho Analytics provides extensive possibilities to customize the Pivot View. You can customize the various elements in the Pivot view (hide totals, wrap text in header, etc.,) based on your requirements.
General Settings
The General tab lists you all the range of settings to customize the pivot view.
Basic
The Basic tab helps you modify the Title, add a short Description about the data, and configure the settings for the Missing values.
Follow the below steps to customize the settings,
- Click the Settings icon on the top-right corner.
- The General Settings Tab will open.
- Under Basic tab, modify the settings as required.
Show Missing Values
Show missing values feature is used to display the in-between missing values in a Pivot. This can be applied on a Date or a Category column. When creating a Pivot, if a particular data point does not have any value, then the Pivot would skip displaying that data. With this option, you can choose to display the record even if a point does not contain a value.
- Columns: You can choose to display the filtered columns in the 'Columns' shelf by selecting/deselecting the check box. By default, this value will not be selected.
To learn more about missing values, refer the below section. - Rows: You can choose to display the filtered columns in the 'Rows' shelf by selecting/deselecting the check box. By default, this value will not be selected.
To learn more about missing values, refer the below section.
Let us say that you are the manager of a team and would like to view your employee`s attendance details every week. In case an employee is not available for a particular day, his data will not be available for that day. Our database looks as shown below.
Lets now create a pivot as shown in the below snapshot to view the number of employees present in the given week. To do that, drag and drop the Date and Employee Name column in the Rows shelf and Clock-in hours column in the Data shelf.
This Pivot does not contain any record of the employees who were not available (absent). To view the name of the employees who were not available for a particular day, you can enable show missing value function for the Employee Name column.
You can either right click on the column name and choose Show Missing Values or click Settings option on the toolbar.
In the settings tab that appears, Under the Show Missing Values section, click Choose Columns link next to For columns in the "Rows" shelf. You can choose the columns for which you wish to show the missing values.
The Pivot that is generated now, will contain the data of the employees who were absent.
In case you wish to view the details of the employees based on their location, we will be making a small change in the existing pivot. Drag and drop the Region column under the Rows shelf.
Our Pivot will look as shown in the below snapshot. If you take a closer look, you will notice that this might not be the best way to display the data as it displays the name of all employees across all locations.
In this case, you can choose to apply hierarchy function while listing missing values.
- Click Settings > Basic tab.
- Under Show Missing Values, check Apply hierarchy for missing values For Rows.
The Pivot will now look as shown below.
Layout
Zoho Analytics allows you to customize the layout of your Pivot Table.
You can edit the following details from the Layout tab:
Layout: You can customize how your data needs to be arranged in the Pivot Table. You can choose between the following layouts:
- Tabular Layout: This is the default layout of your Pivot Table where the columns dropped in the 'Rows' shelf will be arranged as separate columns in the Pivot Table.
- Repeat group label value in each row: In case, you wish to repeat the group label for each row, select this checkbox.
- Repeat group label value in each row: In case, you wish to repeat the group label for each row, select this checkbox.
- Compact Layout: This is a close-packed view of the Pivot Table where the rows dropped in the 'Rows' shelf will be grouped and arranged in a single column in your Pivot Table.
- Indent Level: You can change the indent spacing of the data displayed by choosing an Indent Level. By default, level 1 indent will be applied.
- Check Increase Font size for each higher group in Rows, if you want to increase the font size for higher-level groups in the Rows section.
- Tabular Layout: This is the default layout of your Pivot Table where the columns dropped in the 'Rows' shelf will be arranged as separate columns in the Pivot Table.
To learn more about Tabular and Compact layout, refer to the next section.
Display
This helps you specify what and how data needs to be displayed in the Pivot Table.
- Show row numbers: Displays the row numbers for the records in the pivot table. This option is disabled by default.
- Show Vertical Line between Each Column: Separates each column in the pivot table with a vertical line. This option is enabled by default. Removing vertical lines can be helpful while preparing financial statements.
- Show Horizontal Line between Each row: Separates each row in the pivot table with a horizontal line. This option is disabled by default.
- Show Expand/Collapse icons : Enabling this option helps view the data at different levels of granularity and also makes data navigation easier.
- Wrap Text in Column Headings: Enabling this option helps maintain readability and prevent headings from getting hidden.
- Column Alignment: To align column headers from Left, Center, and Right for improved readability
- Column Width : The Column Width enables you to set a specific width to columns in the pivot table. You can use the options available to set uniform, compact or varied widths across all columns in a pivot table.
- Compact: This option tightly packs the columns in the pivot table, thereby helping to save horizontal space and improve readability without the need to scroll sideways.
- Fit to Screen: This option adjusts column width to fit the table across the entire screen. In case of adding/removing columns, applying filters, etc in the future, the column width will always adapt to the screen size. The Fit to Screen option can also be applied to all pivot and summary views in the dashboard, by enabling the Fit the Pivot/Summary view to card width from the Settings menu in dashboard.
- Equal: This option allows you to uniformly resize all the columns to an equal width. Once selected, specify the required width (in pixel) in the provided field.
- Display 'Unknown' value as: You can specify a value that needs to be displayed in the place of null or empty values present in the underlying data of the pivot. By default, -No Value- will be displayed here.
- Sub Total Label: By default, Zoho Analytics will display the sub-group names in the row header. You can add a prefix or suffix to the Sub-total Label, or you can customize the label as needed.
Format
You can edit the column names and the display format used in the pivot table as needed.
- Click Settings > Format.
- Click the Label field to edit the respective column names.
- Click Format to change the format of the data columns. The options displayed in the format dialog will be based on the data type of the columns. Click here to learn more about Formatting data in Zoho Analytics.
Drill
The drill feature enables you to view data at varying levels of granularity, making it easier to compare different data segments.
The Drill Through action lets you navigate from a data point in one report to related reports for deeper insights. For example, from a Region-wise Sales report, you can drill through to a Product-wise Sales report to identify which products are driving sales in a specific region. Refer to Drill Through article to learn more.
Tabular and Compact Layout
Zoho Analytics allows you to visualize your Pivot Table in two layouts. The difference between the two layouts is the structure, i.e., the way in which the columns dropped in the Rows shelf are arranged in the Pivot Table. You can choose between the below two layouts:
- Tabular Layout
- Compact Layout
Tabular Layout (Default Layout)
The Tabular Layout is the default layout of your Pivot Table where the columns dropped in the Rows shelf will be arranged as separate columns in the Pivot Table.
Compact Layout
The Compact Layout is a close-packed view of the Pivot Table where the rows dropped in the Rows shelf will be grouped and arranged in a single column in your Pivot Table.
The columns dropped in the Rows shelf will be grouped and arranged in a single column with Row Labels as the column name. You can later change this column name by clicking the Edit icon that appears on mouse hover.
Show/Hide
By default, Zoho Analytics will display all the values in the columns added in the Columns field as a Pivot View column. You can choose to hide or display the required columns using the Show/Hide option.
Show/Hide Columns
Follow the below steps to show or hide columns.
- Open the Pivot View.
- Click the Show/Hide option in the toolbar.
- Select Columns.
- The Show/Hide Columns dialog will open.
- Expand to view all columns.
- Select the columns you want to be displayed, and unselect the columns that you want to be hidden.
- The Empty Columns checkbox allows you to show or hide the empty columns in the Pivot. Select this to display empty columns, and unselect this to hide empty columns.
Alternatively, you can also show or hide columns by following the below steps.
- Open the Pivot in Edit Design mode.
- Right-click the required cell and select Show/Hide Columns. Click one of the below values:
- Hide : This option is used to hide the selected column.
- Hide All : This option will be available if you have repetitive columns. Using this option will hide all the columns with the same column name.
- More - This option opens the Show/Hide Columns dialog.
Show/Hide Totals
In Zoho Analytics, by default, sub-totals of individual columns, and the grand total of all the rows and columns get automatically added and shown as part of the Pivot Table. Zoho Analytics also allows you to disable these totals when they are not required, or to change the totals' positions. You can hide the totals even when the records are expressed in Data as row format.
Follow the steps below to customize the sub-totals and the grand-totals in your pivot.
- Open the Pivot Table.
- Click the Show/Hide option in the toolbar or right-click the corresponding cell/column in the pivot table and select Show/Hide Totals > More... menu option
- The Show/Hide Total dialog will open with the following options.
- Sub-total - This lists the option to show or hide the Row and the column sub-totals.
- Rows - Select Right or Left to display the sub-total in the corresponding position. You can also choose to hide the row sub-total by selecting Hide.
- Columns - Select Bottom or Top to display the sub-total in the corresponding position. You can also choose to hide the column sub-total by selecting Hide.
- Grand-total - This lists the option to show or hide the Row and the column grand-totals.
- Rows - Select Right or Left to display the Grand-total in the corresponding position. You can also choose to hide the row Grand-total by selecting Hide.
- Columns - Select Bottom or Top to display the Grand-total in the corresponding position. You can also choose to hide the column Grand-total by selecting.
The below image shows the total sales and costs of different product categories for each quarter. The sub-total of sales and cost for each product category and the grand total are hidden.
Show Total As
In Zoho Analytics, by default, the summary function used to display the subtotals and the grand total will be the same as that of the summary function applied to the corresponding data column. You can customize this and apply other summary functions such as sum, average, min and max on the sub-total that is displayed.
To change this,
- Right-click anywhere on the Pivot table
- Select Show Total As and then, select the function that you wish to apply.
In our example, we have applied the average function. Shown below is the Pivot with the Average function applied to the Subtotal and Grand Total.
Please do note that the Show Total As feature is customizable for each data column.
Sorting a Pivot Table
In Zoho Analytics, by default, a pivot table data will be sorted in ascending order by the values of the columns from the source table that you assign to Row orientation in a Pivot Table. Zoho Analytics allows you to change this default sort order in lot of different ways. Below is a brief description of various ways to sort a Pivot Table.
Sorting a Pivot column by its values (by the values of the columns in Row shelf): This option allows you to sort Pivot Table column data in ascending or descending order by its actual values.
To sort a pivot table by its column values:
- Right-click the column header or on any cell of the corresponding pivot table column whose values has to be sorted.
- In the pop-up menu, select the required sort order and then By Column (column specific) option.
For example if a pivot table has Product category and Productcolumns in Row shelf (Row Orientation), initially the Product Categories and Products will be ordered alphabetically in ascending order. When corresponding columns are sorted in descending order as described above, Pivot data will be rearranged as shown in the screen shots below.
Sorting a Pivot Table column by its corresponding data values(by values of the column in Data shelf): This option allows you to sort Pivot Table columns based on data values corresponding to each pivot column value.
To sort a pivot table based on its data values:
- Right-click the data value column header or on any data value cell corresponding to a Pivot Table column value.
- In the pop up menu, select the required sort order and then select the column based on which you want to sort data values as shown below.
In the above example, when you right click Central region and select Sort Descending -> By Product Category, Sales values in Central region corresponding to Product Category column will be sorted in descending order as shown below.
When you select Sort Descending -> By Product, Sales values in Central region corresponding to Product column will be sorted in descending order as shown below.
Sorting Pivot Table columns by its corresponding summary values: This option allows you to sort Pivot Table columns based on summary values corresponding to pivot column values.
To sort a pivot table based on its summary values:
- Right-click the summary column's header.
- In the pop up menu, select the required sort order and then select the column based on which you want to sort summary values as shown below.
When you right click Summary Column and select Sort Descending -> By Product Category, Sales values in Summary column corresponding to Product Category column will be sorted in descending order as shown below.
When you select Sort Descending -> By Product, Sales values in Summary column corresponding to Product column will be sorted in descending order as shown below.
You can also sort rows by column values by clicking on the arrow icon() at the heading of the corresponding column. A down arrow indicates that the column is sorted in ascending order. An up arrow indicates the column is sorted in descending order.
Conditional Formatting
Conditional formatting helps apply custom formatting to the cells that meet a specific criteria. This is used to highlight and emphasize critical information such as deadlines, targets, goals achieved, stock levels, and task completion.
Zoho Analytics provides varied formatting options such as Font color, Background color, Custom text, and Icons. Conditional formatting can be applied based on the data values of the same or other columns used in the pivot view.
Applying Conditional Formatting
- Drag and drop the required columns into the respective shelves.
Right click the column and select Conditional Formatting from the drop-down menu.
Zoho Analytics allows you to apply conditional formatting based on the following options:
Note: Color Band and Icon Band options are applicable only for numerical data type.
Conditional Formatting - Rule Based
- You can format the data values based on the current selected column or choose another column from the Based on drop-drop menu.
- Specify the Conditions based on which the columns should be formatted. The conditions are listed based on the Data Type of the column.
- Specify the Value for the given condition.
- Choose the Format options to be used. Refer to the Format Options section to learn more.
- Click Add Condition to include more conditions. Specified conditions will be evaluated, and the corresponding formatting options will be applied to the data that meets the condition.
' - Click Ok.
Format Options
Format by Font color: This will apply the chosen color to data that meets the specified conditions.
Format by Background color: This will apply the chosen color to the background of the cells that meets the specified condition.
Add Text: This allows you to include Prefix or Suffix to the existing data value or change the existing data values with custom text using the Text Replacement option.
Add Icons: This helps provide a quick visual representation to indicate the increase or decrease in data trends and spot areas of excellence and areas needing improvement.
The following are the customization options for Icons,
- Choose the icon that is best suited to convey the information in the data. Click Icon color to choose the preferred color for the icon.
- You can choose to display the Values with Icon or Only the Icon.
- Choose the Icon Alignment, Align left or Align right. By default, the Place icon near the value is enabled.
Conditional Formatting - Color Band
Color Band feature allows you to apply a gradient of colors across your data range. This feature is useful to highlight the variation in data, such as showing a gradual increase or decrease in values.
- You can format the data values based on the current selected column or choose another column from the Based on drop-down menu.
Select the type of color band you want to apply from the Color Band Type drop-down.
Monochrome:
Monochrome color band type allows you to apply gradient using shades of a single color to represent the data range.
- Choose your preferred color.
- Click on the Reversed toggle button if you want to reverse the color gradient. This will invert the color intensity across your data range, with the lightest shade becoming the darkest and vice versa.
Gradient:
Gradient color band type allows you to create a smooth transition between two to three colors in your pivot table.
- You are provided with options to choose two to three colors for the gradient.
- Start color: This is applied to the minimum data values.
- End color: This is applied to the maximum data values.
- Middle color (Optional): Click on the + icon to add the third color. This is applied in the middle of the gradient.
- Adjust the position of the middle color using a slider that ranges from 0% to 100%.
- When setting up your gradient color band, you have the flexibility to delete any of the selected colors by clicking on Delete Colors.
- Merge Colors option enables you to blend two selected colors into a smooth unified gradient. Disabling this option gives you a separate gradient of each color.
Note: The Merge Color option is applicable only if two colors are selected. It is not available if a third color is added to the gradient.
- Choose your preferred color.
- The Auto MinMax checkbox is provided to automatically set the minimum and maximum values for the color band. Unchecking this checkbox allows you to set your own minimum and maximum values, giving you control over the range of values that the gradient covers.
- Click Ok to save your conditions.
Conditional Formatting - Icon Band
Icon Band feature allows you to represent your data with icons such as arrows, emojis, circles, hearts, stars, etc. This is useful to identify high and low values or performance indicators.
- You can format the data values based on the current selected column or choose another column from the Based on drop-down menu.
- You are provided with the options to choose two to five icons and their colors. The middle three icons are optional, and their positions can be adjusted.
- The position of the middle icons are adjusted using a range slider that spans from 0 to 100%.
Note: The ranges adjust automatically as you add or remove icons. - You can use the below format settings to adjust icon display options:
- Value With Icon: Displays both the data value and the corresponding icon.
- Icon Only: Displays only the icon value, without the data value.
- Icon Alignment:
- When the Value With Icon is selected, you can align the icon either to the left or right of the value. You can also check/uncheck the Place Icon near the Value checkbox to position the icon closer /farther to the corresponding value.
- When the Icon Only is selected, you can align the icon to the left, middle, or right within the cell.
- The Auto MinMax checkbox is provided to automatically set the minimum and maximum values for the icon band. Unchecking this checkbox allows you to set your own minimum and maximum values.
- Click Ok to save your conditions.
Applying Themes
Zoho Analytics allows you to customize the look and feel of your Pivot table using colorful and attractive themes. You can customize your Pivot Table using the options provided to suit your taste. Please do note that this option is available only as a part of the new charting library that was released recently.
Read the below steps to learn about changing the Pivot Theme.
- Open the Pivot Table
- Click the Themes button. The Themes dialog will open as shown below.
- You can select an appropriate theme to suit your needs and customize it using the options available. The Themes dialog allows you to select the,
- Theme Layout: You can choose a layout from the available set of seven layouts.
- Theme Color: Select a color that you wish to apply.
- Font: Select the font for the text in your Pivot.
- Zoom: You can Zoom in or Zoom out. This will increase or decrease the size of your Pivot Table.
- Row spacing: You can alter the row spacing using the predefined options available.
- As you choose the themes, the changes will be dynamically applied in the background.
- If you wish to undo the changes click Reset.
- If you want to reset the theme to the default theme click the Reset to default option.
- Save the Pivot Table.