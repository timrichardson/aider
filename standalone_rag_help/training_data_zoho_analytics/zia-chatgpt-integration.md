ChatGPT Integration
Zoho Analytics integration with ChatGPT makes working with data much easier and saves time spent finding formulas, building complex queries, and discovering datasets. It also helps to find synonyms for data columns to train Ask Zia effectively and enhance natural language processing capabilities.
Note:
- ChatGPT Integration feature is only available for Premium and Enterprise plans.
- Only Account, Organization, and Workspace Admins can use this ChatGPT integration feature.
- ChatGPT Integration - Setup
- Formula Suggester
- SQL Query Suggester
- Discover External Datasets
- Synonym Suggester
- Frequently Asked Questions
ChatGPT Integration - Setup
The Account Admin can configure the ChatGPT integration in Zoho Analytics.
Follow the below steps to integrate ChatGPT with Zoho Analytics,
- Login to your Zoho Analytics account
- Click Organization Settings > Controls / Configurations > Feature Controls > ChatGPT Integration
- Enter your ChatGPT secret key.
- Select the desired features by checking the boxes.
If you want to improve the accuracy and relevance of the ChatGPT integration, enable the toggle button Optimize ChatGPT results by sharing workspace metadata. Doing this will share the metadata to OpenAI Embedding APIs, which use Retrieval-Augmented Generation (RAG) to enhance the quality of responses.
RAG uses embeddings (numerical representation of text) to find relevant information from your data and includes it in the response generation. This helps ChatGPT provide more accurate and relevant answers based on your specific data.Note:
- Enabling this option shares only metadata with OpenAI Embedding APIs. No actual data is shared with ChatGPT.
- The Metadata includes the following:
- Table Names
- Column Names
- Data Type
- Synonyms
- Descriptions
- There is a typical pricing difference between OpenAI APIs and OpenAI Embedding APIs. For the most up to date pricing information, visit the OpenAI Pricing page.
- Select the checkboxes to grant access to the Organization and Workspace Administrators for using this integration.
- Click Apply. ChatGPT integration will now be enabled.
Formula Suggester
Finding the correct formula for analyzing data can be tedious and time consuming. With the Ask Zia: Formula suggester, you can create formulas by asking questions in simple natural language and get intelligent suggestions.
Follow the below steps to use Formula Suggester while creating formula columns,
- From the Explorer tab of the Workspace, select the table to which you want to add the formula column.
- Select Add > Formula Column option from the toolbar or right click on a column in the table and select Add Formula > Formula Column
- The Add Formula Column wizard will open.
- Click the drop down icon of the Zia Formula Suggester.
- Enter your question in the Formula field and then click Generate.
- The Hints field gives examples of how a question could be asked.
- The formula for the defined use case will appear in the Formula Column dialog box. Review the generated formula and make modifications if needed.
- Click Save.
SQL Query Suggester
You can build complex queries by providing inputs in natural language, thus saving a significant amount of time to construct the queries. Users who don't know SQL or have a basic knowledge of SQL can use this feature to construct complex SQL queries.
Follow the below steps to use Query Suggester while creating formula columns,
- Open the desired workspace and click Create from the explorer tab.
- Click the drop down icon of the Zia Query Generator.
- Enter your question in the Ask Zia: Query Suggester field and selected the related tables.
- The Hints field gives examples of how a question could be asked.
- Click Generate SQL.
- The query for the defined use case will be generated. Review the generated query and make modifications if needed.
- Click Save.
Discover External Datasets
You can easily find public datasets from the web by asking questions, and import the same into Zoho Analytics. This data can then be used for further analysis.
Follow the below steps to import public datasets,
- From the Zoho Analytics homepage, click Import your Data or click Create from the explorer tab and select New Table/Import Data.
- Select Find External dataset using Ask Zia from the listed data sources.
- If you haven’t enabled the ChatGPT integration, then ChatGPT Integration wizard will open. Select the features for which you wish to enable the integration and then click Proceed.
- The Find External Data wizard will open. Specify the Table Name.
- Explain the case for which you are trying to obtain the public dataset in Ask Zia: Find External Data field and then click Generate.
- The Data Preview section displays the first few records of the generated data.
- Click Create. A table will be created and you can create reports and dashboards over the imported data.
Synonym Suggester
You can get alternative suggestions for column names to get conversational insights using NLP capabilities.
Follow the below steps to use Synonyms Suggester while creating formula columns,
- Right click the column name and select Ask Zia Settings from the list.
- Click Suggest to get the related words.
- The synonyms for the selected column will be listed.
- Select the words to be listed in the Column Synonyms field.
- Click Save.
Frequently Asked Questions
1. Will my data be shared with ChatGPT while using this integration?
No, your data will not be shared with ChatGPT. Only metadata—such as table names, column names, data types, synonyms, and descriptions—is shared with OpenAI Embedding APIs to improve the accuracy and relevance of results. This metadata is used when utilizing features like Synonym Suggester, SQL Query Suggester, and Formula Suggester. OpenAI Embedding APIs use this metadata to retrieve relevant information, helping ChatGPT provide more contextually accurate suggestions without sharing your actual data.
2. Who can configure the ChatGPT integration?
The Account Admin can configure the ChatGPT integration.
3.Who can access the ChatGPT integration?
The Account Admin can access the integration and he/she can allow other Organization and Workspace Administrators to use this integration.
4.Is it possible for me to modify the formulas or SQL queries generated by Zia?
Yes, the Account Admin and the Organization Admin can modify the formulas or SQL queries generated by Zia.
5. I get no responses for a few prompts. Why?
The response generated in the formula field or the query field is provided by ChatGPT. If your prompts do not contain sufficient information or context for the AI model to understand your request, it may not be able to provide a response. Please try rephrasing your prompt with the necessary information and try again.
6. What are the plans that support the ChatGPT integration?
The ChatGPT integration is available for Premium and Enterprise Plans.