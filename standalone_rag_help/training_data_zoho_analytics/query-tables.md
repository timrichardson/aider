Query Tables for Data Preparation
Query Table is a feature that enables you to prepare data for easy reporting and analysis. You can combine data from one or more tables in a Workspace and create specific data views using the standard SQL SELECT queries. These data views are similar to tables and you can perform operations such as report creation, sharing, and even create another Query Table over an existing Query Table.
You can create Query Tables for filtering datasets, batching datasets together (union), transforming data, applying SQL query functions, joining datasets and more.
General
- What is a Query Table?
- Are there any specific points that I should keep in mind while creating a Query Table?
- What is SQL SELECT command and how is it used in Query Tables?
- What are the SQL dialects supported in Query Tables?
- Do you recommend any specific SQL dialect?
Creating a Query Table
- How can I create a Query Table?
- What are the standard SQL functions supported in Zoho Analytics?
- How can I modify an existing query?
- How can I rename columns in the Query Table?
- I have a dimension column with multiple repetitive values, (e.g., Product Category, Region, Department Name etc). Can I have each unique row value in the column transformed to a separate column in a new table?
- I have all my regional sales as different columns. Can I merge the data into a single column?
- Can I merge data sets using a Query Table?
- Can I join one or more tables using a Query Table?
- What are the types of SQL Joins supported by Zoho Analytics?
- Can I link two Query Tables using a Lookup Column?
- Can I create a Query Table over a Query Table?
- How many levels of Query Tables can I create over an existing Query Table?
- Can I create an aggregate formula for a Query Table?
- How can I change the data type of a column in a Query Table?
- How do I format a column?
- Can I create co-related sub queries?
- What is a Common Table Expression (CTE), and does Zoho Analytics support it?
- What are the limitations of Common Table Expressions (CTEs) in Zoho Analytics?
Reporting
Working with Query Tables
- How do I search for a value in a Query Table?
- How do I sort a column?
- How do I filter the data in a Query Table?
- How can I show/hide the columns in a Query Table?
- How can I freeze columns in a Query Table?
- How do I re-order or resize a column?
- How do I apply conditional formatting in a Query Table?
Collaboration
- How do I share a Query Table?
- How do I export a Query Table?
- How do I embed/generate the URL of a Query Table?
Troubleshooting Tips
- Are there any specific points that I must keep in mind while creating a Query Table?
- I created a Query Table but it keeps loading when I access it. Why?
- I created a query table but it timed out when I tried to Save/Access it. What should I do?
- I was trying to remove a column from an existing Query Table. But, it throws an error. Why?
General
1. What is a Query Table?
Query Table enables you to prepare data for easy reporting and analysis. You can combine data from one or more tables in a Workspace to facilitate easy reporting. These data views are similar to tables and you can perform operations such as report creation, sharing, and even create another Query Table over an existing Query Table.
You can create Query Tables for filtering datasets, batching datasets together (union), transforming data, applying SQL query functions, joining datasets and more.
2. Are there any specific points that I should keep in mind while creating a query table?
Query Tables enable you to meet your advanced reporting needs. However, improper construction and usage might affect the performance of SQL queries. The following are some of the best practices to be followed when working with Query Tables.
Do not create Query Tables,
- For Simple Calculations - Do not create a query table for simple calculations, especially over a single table. You can use formulas (calculations) to achieve this.
- To Join Table - Do not create a query table just to join data. Zoho Analytics supports Auto-Join feature to establish a relational data model. Choose Query Table only if it is absolutely necessary.
- To Filter Data - Do not create multiple query tables to share specific data for different users. Instead, apply dynamic share filter criteria.
- One for Each Case - Avoid writing separate query tables for each use case. Instead, try combining a few. For example, you can calculate multiple metrics across the same dimensions as a single query table. Having too many query tables in a workspace will affect the overall performance of the system.
- Query Table over Query Table - Zoho Analytics supports creating a query table over another query table in multiple levels. However, avoid using this unnecessarily.
- Cleanup Stale Query Tables - Periodically clean up unused query tables to avoid unnecessary constraints.
Make sure that your query table adheres to the following points.
- Avoid writing queries in complex format. Use simple steps to achieve your needs.
- Avoid using SELECT \* and copying the entire table. Select only the required columns.
- While creating query tables, ensure you have placed proper join conditions. Duplicate values in the join columns may return inaccurate results. These are not only useless but also create performance issues with the server.
- Avoid using cartesian joins (n\*n). Always try to have 1\*1 or 1\*n or n\*1 relationships while joining the tables in the query tables, with no join condition or with condition column duplicate.
- A GROUP BY clause should be used only over non-aggregate columns.
- Use a GROUP BY clause for the non-aggregate columns selected in your query, whenever any aggregate functions (min(), max(), sum(), count() etc) are used over the metric columns in the query.
- Avoid applying too many columns in a GROUP BY clause (such as 30 or 40 columns). Select the required columns alone. In case you want more columns, specify them as a sub query out the query for metric calculation. This way, the calculation will only be done with required data, and rest will be appended in the corresponding row, without affecting the query performance.
- Alias names cannot be used in a HAVING clause.
- Apply necessary filters in the first level of query and retrieve only the required data. And then compute the aggregate values. Let's say you have 10 years of data in a table and analysis is to done based on current year data alone. Filtering current year data avoids applying the calculation over the entire data.
- Generally, distinct operation over a large dataset might slow down the performance. Use it only when it is absolutely necessary.
- Avoid using GROUP BY and a distinct operator in a single select query statement.
- Usage of the UNION ALL operator over the UNION function is recommended, because UNION implicitly applies Distinct operation.
- Try to do the computation with a smaller number of records.
- Aggregate the data set first, then apply a join clause.
- Union clause can be avoided for referring to same tables. This could be achieved by using Case When statements.
- Always prefer to use the IN clause instead of multiple OR conditions for expression with the same left side expression.
- f(column) = '1' or f(column) = '2' or f(column) = '3' This can be used as f(column) IN ('1', '2', '3')
- f(column) = '1' or f(column) = '2' or f(column) = '3' This can be used as f(column) IN ('1', '2', '3')
3. What is SQL SELECT command and how is it used in Zoho Analytics?
SQL (Structured Query Language) is a standard & popular language for storing, manipulating and retrieving data in databases (eg., Oracle, SQL Server, MySQL etc.,).
Zoho Analytics uses the SQL "SELECT" statement for creating a Query Table. The SELECT statement is used to select data from the tables. A simple SQL SELECT query looks as shown below:
SELECT Customer Name, City FROM Customers;
This query fetches the Customer Name and City from the table Customers.
To learn more about SQL SELECT queries refer to this link.
4. What are the SQL dialects supported in Query Tables?
Zoho Analytics currently supports SQL SELECT queries written in ANSI, Oracle, SQL Server, IBM DB2, MySQL, Sybase, Informix and PostgreSQL SQL dialects.
Although we support all of the above-mentioned dialects, we would recommend you to use the ANSI SQL dialect for better coverage and support.
5. Do you recommend any specific SQL dialect?
We support SQL Select queries written in the all of the above-mentioned dialects (Refer Question 3). But, we would recommend you to use the ANSI SQL dialect for better coverage and support.
Creating a Query Table
1. How can I create a Query Table?
2. What are the standard SQL functions supported in a Query Table?
Zoho Analytics allows you to use all the functions listed under the Insert SQL Functions tab while creating a Query Table. Please note that this is just a suggested list of functions and is not limited to these. However, the suggested list is guaranteed to work.
3. How can I modify an existing query?
You can modify an existing query by following the below steps:
You can either make the changes in the existing query or click the Clear Query button to clear the entire query and type a new one.
- Click Execute Query after you have finished rewriting/modifying the query.
- Click Save to save the Query Table values with the new query results.
4. How can I rename columns in the Query Table?
Zoho Analytics allows you to rename columns in the Query Table using an alias name. You can define this alias name using the SQL keyword "As".
For example, let's assume a case where we use the query table to determine the Customer type as New or Returning customer from the Orders table. Here, we have added the alias name to the columns for better readability.
Sample query:
Note:
Any modification to the column name will be applied across all the associated views and query tables.
5. I have a dimension column with multiple repetitive values, (e.g., Product Category, Region, Department Name, etc). Can I have each unique row value in the column transformed to a separate column in a new table?
Yes, you can split the distinct values from a column and transform them into multiple columns using the PIVOT clause.
The PIVOT keyword rotates rows into columns. It transforms the input table in a query in such a way that each unique value in a chosen column is converted to a separate column in the output table.
Example
In this case, the Sales data across Product Category is in a single column.
Using the below query you can split the unique value of the column Product Category into multiple columns as Grocery, Furniture, and Stationery.
pivot
(sum("pivot-source"."Sales") FOR "pivot-source"."Product category" in ( "Grocery", "Furniture", "Stationery" )
) AS Pivottable
6. I have all my regional sales as different columns. Can I merge the data into a single column?
Yes, you can merge the data from multiple columns into a single column using the UNPIVOT clause.
Example
In this case, the Sales data for each region is in a column.
Using the below query, the columns East, West, South and Central are combined into a column named Region.
7. Can I merge data sets using a Query Table?
Yes, you can merge data sets using the "UNION" function in a Query Table. In the below Query Table we are combining the Product Name and License Cost from Product Table with the Product Name and License Cost from the Sales Table.
8. Can I join one or more tables using a Query Table?
Yes, you can. But, we strongly recommend you use the Auto-Join feature in case you wish to join (combine) two or more tables. This feature automatically joins tables when creating reports, if the tables are connected using a Lookup column. Click to learn more.
If you would still prefer to use a Query Table to join tables, you can do so. Zoho Analytics supports the following joins:
The illustrates how the data is combined in all three join types when you join the column DepName from the Department Table along with the columns Emp\_Name, Joining\_Date from the Employee table.
9. What are the types of SQL Joins supported by Zoho Analytics?
Zoho Analytics supports the following joins:
10. Can I link two Query Tables using a Lookup Column?
Yes, you can link two Query Tables using a Lookup column as you do over a table.
To do so,
- Open the Query table
- Select the column that you wish to change as a Lookup column
- Right click the column name and select Change to Lookup Column
- In the Change to Lookup column dialog that opens, select the Column to Lookup
- Click OK
11. Can I create a Query Table over a Query Table?
Yes, you can create Query Tables over an existing Query Table. You can create a maximum of 3 levels of queries over an existing Query Table.
12. How many levels of Query Tables can you create over an existing Query Table?
You can create a maximum of 3 levels of queries over an existing Query Table.
13. Can I create an aggregate formula for a Query Table?
Yes, Zoho Analytics supports aggregate formulas for Query Tables. Please refer to this help document to learn more about creating aggregate formulas.
14. How can I change the data type of a column in a Query Table?
To change the data type of the column in a Query Table, follow the below steps:
- Select the column and click the Column Properties button in Toolbar.
- Click Change Datatype menu option.
- In the Change Data Type dialog that opens change the data-type accordingly and click OK.
15. How do I format a column?
Zoho Analytics offers options to change the format of a column in a Query Table (such as alignment, decimal places, date formats, currency symbol, etc) depending on its data type as you can do over a table.
To format a column:
- Select the column you want to format by clicking on the header.
- Click Format > Format Column option from the toolbar, or right-click the column name and select the Format Column option from the pop-up menu. The Format Column dialog box with available options for formatting the column will open.
- Select the preferred formatting options in the dialog box and click OK.
Formatting options provided in the dialog box differs based on the data type of the selected column. Refer to this help documentation to learn more.
16. Can I create co-related sub queries?
Zoho Analytics at present does not allow you to create co-related sub queries (sub queries inside the Where clause) . In case you have a special case where you need to use a sub query, please do mail us your requirements to support@zohoanalytics.com, we will analyze your requirement provide you with an alternate solution.
17. What is a Common Table Expression (CTE), and does Zoho Analytics support it?
A Common Table Expression (CTE) is a temporary result set defined within a SQL statement's execution scope. It simplifies complex queries by allowing the temporary result set to be referenced multiple times within the same query, enhancing readability and performance.
Zoho Analytics supports only non-recursive CTEs in query tables. This improves query organization and efficiency by reducing redundancy, and eliminating the need for repeated subqueries.
Benefits of CTE:
- Improves query performance.
- Reduces redundant calculations by allowing result reuse within a query.
- Enhances query readability and structure.
- Breaks down complex queries into smaller, logical parts.
Example Use Case:
A CTE is particularly useful when a result set needs to be referenced multiple times within a query, which is not possible with sub-queries without recalculating them.
For instance, suppose you need to find products priced above the average category price. Without a CTE, you would have to repeat the same sub-query multiple times, leading to inefficiency.
By using a CTE, the average price per category can be computed once and referenced multiple times, improving performance and readability. Here’s an example SQL query:
CategoryAvg AS (
SELECT category, AVG(price) AS avg\_price
FROM products
GROUP BY category
)
SELECT p.id, p.category, p.price, c.avg\_price,
(p.price - c.avg\_price) AS price\_diff
FROM products p
JOIN CategoryAvg c ON p.category = c.category
WHERE p.price > c.avg\_price;
This approach avoids redundant calculations and makes the query more efficient.
18. What are the limitations of Common Table Expressions (CTEs) in Zoho Analytics?
While CTEs improve query readability and performance, Zoho Analytics imposes certain restrictions on their usage. The key limitations include:
- Only non-recursive CTEs are supported. Recursive CTEs are not allowed.
- Subqueries cannot be used within CTEs.
- CTEs cannot be used within subqueries.
- PIVOT and UNPIVOT operations cannot be used along with CTEs.
- A query can include a maximum of three CTEs.
These constraints should be considered when designing CTE queries in Zoho Analytics to ensure compatibility and optimal performance.
Reporting
1. Can I create reports over a Query Table?
Yes, you can. Query Table when created acts just like a table. You can create any type of report as you do over a table. Refer to the following documents to learn about creating reports and dashboards:
Working with Query Tables
1. How do I search for a value in a Query Table?
Zoho Analytics allows you to quickly search for specific records within a large set of data. The Search box in the toolbar can be used to locate records in a Query Table that matches the keyword that you specify.
2. How do I sort a column?
Zoho Analytics allows you to rearrange the rows in a Query Table by sorting values in columns. To sort a column follow the below steps:
Select the column and click the Sort button in the tool bar. The available sort options are:
- Sort Ascending sorts text data in ascending alphabetical order (A to Z), numbers from smallest to largest (0-9), and dates from oldest to most recent.
- Sort Descending sorts text data in descending alphabetical order (Z to A), numbers from largest to smallest (9-0), and dates from most recent to oldest.
- Remove Sorting clears the applied sorting.
3. How do I filter the data in a Query Table?
Zoho Analytics provides a Filter option to easily filter the records in your Query Table based on the criteria that you specify. Depending on the data type of the column, Zoho Analytics offers various filtering options such as filter based on specific numeric ranges, date ranges, individual values, partial match, and more. You can also apply filters on multiple columns at a time.
To apply a filter:
- Click on the Filter button in the toolbar and select the filter that you wish to apply for each column from the dropdown as shown below.
- Click Apply to apply the filter and Save to save the filter with a name.
Note:
- The Filter option mentioned above is not applicable while sharing the report. If you wish to filter data while sharing a report, refer to this help section.
- If you wish to permanently filter out the data in your Query Table, use the WHERE clause in your query.
4. How can I show/hide the columns in a Query Table?
To show or hide columns in a Query Table:
- Click the More button in the toolbar and select Show/Hide Columns.
- Select or unselect checkboxes in the Show/Hide/Reorder Column dialogue box to show or hide individual columns.
- You can also reorder the columns in this dialog, to reorder - select the column and click on the up or down arrow.
- Click OK.
5. How can I freeze columns in a Query Table?
Zoho Analytics has a Freeze Column option that makes sure certain columns stay visible in the Query Table, even when you scroll horizontally across the screen. Refer to the Freeze Columns topic to learn more.
To freeze a column:
- Select the column and click More > Freeze Column.
- To unfreeze the column, click the pin icon in the top-right corner of the column.
6. How do I re-order or resize a column?
Zoho Analytics allows you to reorder or resize the columns in a Query Table by dragging the column as you can do in a table.
You can also do the this by selecting More > Show/Hide Columns.
7. How do I apply conditional formatting in a Query Table?
The conditional formatting feature allows you to highlight cells in a column with different background and font colors based on a condition. You must specify the required conditions/criteria for formatting. When data in a cell meets the condition, Zoho Analytics applies the corresponding formatting style that you have specified.
To apply conditional formatting:
- Select the column to format by clicking on the header.
- Click Column Properties > Conditional Formatting option from the toolbar. The Conditional Formatting dialog will open.
- Specify the conditions to format the column. (Refer the topic "Conditional Formatting" to learn more).
- Click OK. All cells that meet the condition will be formatted accordingly.
This is similar to the conditional formatting feature in a table. To learn more refer this link.
Sharing and Collaboration
1. How do I share a Query Table?
You can easily share the Query Tables that you create with other users using the Share option. The Share option in a Query Table is similar to that in a table. Once you share your Query Table your users will be able to create reports and dashboards over the same.
Refer to the Sharing and Collaboration help page for more details on this.
Note:
- For shared users, the Share option will be enabled only when the Administrator has provided permission. Refer to the Sharing and Collaboration topic to learn how to share a Query Table.
2. How do I export a Query Table?
Zoho Analytics allows you to export the Query Table that you have created into various file formats like CSV, PDF, XLS or HTML. Refer to this document to learn more.
3. How do I embed/generate the URL of a Query Table?
Zoho Analytics allows you to publish the Query Table that you have created on your websites or blogs. You can also set and control the access privileges for the users who access the Query Table. This option is enabled only for Workspace Administrators or administrators.
Refer to the Publishing Options topic to learn how to publish a Query Table.
Troubleshooting Tips
1. Are there any specific points that I must keep in mind while creating a Query Table?
Yes, please do make sure that your Query Table adheres to the following points
Performance Considerations
- Avoid complex queries
- Avoid unnecessary joins. In case you wish to join two or more tables, we suggest you to use the Auto-Join feature
- Avoid cartesian joins
- Avoid creating a Query Table over a Query Table as much as possible
Functional Considerations
- Use Group By clause whenever the Aggregate functions (min(),max(),sum(),count(),...etc.,) and columns are used together
- Non-aggregate columns present in SELECT columns should be used in Group By clause
- Alias names cannot be used in HAVING clause
2. I created a Query Table but it keeps loading when I access it. Why?
Query Tables are performance intensive. The performance of the Query Table depends on the number of rows, the types of joins used, the functions used etc. Please do make sure that you adhere to the points mentioned in the previous question while creating a Query Table.
We recommend you to keep the query simple. If the issue persists try restructuring the query used in the Query Table. For further assistance, you can also write to us at support@zohoanalytics.com. We will help you optimize your Query Table.
3. I created a query table but it timed out when I tried to Save/Access it. What should I do?
Like said in the previous question, Query Tables are performance intensive. Please do make sure that you keep the points in Question#1 in mind while creating a Query Table.
For further assistance, you can also write to us at support@zohoanalytics.com. We will help you optimize your Query Table.
4. I am unable to remove a column from an existing Query Table. Why?
This can happen when the column that you are trying to delete from the Query Table has dependent reports created over it. Zoho Analytics will run a dependency check before deleting a column in a query table.
In case it has any dependent views, then Zoho Analytics will abort the delete process and display the dependent items for you to review. You can review and delete the dependent items before deleting the column.