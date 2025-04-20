Applying Filters
Filters
Zoho Analytics offers powerful Filtering options to filter the necessary records that are to be plotted in the report you create. The Filtering options are the same for all types of reports that you create in Zoho Analytics - charts, pivot table & summary views.
Depending on the data type of the column, you can filter specific numeric ranges, date ranges, individual values, top10, bottom 10 etc., Zoho Analytics also allows you to apply multiple filters (based on multiple columns) on a report. The filtering options discussed in this topic can be applied only when you are designing a report (i.e., when you are in design mode) and not in the view mode.
To create a filter, after you have created the required chart (or pivot or summary view)
- Select the required Chart.
- Click Edit Design option in the toolbar.
(or)
- Right click on the Chart name listed in the left side of the Workspace and select Edit.
- Click Filters tab next to the Graph tab in the design area. The Filters Tab has three boxes as shown in the screenshot below. Filter Shelf (Box) to drop the columns, second box displays the filter options and lists all the possible values for filtering and the third box displays added filter items.
- Drag and drop the required columns in to the Filter shelf.
Note:
- In the case of Charts you can use the Add to Filter icon () next to X and Y axes to quickly add the columns plotted against X and Y axes into the Filters tab.
Once a column is dropped, a list of all possible options for filtering will be displayed in the (second) box right to Filter Shelf as shown in the screenshot above. The filtering options provided varies based on the data type of the column dropped.
Numeric & Currency type:
Following table lists all the possible options for filtering various column data types:
| Option | Description |
| Individual Values | This option allows you to filter data based on individual values of the selected numeric column. All possible individual values of the dropped column will be listed in the filter tab. You can select these values to filter them. |
| Ranges | This option allows you to filter data based on numeric ranges into which the values in the columns can be segmented Eg., 0 to 100, 101 to 250 etc., Filter tab will list a suggested range of values for filtering. You can choose the required range to filter. You can also add your own custom ranges for filtering. |
| Top/Bottom N | This option allows you to rank the records and filter a specified number of Top/Bottom record. The chart will be sorted ascending or descending to illustrate the ranking. For example Top 10 will filter the top 10 values in the column and Bottom 10, will filter the bottom 10 values in the column. The values will be computed based on aggregate function applied to the filter column. You can also specify another other column for ranking. |
| Top/Bottom N% | Top/Bottom N% is similar to Top/Bottom N option, except that it returns N% of values from the column. For example Top 5%, will filter the top 5% values of the column. |
If the listed values under each of the option does not meet your needs, Zoho Analytics allows you to define your own custom values. You can add your custom ranges, Top/Bottom N and N% values by clicking Add New Range button under the corresponding option.
Text type:
The text type column can be filtered using the following options.
Individual Value
This allows you to filter the chart by actual value. All the distinct values from the column will be listed with a checkbox. Select the value to include or exclude from the chart. You can select multiple values using the shift + click option. A Search box is also available to find the required values.
Wildcard
Wildcard filter allows you to filter by specifying filter criteria. The following table lists the possible conditions for filtering.
| Option | Description |
| Exactly Matches | Filters all the values that exactly match the search term. |
| Does Not Match | Filters all the values that do not match the search term. |
| Contain | Filters all the values that contain the search term. |
| Does Not Contain | Filters all the values that do not contain the search term. |
| Start With | Filters all the values that start with the search term. |
| Does Not Start With | Filters all the values that do not start with the search term. |
| End With | Filters all the values that end with the search term. |
| Does Not End With | Filters all the values that do not end with the search term. |
You can construct filter criteria with multiple conditions and join the condition using (AND) or (OR) operator. You can specify the join operator by clicking the link adjacent to the conditions.
By default, conditions from last to first will be grouped. i.e., when you have three conditions, the third and the second will be joined, and the result will then be joined with the first. You can change the default grouping of the conditions if needed. To modify, click the Edit link next to the Criteria Expression. Modify the filter criteria as required, and then click OK.
Note:
- The search terms are not case-sensitive.
- You can specify up to 15 conditions for filtering data.
Date type:
The following tables list all the possible options for filtering DATE type columns.
When you select Actual Values for a Date column dropped in the Filter shelf the following are the options available for filtering.
| Option | Description |
| Year | Select this option to filter date values based on specific years |
| Quarter | Select this option to filter date values based on specific quarters |
| Month | Select this option to filter date values based on specific months |
| Week | Select this option to filter date values based on specific weeks |
| Date | Select this option to filter based on specific date values |
| Date & Time | Select this option to filter based on specific date & time values |
| Ranges | Select this option to filter values based on specific date ranges |
To enter a custom date range, under Ranges option click Add New Range. In the Add New Range dialog box that appears, type dates in the From and To boxes or click the calender icon to open the calendar to select the required dates and then click Add.
When you select Seasonal for a Date column dropped in the Filter shelf the following are the options available for filtering.
| Option | Description |
| Quarter | Select this option to filter date values based on quarters present across all years in the column. E.g., Q1, Q2. |
| Month | Select this option to filter date values based on months across all years. E.g., January, February. |
| Week | Select this option to filter date values based on weeks across all years. E.g., Week 1, Week 2. |
| Week Day | Select this option to filter date values based on week day across all years. E.g., Sunday, Monday. |
| Day of Month | Select this option to filter date values based on day of month across all dates. E.g., 1 to 31. |
| Hour | Select this option to filter date values based on hours in a day. E.g., 0 to 23hrs |
When you select Relative for a Date column dropped in the Filter shelf the following are the options available for filtering.
| Option | Description |
| Common | Select this option to filter data values based on the common relative (relative to current time) periods. E.g., Last 1 Hour, Today, This Month etc., |
| Quarter | Select this option to filter data values based on relative period quarters E.g., This Quarter, Last 3 quarters, Next Quarter etc., |
| Month | Select this option to filter data values based on relative period months E.g., Last Month, Next 6 Months etc., |
| Week | Select this option to filter data values based on relative period week E.g., This Week, Last 3 Weeks etc., |
| Day | Select this option to filter data values based on relative period day E.g., Today, Next 5 Days etc., |
| Hour | Select this option to filter data values based on relative period hour E.g., Last 1 Hour, Last 12 Hours etc., |
After you have dropped the column and selected one or more values to filter the selected filter items appears in the third box on the right. You can Include or Exclude the selected values from the report that you are designing by choosing the appropriate option on top of this filter items box.
Once you are done with selecting the appropriate filters, select Click here to Generate Graph link or View Mode button in the toolbar. Notice that only the data that matches the filters you have defined will be displayed.
Note:
- You could apply any number of filters for a report that you design. When multiple filters are applied the data is filtered by adding all the filter conditions i.e., all the filter conditions should be met for the data to be shown part of the report.
User Filters
Zoho Analytics allows you to include dynamic filtering capability in the reports view mode through User Filters. User filters enable your users who access the report, to apply filters on the report data displayed using the filter columns exposed as part of User Filters. The filter columns included in User Filters can be displayed using a variety of display components like Drop Down box, Slider, Date range chooser etc., according to your needs.
Following sections describe in detail the User Filters for various column types (Data types).
User Filters for String (Categorical) Column Type
User Filters for Numeric and Currency Column Type
User Filters for Date Column Type
How User Filters Work?
Zoho Analytics allows you to provide multiple user filters in a report. Users who view the report can apply any number of user filters provided, in any order they want. When a user applies more than one user filter on a report, then the data is by AND'ing all the filter conditions i.e., all the filter conditions should be met for the data to be shown part of the report.