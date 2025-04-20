Creating A Summary View
A Summary View allows you to dynamically summarize large amounts of data for easy analysis and visualization. You can transform data in table(s) into interactive and meaningful summaries easily, by using the intuitive drag and drop interface of Zoho Analytics.
Creating a Summary View
Follow the below steps to create a summary view:
- Open the Workspace in which you wish to create a summary view.
- Click Create button in the top left corner of the database and select Summary View.
- Select the base table on which you wish to create the summary view.
- Click OK.
Alternatively, you can also create a new summary view by opening the corresponding table on which you want to create the view and then click New icon > New Summary View option in the toolbar.
The summary view designer looks as shown below.
On the left hand side is the Column pane, listing all the columns available in the table. On the right hand side is the Design Area with shelves to drop the columns and a Preview area below to preview the report that is created.
You should drag and drop the required columns listed in the column list pane into the respective shelves in order to create a summary view. You can also select the check box adjacent to each column listed to auto place the columns into the appropriate shelves.
- Group by shelf: The columns dropped in this shelf are grouped based on the unique values present in the column
- The Summarize shelf: The data in the columns dropped in this shelf will be summarized based on the summary functions selected
Example: Let us see how to create a simple summary view to summarize the sales of the top 10 products based on the profit obtained. We will be creating this Summary View on the Sales Table (shown below).
The following is the Summary View that we are going to create.
Drag and drop the following columns in the summary tab:
- Group by shelf - Product Category, Product
- Summarize shelf - Sales
The following tables list all the functions along with the description of their functionality that is applicable for Group by shelf.
String Data Type:
| Function | Description |
| Actual Values | All the distinct values in the column will be listed. |
Date Data Type - Actual values:
| Function | Description |
| Year | Returns all distinct year values present in the column. E.g.,2007, 2010 |
| Quarter & Year | Returns all distinct quarter values present in the column. E.g., Q1 2010 |
| Month & Year | Returns all distinct month values present in the column. E.g., March 2010 |
| Week & Year | Returns all distinct week values present in the column. E.g; W1 2010 |
| Full Year | Returns all distinct dates present in the column. E.g., 1/1/2011 |
| Date & Time | Returns all distinct date and time present in the column. E.g. 01/12/2010 00:10:07 hrs. |
Date Data Type - Seasonal Value:
| Function | Description |
| Quarter | Identifies seasonal trends based on quarter across all years. E.g., Q1, Q2. |
| Month | Identifies seasonal trends based on months across all years. E.g., January, February. |
| Week | Identifies seasonal trends based on weeks across all years. E.g., Week 1, Week 2. |
| Week Day | Identifies seasonal trends based on week day across all years. E.g., Sunday, Monday. |
| Day of Month | Identifies seasonal trends based on day of the month across all dates. E.g., 1 to 31. |
| Hour of Day | Identifies trend across hours in a day. E.g., 0 to 23hrs. |
Numeric and Currency Data Types:
| Function | Description |
| Dimension | Treats the values in the column as a textual (categorical/dimensional) value. Returns each distinct value present as a text value. |
| Range | Groups the entire range of numeric values present in the column into multiple ranges. E.g., 0 to 100, 101 to 250 etc., |
You can apply functions such as sum, max, min, count etc on the columns dropped in the summarize shelf. The following tables list all the functions along with the description of their functionality that are applicable for Summarize shelf.
In the above example we have dropped the Sales and Profit column and selected Sum.
String Data Type:
| Function | Description |
| Count | Returns the number of values in the column. |
| Distinct Count | Returns the number of distinct values in the column. |
Date Data Types:
| Function | Description |
| Count | Returns the number of date values in the column. |
| Distinct Count | Returns the number of distinct date values in the column. |
Numeric and Currency Data Types:
| Function | Description |
| Sum | Returns the sum of all the values in the column. |
| Maximum [Max] | Returns the maximum value in the column. |
| Minimum [Min] | Returns the minimum value in the column. |
| Average [Avg] | Returns Arithmetic mean of all the values in the specified column. |
| Standard Deviation | Returns the standard deviation of the column. |
| Variance | Returns the variance of the column. |
| Count | Returns a count of number of values in the column. |
| Distinct Count | Returns the number of distinct values in the column. |
Applying Filters
Summary View offers powerful filtering capabilities that enables you to view only the required data. Zoho Analytics allows you to filter data based on individual values, numeric ranges, date ranges, top 10, bottom 10 etc,. It also allows you to apply multiple filters (based on multiple columns) on your report.
The filtering option discussed in this topic can be applied only when you are designing a summary view in Design Mode and not in View mode. (Refer Filters section in charts to learn about filters in detail)
To apply filters,
- Click the Filters tab next to the Summary tab.
- Drag and drop the column that you wish to add as a filter.
- Select the values that you wish to filter. You choose to either include or exclude the data in the Include/Exclude Items shelf.
- Click here to Generate Summary.
Continuing with the example - we will be filtering the report based on profit. Drop the Profit column and select Top 10 by Product.
User Filters
Summary View provides dynamic filtering capabilities in View Mode called User Filters. This enables the users who view the report to apply filters dynamically.
To create user filters,
Drag and drop the columns in the User Filters tab which is next to the Filters tab. (Refer User Filters section in Charts to know more)
Continuing with the example - Drop the Date Column in the User Filters tab to enable users to filter the report dynamically based on the Date of Sale.
The final report along with the User Filters.