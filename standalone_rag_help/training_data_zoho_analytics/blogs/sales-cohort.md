A cohort is a group of subjects who share common characteristics in a given time span. Cohort analysis deals with breaking data into related groups for easy and effective analysis.
A cohort can be of great use in analyzing your sales data. Cohort Analysis aides users to analyze the patterns and trends of data within a particular interval.
Zoho Analytics with its powerful reporting capabilities allows you to create dynamic cohorts in a few clicks. In this help document we will discuss some scenarios where cohorts can be of great use in sales analytics. These solutions can be applied to the data present in Zoho CRM/Salesforce CRM or any such similar data source.
The following section contains solutions for the below questions:
1. How can I create a cohort to analyze customer retention?
2. How is a sales cohort useful in keeping track of the team's performance?
3. How do I measure the conversion rate of my leads to potentials using cohorts?
4. How can I create a cohort to calculate the win rate?
Solutions
1. How can I create a cohort to analyze customer retention?
Query 1: Customer Start Date
SELECT "Customer ID", STR\_TO\_DATE(min("Date of Subscription"), '%Y-%m-%d') "Date" FROM "Invoice" GROUP BY "Customer ID"
Query 2: Invoice and Recurring Month
SELECT INV."Invoice ID" "Invoice ID", INV."Date of Subscription" "Date", INV."Customer ID" "Customer ID", INV."Invoice Owner" "Invoice Owner", STR\_TO\_DATE(CUS."Date", '%Y-%m-%d') 'Min Date', date\_format(CUS."Date", '%Y%m') "Month and Year", period\_diff(date\_format(INV."Date of Subscription", '%Y%m'), date\_format(CUS."Date", '%Y%m')) 'Month' FROM "Customer Start Date" CUS INNER JOIN "Invoice" INV ON INV."Customer ID" = CUS."Customer ID"
Query 3: Customer Count by Month
SELECT date\_format("Date", '%Y%m') "Month and Year", count("Customer ID") "Customer Count" FROM "Customer Start Date" GROUP BY "Month and Year"
Aggregate Formula Recurring % :
count("Invoice ID")\*100/avg("Customer Count by Month"."Customer Count")
2. How is a sales cohort useful in keeping track of the team`s performance?
Query 1: Invoice Count by Owner
SELECT "Invoice Owner", COUNT("Invoice ID") "Invoice Count" FROM "Invoice" GROUP BY "Invoice Owner"
Query 2: Invoice and Recurring Month
SELECT INV."Invoice ID" "Invoice ID", INV."Date of Subscription" "Date", INV."Customer ID" "Customer ID", INV."Invoice Owner" "Invoice Owner", STR\_TO\_DATE(CUS."Date", '%Y-%m-%d') 'Min Date', date\_format(CUS."Date", '%Y%m') "Month and Year", period\_diff(date\_format(INV."Date of Subscription", '%Y%m'), date\_format(CUS."Date", '%Y%m')) 'Month' FROM "Customer Start Date" CUS INNER JOIN "Invoice" INV ON INV."Customer ID" = CUS."Customer ID"
3. How do I measure the conversion rate of my leads to potentials using cohorts?
Query 1: Lead tracking
SELECT \*, CONCAT(LEFT("month\_Created Time1", 3), ' ', YEAR("Created Time")) "Month & Year", CONCAT('Month - ', period\_diff(date\_format("Last Modified Time", '%Y%m'), date\_format("Created Time", '%Y%m'))) "Month Diff" FROM "Leads"
Query 2: Lead Count - Month & Year wise
SELECT "Month & Year", COUNT("LEADID") FROM "Lead tracking" GROUP BY "Month & Year"
4. How can I create a cohort to calculate win rate?
Query 1: Potential Count by Month
SELECT date\_format("Created Time", '%Y%m') "Month and Year", COUNT("POTENTIALID") "Total Potential" FROM "Potentials" GROUP BY 1
Query 2: Potential Conversion by Month
SELECT p."POTENTIALID" "POTENTIALID", date\_format(p."Created Time", '%Y%m') "Month and Year", period\_diff(date\_format(pst."Modified Time", '%Y%m'), date\_format(p."Created Time", '%Y%m')) "Month" FROM "Potentials" p LEFT JOIN( SELECT "POTENTIALID", max("Modified Time") "Modified Time" FROM "Potential Stage History" GROUP BY 1 ) pst ON p."POTENTIALID" = pst."POTENTIALID" WHERE p."Stage" = 'Closed Won'