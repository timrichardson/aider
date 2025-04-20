Report Formulas
Zoho Analytics allows you to create quickly new formulas specific to a report. These formulas can be created over charts, pivot tables, and summary views.
The following are the two types of report formulas:
- Basic Formula: This formula can be created by only using the fields used in the report. You can apply basic arithmetic (e.g., +, -, \*, /), comparison (e.g., =, >, <), and logical operators (e.g., AND, OR, NOT). Additionally, Basic Formulas support the use of IF statements.
- Aggregate Formula: This formula can be created by combining aggregate functions and arithmetic operations using all the related columns associated with the current column or table in the report. Refer to the Aggregate functions article to learn more about the functions supported in Zoho Analytics.
On this Page
Create Basic Report Formulas
- Drag and drop the required columns into the respective shelves.
- Click the Add Report Formula icon,
- For Reports: The Add Report Formula option can be found below the Y-axis field.
- For Pivot and Summary view: The Add Report Formula option can be found above the data shelf.
- For Reports: The Add Report Formula option can be found below the Y-axis field.
- The Add Report Formula dialog will open. Choose the type of formula you intend to create - Basic Formula or Aggregate Formula.
- Give a suitable Formula Column Name. You can also add descriptions and synonyms for this column for training Ask Zia.
- Choose the return Data Type of the formula. Click Edit Format to modify the format settings. The format options are specific to the data type selected. Refer to the Format Columns article to learn more.
- Choose the column and specify the operations to apply in the formula window, and click Save.
Basic Formula will be added to the report. Please note that the basic formula can be used (dropped) only once in the report and cannot be used as Filters and User Filters.
Note:
- Ensure to save the report once again after adding the report formula to the report.
- Deleting a report will also delete the report formulas created on it.
Create Aggregate Report Formulas
- Drag and drop the required columns into the respective shelves.
- Click the Add Report Formula icon,
f - Give a suitable Formula Name. You can also add descriptions and synonyms for this column for training Ask Zia.
- Choose the return Data Type of the formula. Click Edit format to modify the format settings. The format options are specific to the data type selected. Refer to the Format Columns article to learn more.
- Use Zia Formula Suggester to explain your use case and get the correct formula. Refer to the Formula suggester article to learn more.
- For aggregate formulas, you can use all the related columns associated with the current column or table in the workspace. Specify the formula.
- Select the checkbox, Add aggregate formula to table to associate it with a table and to use it in other reports and dashboards.Once this option is enabled, the report level aggregate formula can be used in other reports and dashboards.
- Click Save.
Once the Aggregate Formula is added to the report, the sub function can be changed if needed.
Manage Report formulas
All the report formulas created are listed in the data pane on the left. You can manage all the report formula actions here.
- Access the Report Formulas tab from the data pane on the left.
- Click the more icon and choose the required action from the drop-down menu.
- Add to Filter or user filter: Choosing this option will apply the report formula to act as filters and user filters. This option is applicable only to the Aggregate Formula.
- Edit Aggregate Formula: Choosing this option will allow you to modify the report formula.
- Delete formula: Choosing this option will remove the formula from the report.