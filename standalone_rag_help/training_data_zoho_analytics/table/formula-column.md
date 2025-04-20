Formula Column
Zoho Analytics allows you to define your own powerful formulas to meet your specific reporting requirements. This allows you to perform from a simple arithmetic calculations to a complex combinations of calculations. Zoho Analytics also provides predefined mathematical formulas as in-built functions to perform specific well-known calculations easily.
The output of the formula will be added as a new column in the table. You can use these formula columns similar to other columns in the table in another formula, or creating reports.
- Creating Formula Column
- Quick Add option for Formula Columns
- Constructing a Formula
- In-built Functions
- Creating Formulas Over Formula Column
- Creating Reports Using Formula Column
- Sharing Formula Columns
- View/Edit Formula
Creating Formula Column
You can create Formula Column over a table. Follow the below to create a formula column:
- Open the table over which you want to create the Formula Column.
- Click the Add > Formula Column option from the toolbar or right click on a column and then click Add Formula > Formula Column.
- The Formula Column dialog box will open.
- Provide a Formula Name. This will be used as the Column header for the Formula Column.
- Enter the formula in the provided field. Refer to this section to know how to construct a formula.
- You can also use Ask Zia: Formula Suggester to get find formulas for your requirement. This will return the standard formula. You need to insert your data column in the appropriate place. Click here to learn more about Formula Suggester.
- All the columns in the tables and the supported in-build function will be listed at the right side of the dialog, to enable you to insert them in your formulas easily.
- Click Save. The formula will be saved and added as a new column in the table.
Quick Add option for Formula Columns
Zoho Analytics also provides an easy and convenient way to add formula columns which are based on a limited set of widely used functions.
Follow the steps to use the quick option for Formula Column.
- Select a column based on which you want to add the formula column.
- Click Add > Add Formula Column option on the toolbar.
- Zoho Analytics automatically identifies the data type of the column and lists the widely used pre-defined formulas for the column.
- Select the required formula, Zoho Analytics applies the formula on the corresponding column and adds the result as a new formula column. The column header will be named as {Function} {Column over which it is applied}. You can rename it later.
Constructing a Formula
This section explains how to construct formulas to achieve your needs.
Formula Elements
To help Zoho Analytics understand the formula, follow the format as given below.
- Column nnames- Double Quotes e.g., "Sales", "Cost"
- Text Value - Single Quotes e.g., 'Deal Won', 'Deal Lost'
- Numeric Value - No Quotes e.g., 100
- Arithmetic Operators - (+), (-), (\*), (/), etc.,
Calculation
Zoho Analytics allows you to perform various calculations over the columns with different data types. Let's see a few examples.
Example 1
You can easily round off your invoice amount using the round function.
| round("Amount") |
You can even choose to round off to the nearest greater or lesser number using the ceil or the floor functions.
| ceil("Amount") |
| floor("Amount") |
Example 2
You can apply simple arithmetic calculations such as to finding a discounted price with 20% off the original price.
| "Price"- (20/"Price" \*100) |
Example 3
You can also apply date based calculations. The below formula calculates the year of experience in years using the data and time difference function and verifies whether the employee has five years or more experience, and is eligible to avail a specific option.
| if(dateandtimediff(YEAR, "Date of Joining", currentdate( )) >= 5, 'Yes', 'No') |
Order of Execution
Formula Column allows you to perform simple arithmetic calculations such as addition and subtraction, and even complex formulas. Zoho Analytics will follow the BODMAS or PEMDAS rule as the order of execution for the operation.
Condition based Calculations
Zoho Analytics allows you to set conditions to execute an operation. You can do this using IFor Case< statements.
IF Statement
IF statement is one of the options to write a formula with conditions.
Format
|
You can apply the condition over multiple categories by using a nested IF statement. The following nested IF statement categorizes the customer type based on the sales amount.
| if("Amount" <= 500, 'Basic', if("Amount" <= 15000, 'Standard', if("Amount" <= 30000, 'Premium', if("Amount" > 30000, 'Enterprise', 'Others')))) |
Case Statement
The Case Statement works with the 'when and then' logic. When the condition is met, then the expression will be executed.
Format 1
| case "Column Name" WHEN 'Column Value 1' THEN 'expr1' WHEN 'Column Value 2'THEN 'expr2' ELSE 'expr3' END |
Format 2
| CASE WHEN {Condition 1} 'expr1' WHEN {Condition 2} THEN 'expr2' ELSE NULL END |
Example
| CASE WHEN "Amount" = 500 THEN 'Basic' WHEN "Amount" = 15000 THEN 'Standard WHEN "Amount" = 30000 THEN 'Premium' WHEN "Amount" > 30000 HEN 'Enterprise' ELSE NULL END |
Operators
Zoho Analytics supports the following operators to define conditions on your formula.
| Operator | Description |
| AND | Used to combine the conditions where all conditions need to be met. Ex: CASE WHEN "Customer Type" = 'Enterprise' And "Product Price" > 500 THEN "Price" - ("Price" \*20/100) ELSE NULL END Here, when the customer type is Enterprise and the product price is above 500, then a 20% discount will be applied to the product price. |
| OR - | Used to combine the conditions where either of the conditions need to meet. CASE WHEN "Customer Type" = 'Enterprise' Or "Product Price" > 500 THEN "Price" - ("Price" \* 20/100) ELSE NULL END
Here, when the customer type is Enterprise, or when the product price is above 500, then a 20% discount will be applied to the product price. |
| In | Used to match where one of the multiple values meets the condition.
CASE WHEN "Product" IN ('Kids Cycle', '7 Gear Cycle', '21 Gear Cycle') THEN 'Cycle' ELSE NULL END |
| Not In | Used to match where none of the multiple values meets the condition. CASE WHEN "Product Category" Not IN ('Stationery', 'Furniture', 'Toys') THEN 'Miscellaneous' ELSE NULL END |
| Between | Used to ensure the data is between the specified range. CASE WHEN "Sales" BETWEEN 100 AND 500 THEN 'Good' WHEN "Sales" BETWEEN 500 AND 1000 THEN 'Excellect' ELSE NULL END |
| Not Between | Used to ensure the data is not between the specified range. CASE WHEN "Weather" NOT BETWEEN 24 AND 33 THEN 'Out of Trend' ELSE NULL END< |
| Like | Used to identify data with matching pattern. CASE WHEN "Course Code" like 'ENG%'THEN 'English' WHEN "Course Code" like 'Math%'THEN 'Maths' ELSE NULL END |
| Not Like | Used to identify data that does not match the pattern. CASE WHEN {Condition 1} THEN 'expr1'ELSE NULL END |
| Is Null | Used to identify whether a data is null. CASE WHEN "Survey Email ID" Is Null THEN 'Anonymous' ELSE NULL END |
| Is Not Null | Used to identify whether a data is not null. CASE WHEN "Survey Email ID" Is Not Null THEN 'Call back' ELSE NULL END |
In-built functions provided by Zoho Analytics
Zoho Analytics provides you a large set of pre-defined formulas designed to perform specific well-known calculations easily as in-built functions. You can use them as part of your formula to achieve your requirement.
Refer to the In-Built Function page to view the complete list of functions.
Creating Formulas Over Formula Column
Formula columns are similar to other columns of the table. You can use them while creating a new formula column. Creating formula column over another formula column helps you create powerful formula combinations.It also helps in the maintenance of the formula structure.
Let's say, you want to split the support tickets that flow into your portal into shifts based on the hour of the created time. You need to find the hour of the ticket created time and then bucket them into different shifts. Instead of writing a single formula, splitting them into two will be easier to maintain.
As Single Formula
| if(hour("Created Time")>6 and hour("Created Time")<22,if(hour("Created Time")>14,'2nd Shift','General Shift'),'Night Shift') |
As Split Formula
| hour("Created Time") |
| if("hours">6 and "hours"<22,if("hours">14,'2nd Shift','General Shift'),'Night Shift') |
Creating Reports Using Formula Column
You can create reports over Formula Column as you create over a normal column. Open the report editor over the table with the formula. All these formula columns will be listed in the Columns list pane on the left. You can be drag and drop theses into the report designer. You can apply functions on the formula column, as you do for other columns.
The following screenshot shows the Payment Date formula column listed in the columns list page:
Sharing a Formula Column
Once a Formula column is created, it behaves like any other column in a table. All collaborators will be able to access and use it with the corresponding permission granted to them.
Note:
The User with write permission over the table can not edit, delete or format the formulas. They also can not add their own formula column over the shared table.
View or Edit Formulas
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