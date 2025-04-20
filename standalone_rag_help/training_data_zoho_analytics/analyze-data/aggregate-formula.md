Aggregate Formulas
- Creating Aggregate Formulas
- Creating Reports Using Aggregate Formulas
- Sharing Aggregate Formulas
- View/Edit Formula
Analyzing data requires applying advanced calculations to uncover insights hidden in the huge data. Aggregate Formulas in Zoho Analytics addresses this need. Aggregate Formula allows you to calculate the much-needed key business metrics by applying the in-built functions.
- Aggregate Formula should use at least one aggregate function (SUM, AVG etc) in the calculation.The result of an Aggregate Formula is always a numeric value.
- Aggregate Formula will not be added as another column in the base table, like the Formula Column, as it is not calculated for each row but a data group. But it will be available in the report designer, where you can drag and drop it when you create a report over the table (it behaves like a column here).
- The result of an Aggregate Formula is not just a single value either. It will be computed for each data point based on the dimensional group you have specified in the report.
Creating Aggregate Formulas
To create an aggregate formula:
- Open the table over which you want to create the formula.
- Select Add > Aggregate Formula option from the toolbar
- The Add Aggregate Formula dialog box will open. Specify a name for the formula in the Formula Name field. The Data Type will be identified automatically based on the calculations performed. You can also choose the data type. The following are the data types supported for aggregate formulas: Number, Positive Number, Decimal Number, Currency, Percentage, Duration, Plain Text, and Date.
- The Add Aggregate Formula dialog box will open. Specify a name for the formula in the Formula Name field.
- Click Edit Format to modify how the date should be displayed based on its data type.
- Ask Zia - Formula Suggester helps get relevant formulas for analysis. State the requirement in the Formula Suggester field and click Generate to get the formula. Refer to this article for more information about the Open AI integration.
- To enable you to construct the formula easily, Zoho Analytics lists the following elements at the right. You can insert them by clicking it.
- Columns - This section allows you to insert the columns from the base table and the tables joined using Lookup column. Switch the table using the dropdown. All the columns in the selected table will be listed.
- Functions - This section lists all the supported in-built functions. Select the category of the function you want to use in the dropdown. Note: It is mandatory to use an aggregate function to create an aggregate formula.
- Variables - This section lists all the variables available in the workspace.
- Once you have constructed the formula, click Save.
Note: You can also insert columns from related tables joined through Lookup Column. The drop-down lists all the parent table associated with the base table. Select the required table, the columns in this table will be listed below. You can insert this in the formula by clicking.
In-built Aggregate functions
Zoho Analytics provides you a large set of pre-defined formulas designed to perform specific well-known calculations easily as in-built functions. You can use them as part of your formula to achieve your requirement.
Refer to the Formula Column in-built functions page to view the complete list of functions
Aggregate Formula columns are similar to other columns of the table. You can use them while creating a new formula. Creating formula column over another formula column helps you create powerful formula combinations. It also helps in the maintenance of the formula structure.
When you create a new aggregate formula, existing formulas will be listed along with other columns in a different color. You can insert these formulas into your new formula by clicking them. Let's say you have created a formula to calculate the Won Amount. Now you can easily reuse it to find Win Rate instead of repeating the same formula in the Win Rate formula too.
Creating Reports using Aggregate Formulas
You can create reports over Aggregate Formula, as you create over a normal column. Open the report editor over the table with the formula. All these formula will be listed in the Columns list pane on the left. You can be drag and drop theses into the report designer. You can apply advanced summary functions over the aggregate formula.
In the below example, we have calculated the month to date sales.
| mtd(sum("Sales"."Sales"),"Sales"."Date") |
When you plot the chart across months, the aggregate formula will calculate the metric for the months.
When you add region in the Color shelf, the same aggregate formula will calculate the metric for each region across months.
Sharing Aggregate Formulas
Once a Formula column is created, it behaves like any other column in a table. All collaborators will be able to access and use it with the corresponding permission granted to them.
Note:
- The User with write permission over the table can not edit, delete or format the formulas. They also can not add their own formula column over the shared table.
View/Edit Formulas
Zoho Analytics allows you to view, edit, format and delete all the formulas defined over a table through the Edit Formula option. You can view & edit both Formula Columns and Aggregate Formulas using this option.
To view/edit existing Formula Column or Aggregate Formulas:
- Open the required table.
- Select Add > Edit Formulas option from the toolbar.
- The Edit Formula dialog box will open.
- Formula Column tab will list of all the formulas associated to the table.
- Hover over the formulas, the following option will be shown.
- Edit -Click this to open the Edit Formula dialog. You can edit the constructed formula or name here.
- Format -Click this to format the Formula Column. Depending on its data type of the formula column Format option will vary. It's similar to how you format a data column. Refer here to know how to format a column.
- Delete -Click this to delete theFormula any time from the table.