Training Ask Zia
Ask Zia natural language interface understands your data model to answer your questions appropriately. However, it may not interpret every domain-specific terminals (language parols). In such scenarios, you can train Ask Zia to learn your domain-specific skills to answer your questions.
In this section let's see how to train Ask Zia.
Manage Synonyms
When you draft a question, the business term you use may differ from the actual column name from which you want to fetch data. The synonyms option helps you to bridge this difference. It allows you to map the terms in natural language with the corresponding column in your data set.
For example, in a Sales data set you might ask for the Revenue Trend. Your actual column with revenue data may be named as Amount. Using the synonyms you can specify that the term Revenue is referring to the Amount column. Now, Ask Zia will get the data from the column Amount whenever you ask for Revenue. You can specify any number of synonyms for your data.
Follow the below steps to add synonyms for your data.
- Click the Settings icon at the top right of the Ask Zia screen and then select Manage Synonyms.
- The Manage Synonyms dialog will open. All the tables and the corresponding column names will be listed at the left. The Synonyms Settings will be given at the right.
You can specify the synonyms at the following three levels.
Table Synonyms
Table Synonyms allow you to specify other terms that refer to the table name. Enter the Table Synonyms as comma separated values.
You may have columns with the same data in multiple tables. For example, the sales person column will be available in both the Agents table and the Sales table. When you use this column in a query, Ask Zia will rank the columns from the tables based on the Table Priority specified and gives preference to the higher priority column for generating reports. You can also block the table from being used in the query using the Blacklist for Ask Zia option.
Column Synonyms
Column Synonyms allow you to specify other terms that refer to the column name. Select the column to open the settings. Enter the Column Synonyms as comma separated values.
You may have similar data in multiple tables. When you use this column in a query, Ask Zia will rank the columns based on the Column Priority specified and choose the column for generating reports. In case two or more columns have the same priority, then the Table Priority will be considered for ranking.
Zoho Analytics provides a wide range of functions for each data type. When you use a column in your question, Ask Zia will try to apply the best possible function over your column. You can also set the Default Function to be applied over the columns when it is called in the query.
Synonym suggestion by ChatGPT
Ask Zia supports integration with ChatGPT, which provides synonym suggestions for the column. This option will be available when you set up the integration with ChatGPT.
Click the Suggest synonyms option. Synonyms for the column name will be listed. Select the needed terms to add as column synonym.
Refer how to integrate with ChatGPT.
Data Synonyms
For text columns, Ask Zia allows you to specify synonyms for the columns' data using the Data Synonyms tab.
All the column's data will be listed in the Column Data section. You can sort the list by ascending, descending, or by frequently used order. You can also search for data. Select each value and then specify the corresponding synonyms.
Note:
- Data Synonyms will not be available for columns marked as personal.
- Data Synonyms will not be available for live connect tables.
Invoking Ask Zia Settings from Table
You can invoke the Ask Zia Settings dialog from one of the following interfaces.
Using Table Edit Design
Follow the below steps to customize the settings using Table Edit Design.
- Open the table and click Edit Design.
- Modify the Synonyms, Default Function and Column Priority field sections.
- Click Save.
Using Column Settings
You can also invoke the Ask Zia Settings using column settings. Follow the below steps to do this.
- Open the table.
- Right-click the column and then select Ask Zia Settings.
- The Ask Zia Settings dialog will open. Customize the setting.
- Click Save.