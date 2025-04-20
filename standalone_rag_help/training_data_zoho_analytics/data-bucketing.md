Bucket Columns
Data bucketing, or binning, is the method of grouping data points based on specific conditions. For instance, categorize customers based on the value of their purchases. Bucketing reduces the number of distinct values in the data by assigning each data point to a specific bin based on the criteria. It facilitates the transformation of numerical data into different categorical bins and makes data analysis easier. Data binning can be applied to both Numerical and Categorical data.
Significance of Bucketing Columns
- Reduces Data Variability: Though data variability shows the dispersion of data points, high variability can make data interpretation difficult. Grouping data points helps reduce data complexity by smoothing out variations and making trends and patterns more evident.
- Handling Outliers: Binning can mitigate the effect of outliers by grouping them into more significant categories, reducing their impact on the final results of the analysis.
Best Practices for Bucketing Columns
- Evaluate the Data: Before binning the data, understand the characteristics of the data like its skewness, range and its distribution. Choose bucketing for columns that have high cardinality (number of data points).
- Choose appropriate number of buckets and the range: The number of buckets or bins has a direct effect on the results of the analysis and how the data is interpreted. A small number of bins can lead to a loss of detail, and a many buckets can increase the complexity. Hence, choose the number of buckets based on the range of the data and the purpose of the analysis.
- Descriptive Labels: Ensure that the bucket labels are clear, making it easy for the users to understand how the data values grouped.
Creating Buckets in Zoho Analytics
- Access the table view.
- Click the Add option on the tool bar and choose Bucket Column from the drop-down menu.
(or)
Right-click the column you need to create buckets for and choose Add Buckets from the drop-down. - The Add Bucket Column dialog will open. Give a suitable Title for the Bucket Column that is to be created. Also add a Bucket Description to help users understand the basis on which the data is bucketed.
- Choose the column that should be used for bucketing from the Column To Apply On field.
- Input the conditions for bucketing the data.
- Specify the Bucket Label that will represent the values or elements inside that bucket.
- Choose the conditions based on which the data should be classified. The conditions will be listed based on the data type of the column. Click Add Condition to include additional criteria.
- Specify the Values for each condition.
- Click Add New Bucket Label to group data based on different conditions.
- Selecting the checkbox Labels for Unmatched Values will group all the data points that do not fall under any of the given conditions into one bucket. Specify the labels that should be given for that bucket.
- Click Save.
Creating Buckets - Numeric Data Type
Let's consider the case where you want to classify the amount based on the sales value.
- Right-click the Sales column and choose Add Bucket from the drop-down menu.
- Specify the Bucket Column Name as Amount Tier.
- Specify the Bucket Label as 0 - $500 and choose the condition Less Than to group the data values below 500.
- Click Add New Bucket Label. Enter the second Bucket Label as $501 - $1000. Choose the Condition as Between. Specify the values as 501 and 1000.
- Similarly, specify the conditions for other buckets as shown in the below image.
- Click Save.
Creating Buckets - Text Data Type
Consider the case where you need to group countries based on the regions.
- Right-click the Country column and choose Add Bucket from the drop- down menu.
- Specify the Bucket Column Name as Region.
- Enter the first Bucket Label as APAC.
- Choose the Condition as In and specify the Values as India, China, Malaysia, and Singapore.
- Click Add New Bucket Label.
- Specify the Bucket labels, conditions, and data values that should be used for grouping, as shown in the below image.
- Select the Case-Sensitive checkbox if you want the grouping to differentiate between uppercase and lowercase letters.
- Click Save.
A new column Region will be created, and the countries will be bucketed based on the given conditions as shown in the below image.