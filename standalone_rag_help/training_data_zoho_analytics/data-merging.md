Data Merging
Zoho Analytics allows you to link one or more tables using a feature called lookup columns. This feature enables you to combine datasets while creating reports. But, if you wish to merge two or more datasets into a single table then you will have to use the Data Merging feature.
Let us say for instance you have a Sales database that contains yearly sales data stored as individual tables (like Sales 2016, Sales 2017 etc). What if you want to merge the "Sales 2016" data along with the "Sales 2017" data and create a consolidated table such that you can analyze the sales across all the years? This is where the data merging feature comes in handy. You can merge the data from any number of tables and store it as a single table for reporting and analysis.
Zoho Analytics uses the Query Table feature to merge datasets.
This section will tutor you on how to use the data merging feature:
- What is Data Merging?
- What is a Query Table?
- How to merge two or more datasets?
- Are there any guidelines to be followed while merging two datasets?
- Is there a limit for the number of tables that I can combine?
- If I change the data in the parent table will it get reflected in the Query table as well?
- I got an error stating "Kindly check the no.of columns used in select statements are equal or not". What should I do?
- I got an error stating "Duplicate display columns found in your SQL Query.". What should I do?
- Can I create reports over this query table?
- Can I link this query table with another table?
- Where can I learn more about Query Tables?
1. What is Data Merging?
Data merging is a method for merging similar datasets from two or more tables to create a single data set (table) for easy reporting & analysis. Zoho Analytics allows you to merge datasets using a Query Table.
2. What is a Query Table?
Query Table is a feature that enables you to prepare data for easy reporting and analysis. You can fetch data from one or more tables in a Workspace and create specific data views using the standard SQL SELECT queries. These data views are similar to tables and you can perform operations such as report creation, sharing, and even create another Query Table over an existing Query Table.
You can create Query Tables for filtering datasets, merging datasets together (union), transforming data, applying SQL query functions, joining datasets and more.
Click to learn more about Query Tables.
3. How to merge two or more datasets?
Zoho Analytics allows you to merge two or more datasets (tables) using UNION sql function in Query Tables.
Please do note that the columns that you wish to merge across the multiple tables should be of compatible data types.
Let us assume that you have 2 tables containing sales data from the year 2016 and 2017.
Following image shows the structure of the table containing sales data for the year 2016.
Following image shows the structure of the table containing sales data for the year 2017.
You can now merge the two datasets by following the below steps:
- Open the table Sales 2016 or Sales 2017
- Click New > New Query Table
- Enter the below query in the Query Editor that opens.
The below query combines data from the table "Sales 2016" along with data from the table "Sales 2017". A sample of the data will be displayed at the bottom of the query on execution.
SELECT
"Date",
"Customer Name",
"Product",
"Product Category",
"Sales",
"Cost"
FROM "Sales 2016"
UNION ALL
SELECT
"Date"
"Customer Name",
"Product",
"Product Category",
"Sales",
"Cost"
FROM "Sales 2017"
- Click Save to save the Query Table.
Click here to learn more about the UNION function.
4. Are there any guidelines to be followed while merging two datasets?
Yes, please do ensure that the following conditions are met before merging two datasets.
- The datasets that need to be merged must be similar.
For example, you can merge a sales table with another sales table. But, you will not be able to merge a sales table with a department table. - Columns that are merged should have the same or similar data type.
In case if any of the above-mentioned criteria are not met, you will not be able to merge the tables.
5. Is there a limit on the number of tables that I can merge?
No, you can merge data from any number of tables and save it as a single table.
6. If I change the data in the parent tables will it get reflected in the Query table as well?
Yes, any changes that you make to the parent tables will automatically reflect in the query table as well.
7. I got an error stating "Kindly check the no.of columns used in select statements are equal or not". What should I do?
This error will occur when the number of columns selected from the tables are not equal.
In our example, Sales 2016 contains 6 columns, whereas Sales 2017 contains 5 columns.
This issue can be rectified by specifying an equal number of columns from both the tables.
8. I got an error stating "Duplicate display columns found in your SQL Query", What should I do?
This error statement will occur when you
- have two columns with the same column name.
For example, if your dataset contains two columns with the name 'Region'. - the alias name of your column matches with any other column in the parent table.
In the below example, the column name 'Product Category' has been aliased as 'Product'. But if you check the query it also contains a column called Product.
To avoid this make sure that all the column names are unique. if not make the display column names unique by defining different alias names for the duplicate display columns.
9. Can I create reports on this merged table?
Yes, you can create any type of report over this query table as you do over a normal table. Refer to the Creating Reports Section to learn more.
10. Can I link this merged table with another table or Query Table and create reports?
Yes, you can link the merged query table with any other table using a Lookup column.
To do so,
- Open the Query table
- Select the column that you wish to change as a Lookup column
- Right-click the column name and select Change to Lookup Column
- In the Change to Lookup column dialog that opens, select the column to lookup
- Click OK
Click to learn more about creating lookup columns.
11. Where can I learn more about Query Tables?
Please refer to the following document to learn more about Query Tables - https://www.zoho.com/analytics/help/query-tables.html