Constructing Questions for Ask Zia
You can ask your question to Zia in plain English. Zia will understand your question's intent and will reply with the most appropriate report that matches your question. However, there can be some communication gaps like how it exists among people.
This section explains how best you can communicate with Ask Zia.
How to Construct Questions?
Ask Zia can understand the intent in your questions. It can resolve ambiguity and generate the best possible insights for your questions. The questions you construct can be one of the following types.
Structured Question
Your question can be in a structured language e.g.,
Show me the sales grouped by country for the year 2018
Unstructured Question
Your question can be in an unstructured fragment phrase e.g.,
India sales in 2019
WH Questions
You can ask a 'WH' question. Ask Zia recognizes the 'WH' questions such as What, When, who, which e.g.,
What is the last year profit?
Explicit Information
Your question states explicit information in your data. e.g., Let's say you have Sales and Region columns in your dataset. The below question will get the total sales for each region.
Get me the sales across the regions
Implicit Information
Your question contains implicit information. Ask Zia will identify the terms such as monthly, yearly, daily, quarterly. e.g., for the below question, Zia will recognize the term Monthly, identified a date column in your data set and plots the sales across months.
Monthly Sales
Column Value
Your question can contain a value from a column. In this case, West is a value in the column Region. Ask Zia will identify this and excludes the data for the west region.
Get me sales across regions except west
Across Tables
You can ask for metrics across tables in your dataset. Ask Zia will interpret it based on how you have joined the tables using Lookup column. In this example, the column Sales is from the Sales table and the column Targeted Sales is from Regional Target table.
sales vs target by region
Formula Columns
You can ask a metric from a formula column available in your dataset.
Typographical Error
Your question can contain a typographical error. Ask Zia can interpret questions with incomplete, incorrect words. In this case, the term 'salse' will be matched with sales
Show me the salse by salesperson
What can be achieved in Ask Zia?
Ask Zia supports creating the following types of queries.
Ask for a Metric
You can ask for a single metric or multiple metrics in a question like sales, my top salesman, what is the most sold product, etc.,
Single Metric
You can ask for a single metric in your question. The following question will get the total profit for last year as a Numeric KPI widget.
What is the last year profit?
Multiple Metrics
You can ask for multiple metrics in a question. The below question gets Total Sales and Total Profit as a pie chart.
Sales vs profit
Apply Summary Functions
Zoho Analytics provides a wide range of summary functions like Sum, Count, Average, Running Total etc., Ask Zia will try to apply the best possible function over your column. You can choose to change them in your question.
Summary Function
You can choose the apply the supported summary functions over a metric column by explicitly specifying them in your question. The below example applies count over the sales column and plots it across months.
what is the number of orders we have every month?
Advanced Summary Function
Ask Zia can also apply advanced summary functions. The below question applies the advanced summary function Running Total over the Sales column and calculates it across the quarters.
show me the running total of sales.
Predictive Analysis
Ask Zia supports predictive analysis. You can easily predict the data trend or forecast your future data.
Forecast
You can forecast the data by simply asking for the future data. The following example will predict how the future sales for the next 6 months that will most likely be.
Get me the sales for next 6 months
Trend Line
Ask Zia supports adding the Trendline for your chart. You can predict the data trend using the terms trend or trendline in your question. In the following example, the sales trend is predicted.
Show me the Sales Trend
Forecasting Trend
Ask Zia can add both forecasting and trendline to you chart. The following question forecast the sales for the next 6 months and also predict the sales trend.
Show me the Sales Trend for next 6 months
Statistical Measures
Find the correlations between metrics
Correlation helps find if and how strongly two measures are related to each other. If a measure or variable increases or decreases together, they are positively correlated. If one measure tends to increase and another one decreases, then they are negatively correlated.
Zia computes the correlation using Pearson's Correlation Coefficient, which is the covariance of the two variables to the product of their standard deviations.
- R > 0.5 indicates a positive linear relationship.
- R value between - 0.5 and 0.5 (- 0.5 < R < 0.5) indicates no linear relationship.
- R < - 0.5 indicates a negative linear relationship.
Sample queries
Give me or find the correlation between Sales and Cost
Period wise Categorical Correlation: Give me the quarterly correlation of Sales and Cost
Find Trends Strength in the data
Trend strength is a statistical measure used to determine how strongly data is moving in an upward or downward direction. It helps assess whether a trend is likely to continue or weaken.
- If the value ranges between 0.0 to 0.3, it indicates a weak trend meaning the data does not follow a clear upward or downward path.
- If the value ranges between 0.3 to 0.7, then it indicates a moderate trend meaning the data shows a relatively consistent direction (upward or downward), but with occasional fluctuations or deviations.
- If the value ranges between 0.7 to 1.0, it indicates a strong trend meaning the data consistently moves in one direction (upward or downward).
Show me the regions with an upward trend
Group the Metric Column
You can group the metric column using phrases like sales by /group by / categorized by / across / wise ... You can also categorize the metrics by geo location to create Geo Visualization.
The following types of groupings are supported.
- Single Metric by a Single Dimension
- Single Metric by Multiple Dimensions
- Multiple Metrics by a Single Dimension
- Multiple Metrics by Multiple Dimensions
- Metrics by Geo Location
Single Metric by a Single Dimension
In this example, the Sales column is grouped into months by the Date column.
monthly sales
Single Metric by Multiple Dimensions
In this example, the Sales column is grouped by the Date and the Region columns.
what is my sales across the regions every month?
Multiple Metrics by a Single Dimension
In this example, the Sales and the Profit columns are grouped by the Date column.
Profit and sales across months
Multiple Metrics by Multiple Dimension
In this example, the Sales and the Profit columns are grouped by the Date and the Region columns.
Sales and profit across months for each region
Ask Zia recognizes the geo location by name or Geo Alpha code such as USA, IND, NY etc., and creates the appropriate geo visualization.
Sales by States in USA
Apply Filter Criteria
You can apply single criteria or multiple criteria of filters in a question. The following are the supported filter criteria.
Show me the sales across months where the region is west
Salesperson by win rate and won amount where the deal size >12k
Slice by Range
You can slice data by range using special criteria like Top 10, Bottom 5, Highest, lowest, most, recent. In this example, we have filtered top 10 salespersons.
My top 10 salespersons by win rate
Exact Dates
You can filter data for a specific date such as 2019, March 2018, 12/3/2019... In this example, we've filtered the tickets escalated on 17th of March 2018.
Escalated tickets on 17 march 2018
Date ranges
You can filter data for a specific date range. In this example, the Revenue for a specific period i.e., from 3rd March 2018 to 3rd September 2018 is filtered.
Show me the revenue by salespersons from 3rd Mar 2018 to 3rd Sept 2018
Relative Dates - You can filter data for a relative period such as This Month, Last Quarter, Today... In this example, the Revenue for the period of last 1 year is filtered.
Show me the revenue across months for the last year
Filter Negation - You can exclude a set of data from the report using the filter negation such as exclude, except, ignore, without... In this example, we've excluded the west region sales.
Sales across regions except west
Sort Data
You can choose to sort the report either by the metric column or by columns to group the metric. In this example, the report is sorted based on the Y-Axis column Revenue.
Revenue by Salespersons sort by Revenue
Keywords for Ask Zia
The following is the list of keywords that Ask Zia can interpret and create appropriate insights.
Summary Options | |
| Functions | Keywords |
| Summary | sum, total, tot |
| Minimum | minimum, min |
| Maximum | maximum, max, highest, high |
| Count | count, number, no, total number, distinct count, unique, unique count |
| Others | standard deviation, std dev, variance |
Advanced Summary Options | |
| Functions | Keywords |
| Running Total | running total, running tot., running sum |
| Percentage of | percentage, total percentage, %, percent, percentage of total, total %, % of total, pct of total, % of sum, sum percentage, sum pct, contribution, contribution of total |
| Difference From | difference, difference from, diff, growth |
| % of Difference From | % of difference, pct of difference, difference %, % diff, difference percentage, difference in percentage, |
| % of Previous Value | percentage of previous, % of previous, pct of previous, prev %, previous value % |
Group by Options | |
| Functions | Keywords |
| Numeric | actual, range, as range, dimension, as dimension |
| Date-Actual | year, yearly, year over year, yoy, absyear quarter, quarterly, quarter over quarter, qoq, absquarter month, monthly, month over month, mom, month and year, absmonth week, weekly, week over week, wow, week and year, absweek day, daily, day over day, absday date, hour, hourly, minute, second |
| Date-Seasonal | seasonal day, seasonal month, seasonal year, seasonal week, seasonal quarter |
Filtering Options | |
| Functions | Keywords |
| Numeric | >, >=, greater than, above, over, beyond, higher than, more than, exceeds <, <=, lesser than, lower, lower than, less than, below, under equal to, equals to, equals, =, between |
| Units and Currency | thousands, k, millions, m, mn, billions, b, bn, Lakhs, L, Crores, C, Rupees, RS, ₹, Dollars, $ |
| By Range | top 10, top few, top, top most, highest, best bottom 10, bottom few, bottom, lowest, worst |
| Text | starts with, starts with, ends with, contains, is |
| Date-Actual | 2018, 2019, Q1 2019, Q4 of 2018, quarter 1 of 2019 January 2019, Jan 2019, 1/2019 15th october , 30 july, nineth july 2017, third may 2016, 2 feb 2001, 2019 mar 4, 17/feb, twenty six october |
| Date-Seasonal | June, may, jul, oct, Sunday, saturday, thurs, tue 1st quarter, 2nd quarter, second quarter, third quarter, fourth quarter, first quarter, quarter 4, quarter1 |
| Date-Relative | this year, previous year, last year, past year, recent year, previous 3 years, next 3 years, last 3 year, recent 3 years, last nine years, previous few years, recent few years, past few years, recent few decades, previous few decades, past few decades, next few decades, last few years, last decade, recent decade this quarter, previous quarter, last quarter, this quarter, recent quarter, previous 9 quarters, last 9 quarters, next 9 quarters, recent 5 quarters, previous five quarters, last three quarters, recent few quarters, next few quarters, previous few quarters, past few quarters, last few quarters this month, previous months, last months, past month, recent months, previous 6 months, next 6 months, last 6 months, recent 6 months, previous thirteen months, recent seventeen months, previous few months, recent few months, previous month, current may, previous november, this apr, past mar this week, last week, past week, recent week, last few weeks todat, yesterday, tomorrow, recent 3 days, past 21 days, recent few days, next few days, next day, recent day recent 22 hours, recent 13 hours, next hour, past hour |
| Filter Negation | not, except, excluding, without, neither, other than, ignoring, apart. apart from, ! =, exclude, exceeding |
Sorting Options | |
| Functions | Keywords |
| Ascending | ascending order, ascending, increasing order, alphabetical order, alphabetical order (a-z) |
| Descending | descending, descending order, decreasing order, alphabetical order (z-a) |
| By Column | sorted, sort, sort by column |