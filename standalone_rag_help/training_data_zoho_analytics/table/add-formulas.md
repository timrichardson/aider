Formulas (Calculations)
Zoho Analytics provides a powerful formula engine to perform various calculations over your data. It enables you to derive business-specific metrics/insights from complex data and helps you visualize them as useful reports.
Zoho Analytics formula engine offers a rich set of in-built functions library to help derive your own business metrics through formulas (calculations), that meet your specific analytical requirements.
The following are the types of formulas supported in Zoho Analytics.
Formula Column
Formula Columns, as the name indicates, are columns derived using calculations. The calculations can vary from simple arithmetic expressions to deeper logical expressions.
Formula columns enable you to add derived calculated columns to your data tables easily. You can use these formula columns in creating reports in the same way you use other columns in a table.
Click here to learn more about Formula Column.
Aggregate Formula
Aggregate Formulas are meant for applying calculations over your data by aggregating/grouping/combining them. You have to mandatorily use at least one aggregate function (SUM, AVG, MAX, etc) in the formula calculation to create an Aggregate Formula.
The result of an Aggregate Formula is always a numeric value. Unlike Formula Column, this will not be added as another column in the base table. They will just be associated with the table on which they have been created and can be used in creating reports (Charts, Pivot Tables, and Summary Views) like any other table column.
Aggregate formula value will be computed for each data record/group in a report in which it is used.
Click here to learn more about Aggregate Formula.
Report Formula
Report Formula, as the name indicates, is a formula specific to a particular report. You can create this formula only using the columns used within a report. The result will be added as another column in the report and cannot be used in any other report.
It differs from Formula Column and Aggregate Formula, which are based over a table (and are then available for creating any report over this table). Report formulas are available only within a specific report in which they are created.
Click here to learn more about Report Formula.