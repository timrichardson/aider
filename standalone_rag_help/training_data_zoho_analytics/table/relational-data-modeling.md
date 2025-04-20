Relational Data Modeling
You might have a database consisting of multiple data tables related to each other. You would want to import these related tables into Zoho Analytics and create reports and dashboards combining data from these tables.
When these tables are imported as separate entities into a workspace, you cannot create reports and dashboards using data from these tables. You need to join the tables using a lookup relationship to perform cross-functional analytics.
With a feature like Lookup Columns you can,
- Organize your data in a normalized model avoiding duplication of information across tables
- Segregate as measures (numeric data columns which you could aggregate) and facts/dimensions (data columns which you use for grouping in reports).
- Define familiar models like Star Schema & Snowflake Schema which are optimized for reporting and analysis.
Once you relate two tables using lookup columns, Zoho Analytics will use this information to enable you create reports by combining columns from these tables, seamlessly without no additional effort.
Relating Tables with Lookup columns
In a relational database, the related columns from multiple tables are joined using a Foreign key. In Zoho Analytics, the related columns from multiple tables are joined using a Lookup column relationship using cardinality functions. When we join two tables in Zoho Analytics, a Parent-Child relationship will be created between the two tables.
What is Cardinality?
Cardinality refers to the type of lookup relationship that can be created between two tables. Any two tables can be related using either of the following relationships:
- One-to-One Relationship: In a one-to-one relationship, the tables that we are trying to connect will have distant values and only one possible relationship can be formed between the two tables. This type of relationship is not widespread.
- Many-to-Many Relationship: Many-to-Many Relationship or M-N relationship is where both the columns used to create a relationship have multiple values. Each element in the "M" attribute (Parent Table) can have multiple matching rows in the "N" attribute (Child Table) and each element in the "N" attribute (Child Table) can have multiple matching rows in the "M" attribute (Parent Table).
- One-to-Many/Many-to-One Relationship: This is the most common type of relationship. Each element in the "1" attribute corresponds to one or more elements in the "N" attribute, and each "N" attribute corresponds to one and only one element in the "1" attribute. In a One-to-Many relationship, the parent table will have unique values and the child table will have duplicate values. In a Many-to-One relationship, the parent table will have unique values and the child table will contain duplicate values.
Joining Tables using Lookup columns
Lookup columns can be used to join tables where you need to retrieve data from two or more tables in a Workspace. In Zoho Analytics, tables with lookup relationships can be joined in the following two ways:
Joining Tables with Auto-Join
Zoho Analytics allows you to define a lookup relationship from the import wizard, the table or from the report editor. While creating reports, Zoho Analytics will list all the tables that have a lookup relationship in the Column list panel of the Report designer. You can drag and drop the required columns from the list into the respective shelves to create the reports. Click here to know more about joining tables.
The following example shows the Department-wise Employee count Pivot Table created over the Employee and Department tables using Auto-Join feature.
In the above example, Auto-Join feature detects the lookup relationship created between Department and Employee tables. Based on this relationship, it lists the columns from both the table under the Column List panel in the Report Designer as shown in the above screenshot.
By default, Zoho Analytics will join tables using the Left Join type. Possible Join types are:
- Left Join - Report will be computed with all the rows from the child table (left) and only the matching rows from the parent table (right). Matching is done based on lookup columns defined between child & parent tables. This will be the default join type.
- Right Join - Report will be computed with all the rows from the parent table (right) and only the matching rows from the child table (left). Matching is done based on lookup columns defined between parent & child tables.
You can choose to change the join type. You will find a view relationship icon in the report designer while creating reports by joining tables. Click this, the View Relationship Used dialog will open. Select the type of join and click Apply.
Joining Tables with Query Table
Query Table is a feature that enables you to prepare data for easy reporting and analysis. You can combine data from one or more tables in a Workspace and create specific data views using the standard SQL SELECT queries. These data views are similar to tables and you can perform operations such as report creation, sharing, and even create another Query Table over an existing Query Table.
You can create Query Tables for filtering datasets, batching datasets together (union), transforming data, applying SQL query functions, joining datasets and more.
For example, a query combining the Employee and Department tables can be made as shown below.
The example query above joins the Employee & Department tables, getting the department name mapped to each employee. Over the query table that you have created by joining the necessary tables, Zoho Analytics allows you to create any type of reports for analysis and visualization. Click here to learn more about Query Table.