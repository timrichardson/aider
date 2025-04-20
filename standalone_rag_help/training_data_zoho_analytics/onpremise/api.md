Zoho Analytics On-Premise API
Zoho Analytics On-Premise API offers wide range of functions to help developers build & manage powerful reporting and analytical capabilities for their business application needs. You can add powerful business intelligence capabilities to your product/application, build add-ons to analyze data from third-party business applications (eg., Google Adwords, Google Analytics, CRM systems etc., ) that you use and do much more.
Easy to use programming language wrappers called "Client Libraries" are provided to conveniently use the Zoho Analytics On-Premise API from within your familiar programming language like Java, C#, Python, PHP, GO, and CURL.
Important Notations
We have used a few notations in this document. Here are their meanings
is the host name of the Zoho Analytics server.
is the port that Zoho Analytics runs on. By default, this is 8443.
Here is how you can get your web client port
- Login to the application.
- Get the web client port from the browser URL. E.g.
https://BI-server:8443/ZDBHome.cc
here, 8443 is your web client port number.
is the email address associated with your Zoho Analytics user login.
Prerequisites
The following are the prerequisites to use Zoho Analytics On-Premise API
Note: It is mandatory to use HTTPS in all API requests instead of Request URI. HTTP is not supported
Auth Token
Browser Mode : URL
https://:/iam/apiauthtoken/create?SCOPE=ZROP/reportsapi
https://:/iam/apiauthtoken/create?SCOPE=ZROP/reportsapi
https://:/iam/apiauthtoken/create?SCOPE=ZROP/reportsapi
https://:/iam/apiauthtoken/create?SCOPE=ZROP/reportsapi
https://:/iam/apiauthtoken/create?SCOPE=ZROP/reportsapi
https://:/iam/apiauthtoken/create?SCOPE=ZROP/reportsapi
API Mode : URL
https://:/iam/apiauthtoken/nb/create?SCOPE=ZROP/reportsapi&EMAIL\_ID=emailid&PASSWORD=password
https://:/iam/apiauthtoken/nb/create?SCOPE=ZROP/reportsapi&EMAIL\_ID=emailid&PASSWORD=password
https://:/iam/apiauthtoken/nb/create?SCOPE=ZROP/reportsapi&EMAIL\_ID=emailid&PASSWORD=password
https://:/iam/apiauthtoken/nb/create?SCOPE=ZROP/reportsapi&EMAIL\_ID=emailid&PASSWORD=password
https://:/iam/apiauthtoken/nb/create?SCOPE=ZROP/reportsapi&EMAIL\_ID=emailid&PASSWORD=password
https://:/iam/apiauthtoken/nb/create?SCOPE=ZROP/reportsapi&EMAIL\_ID=emailid&PASSWORD=password
Sample Response:
The following is a sample response for a Auth Token request.
#
#Wed Jun 29 03:07:33 PST 2013
AUTHTOKEN=bad18eba1ff45jk7858b8ae88a77fa30
RESULT=TRUE
The following is a sample response for a Auth Token request.
#
#Wed Jun 29 03:07:33 PST 2013
AUTHTOKEN=bad18eba1ff45jk7858b8ae88a77fa30
RESULT=TRUE
The following is a sample response for a Auth Token request.
#
#Wed Jun 29 03:07:33 PST 2013
AUTHTOKEN=bad18eba1ff45jk7858b8ae88a77fa30
RESULT=TRUE
The following is a sample response for a Auth Token request.
#
#Wed Jun 29 03:07:33 PST 2013
AUTHTOKEN=bad18eba1ff45jk7858b8ae88a77fa30
RESULT=TRUE
The following is a sample response for a Auth Token request.
#
#Wed Jun 29 03:07:33 PST 2013
AUTHTOKEN=bad18eba1ff45jk7858b8ae88a77fa30
RESULT=TRUE
The following is a sample response for a Auth Token request.
#
#Wed Jun 29 03:07:33 PST 2013
AUTHTOKEN=bad18eba1ff45jk7858b8ae88a77fa30
RESULT=TRUE
Response Details:
\* #-COMMENT Auth Token generated date.
\* AUTHTOKEN The permanent Auth Token (Alpha numeric value) generated for
Zoho Analytics On-Premise API access.
\* RESULT Value is TRUE if the Auth Token is generated successfully.
\* #-COMMENT Auth Token generated date.
\* AUTHTOKEN The permanent Auth Token (Alpha numeric value) generated for
Zoho Analytics API access.
\* RESULT Value is TRUE if the Auth Token is generated successfully.
\* #-COMMENT Auth Token generated date.
\* AUTHTOKEN The permanent Auth Token (Alpha numeric value) generated for
Zoho Analytics API access.
\* RESULT Value is TRUE if the Auth Token is generated successfully.
\* #-COMMENT Auth Token generated date.
\* AUTHTOKEN The permanent Auth Token (Alpha numeric value) generated for
Zoho Analytics API access.
\* RESULT Value is TRUE if the Auth Token is generated successfully.
\* #-COMMENT Auth Token generated date.
\* AUTHTOKEN The permanent Auth Token (Alpha numeric value) generated for
Zoho Analytics On-Premise API access.
\* RESULT Value is TRUE if the Auth Token is generated successfully.
\* #-COMMENT Auth Token generated date.
\* AUTHTOKEN The permanent Auth Token (Alpha numeric value) generated for
Zoho Analytics API access.
\* RESULT Value is TRUE if the Auth Token is generated successfully.
Authentication Token, also referred as Auth Token, is a unique token that authenticates the user to access his/her Zoho Analytics Account. This is a permanent user specific token, that needs to be passed along with every Zoho Analytics On-Premise API request.
Generating Auth Token
Users can generate a Auth Token using one of the following modes. You can generate it just once and use it for all your API calls.
- Browser Mode
- API Mode
Browser Mode
To generate Auth Token from your browser, follow the steps given below.
- Open a new tab in your browser and then access the url given in the sample.
https://:/iam/apiauthtoken/create?SCOPE=ZROP/reportsapi
API Mode
To generate Auth Token using API mode, send an HTTPS POST request to Zoho Analytics Accounts (webclientport/iam) using the URL format given in the sample.
https://:/iam/apiauthtoken/nb/create?SCOPE=ZROP/reportsapi&EMAIL\_ID=emailid&PASSWORD=password
Mandatory "POST" Parameters to be passed along with this URL are:
| Parameter | Description |
|---|---|
| EMAIL\_ID | Specify the email address associated with your Zoho Analytics user login. |
| PASSWORD | Specify your Zoho Analytics Password |
Managing Auth Tokens
You can access and manage all the active secret Auth Tokens of Zoho Analytics from the Zoho Analytics Auth Token page.
To access the active Auth Tokens:
- Go to
https://:/iam/u/h#sessions/userauthtoken
- The Active Authtoken page will list all the active secret Auth Tokens of your account.
- If required, you can remove or regenerate the Auth Token using the Remove and Re-Generate button respectively.
Important Note
- Generate a Single Auth Token and use it across all API calls in Zoho Analytics.
- In case the user has removed or regenerated the Auth Token, then the existing token will become invalid and cannot be used in API request.
- In case the user is deactivated, then all the Auth Token's of the user's account will become invalid.
Reporting Workspace
To use the Zoho Analytics On-Premise API, users should have already created a reporting workspace with required tables and reports in Zoho Analytics service using the browser based Web interface provided. You cannot use the API, if you do not have any reporting workspaces in your Zoho Analytics account. To know how to create a workspace, click here.
API Specification
Zoho Analytics On-Premise API uses HTTPS as the underlying transport protocol. It is based on REST principles. The following are the basic points of how the REST APIs are structured:
- Every table or report or dashboard in a Zoho Analytics workspace can be uniquely identified using a URL.
- The operation to be performed on the table/report/dashboard can be specified using the parameters in the URL.
- The additional payload required to perform the operation should also be specified as parameters in the URL.
- Every request has a response whose format can be controlled using parameters in the request URL.
It is important to understand the API specification clearly before referring to the actual API methods
Request Format
Sample Request:
The below URL adds a row in EmployeeDetails table in EmployeeDB workspace in a CSV format.
https://:/api/abc@zylker.com/EmployeeDB/EmployeeDetails?ZOHO\_ACTION=ADDROW&
ZOHO\_OUTPUT\_FORMAT=XML&ZOHO\_ERROR\_FORMAT=XML&authtoken=g38sl4j4856guvncrywox8251sssds
&ZOHO\_API\_VERSION=1.0
The below URL adds a row in EmployeeDetails table in EmployeeDB workspace in a CSV format.
https://:/api/abc@zylker.com/EmployeeDB/EmployeeDetails?ZOHO\_ACTION=ADDROW&
ZOHO\_OUTPUT\_FORMAT=XML&ZOHO\_ERROR\_FORMAT=XML&authtoken=g38sl4j4856guvncrywox8251sssds
&ZOHO\_API\_VERSION=1.0
The below URL adds a row in EmployeeDetails table in EmployeeDB workspace in a CSV format.
https://:/api/abc@zylker.com/EmployeeDB/EmployeeDetails?ZOHO\_ACTION=ADDROW&
ZOHO\_OUTPUT\_FORMAT=XML&ZOHO\_ERROR\_FORMAT=XML&authtoken=g38sl4j4856guvncrywox8251sssds
&ZOHO\_API\_VERSION=1.0
The below URL adds a row in EmployeeDetails table in EmployeeDB workspace in a CSV format.
https://:/api/abc@zylker.com/EmployeeDB/EmployeeDetails?ZOHO\_ACTION=ADDROW&
ZOHO\_OUTPUT\_FORMAT=XML&ZOHO\_ERROR\_FORMAT=XML&authtoken=g38sl4j4856guvncrywox8251sssds
&ZOHO\_API\_VERSION=1.0
The below URL adds a row in EmployeeDetails table in EmployeeDB workspace in a CSV format.
https://:/api/abc@zylker.com/EmployeeDB/EmployeeDetails?ZOHO\_ACTION=ADDROW&
ZOHO\_OUTPUT\_FORMAT=XML&ZOHO\_ERROR\_FORMAT=XML&authtoken=g38sl4j4856guvncrywox8251sssds
&ZOHO\_API\_VERSION=1.0
The below URL adds a row in EmployeeDetails table in EmployeeDB workspace in a CSV format.
https://:/api/abc@zylker.com/EmployeeDB/EmployeeDetails?ZOHO\_ACTION=ADDROW&
ZOHO\_OUTPUT\_FORMAT=XML&ZOHO\_ERROR\_FORMAT=XML&authtoken=g38sl4j4856guvncrywox8251sssds
&ZOHO\_API\_VERSION=1.0
Sample POST parameter
Parameters for EmployeeDetails table in EmployeeDB workspace.
&Name=Gary&Date Of Birth=12-Jun-1980&Country=USA&Salary=10000
Parameters for EmployeeDetails table in EmployeeDB workspace.
&Name=Gary&Date Of Birth=12-Jun-1980&Country=USA&Salary=10000
Parameters for EmployeeDetails table in EmployeeDB workspace.
&Name=Gary&Date Of Birth=12-Jun-1980&Country=USA&Salary=10000
Parameters for EmployeeDetails table in EmployeeDB workspace.
&Name=Gary&Date Of Birth=12-Jun-1980&Country=USA&Salary=10000
Parameters for EmployeeDetails table in EmployeeDB workspace.
&Name=Gary&Date Of Birth=12-Jun-1980&Country=USA&Salary=10000
Parameters for EmployeeDetails table in EmployeeDB workspace.
&Name=Gary&Date Of Birth=12-Jun-1980&Country=USA&Salary=10000
All API requests should be placed as HTTPS POST request. The request consists of the following components:
URI (Universal Resource Identifier. Also commonly known as URL)
Common Mandatory Parameters sent as Query String in the URL
Parameters sent via the body of the POST request.
URI
The URI points to the resource inside Zoho Analytics over which the action is to be performed.
https://:/api///
It consists of the following parts
The base URL
https://:/api
: This should be the Email Address associated with the user login of the owner of the workspace in Zoho Analytics
: This should be the name of the workspace on which the API is to be executed. (e.g., EmployeeDB)
: The name of the view (table or report or query table or dashboard name) over which the action is to be executed. (e.g., EmployeeDetails)
Parameters to be passed in Query String
The following snippet shows the common parameters that should be passed as Query string with the URI defined above:
?ZOHO\_ACTION=[IMPORT/EXPORT...]&ZOHO\_OUTPUT\_FORMAT=[XML/JSON/PDF/...]&ZOHO\_ERROR\_FORMAT=[XML/JSON]&authtoken=&ZOHO\_API\_VERSION=1.0
The control parameters such as "ZOHO\_ACTION" is mandatory and have to be sent as part of the query string in the URL. Refer to Common Parameters document to know more about the possible parameters that could be passed in the Query String.
Parameters to be passed via the body of POST Request
Apart from the parameters passed in the Query string, additional information needed for specific actions (such as values of row in a Add Row operation etc.,) needs to be passed as POST parameters
1=1&=....
The parameters should be encoded in application/x-www-form-urlencoded format (This is the default format used by any simple html form).
Note:
In the case of importing csv files multipart/form-data format should be used. (This is the default format used by html forms that contain file type fields used for uploading files)
Response Format
Sample Response : For ADDROW
Sample response to a request adding a row to the EmployeeDetails table in the
EmployeeDB workspace.
Sample response to a request adding a row to the EmployeeDetails table in the
EmployeeDB workspace.
Sample response to a request adding a row to the EmployeeDetails table in the
EmployeeDB workspace.
Sample response to a request adding a row to the EmployeeDetails table in the
EmployeeDB workspace.
Sample response to a request adding a row to the EmployeeDetails table in the
EmployeeDB workspace.
Sample response to a request adding a row to the EmployeeDetails table in the
EmployeeDB workspace.
XML Format:
xml version="1.0" encoding="UTF-8" ?




Gary
12-Jun-1980
10000
USA

xml version="1.0" encoding="UTF-8" ?




Gary
12-Jun-1980
10000
USA

xml version="1.0" encoding="UTF-8" ?




Gary
12-Jun-1980
10000
USA

xml version="1.0" encoding="UTF-8" ?




Gary
12-Jun-1980
10000
USA

xml version="1.0" encoding="UTF-8" ?




Gary
12-Jun-1980
10000
USA

xml version="1.0" encoding="UTF-8" ?




Gary
12-Jun-1980
10000
USA

JSON Format:
{
"response":
{
"uri": "/api/abc@zylker.com/EmployeeDB/EmployeeDetails",
"action": "ADDROW",
"result":
{
"column\_order":["Name","Date Of Birth","Salary","Country"],
"rows":
["Gary","12-Jun-1980",10000,"USA"]
}
}
}
{
"response":
{
"uri": "/api/abc@zylker.com/EmployeeDB/EmployeeDetails",
"action": "ADDROW",
"result":
{
"column\_order":["Name","Date Of Birth","Salary","Country"],
"rows":
["Gary","12-Jun-1980",10000,"USA"]
}
}
}
{
"response":
{
"uri": "/api/abc@zylker.com/EmployeeDB/EmployeeDetails",
"action": "ADDROW",
"result":
{
"column\_order":["Name","Date Of Birth","Salary","Country"],
"rows":
["Gary","12-Jun-1980",10000,"USA"]
}
}
}
{
"response":
{
"uri": "/api/abc@zylker.com/EmployeeDB/EmployeeDetails",
"action": "ADDROW",
"result":
{
"column\_order":["Name","Date Of Birth","Salary","Country"],
"rows":
["Gary","12-Jun-1980",10000,"USA"]
}
}
}
{
"response":
{
"uri": "/api/abc@zylker.com/EmployeeDB/EmployeeDetails",
"action": "ADDROW",
"result":
{
"column\_order":["Name","Date Of Birth","Salary","Country"],
"rows":
["Gary","12-Jun-1980",10000,"USA"]
}
}
}
{
"response":
{
"uri": "/api/abc@zylker.com/EmployeeDB/EmployeeDetails",
"action": "ADDROW",
"result":
{
"column\_order":["Name","Date Of Birth","Salary","Country"],
"rows":
["Gary","12-Jun-1980",10000,"USA"]
}
}
}
The response format of the API request is controlled by the ZOHO\_OUTPUT\_FORMAT query parameter passed in the request. Currently Zoho Analytics supports XML and JSON respone formats. CSV and PDF response formats are supported only for Export action.
Note:
See this link for response formats in case of errors on API execution.
XML Format
The response will have the 
tag as the root node. It might either contain a 
or 
node as it's child, but not both. The 
node will be present under normal circumstances, whereas 
node will be present in case of error conditions.
Format
xml version="1.0" encoding="UTF-8" ?


[specific XML response based on action]
JSON Format
JSON format follows the same pattern as that of XML format.
Format
{
"response":
{
"uri": "/api///",
"action": "",
"result": {[action specific properties]}
}
}
Other Formats
Other formats such as CSV, PDF can be specified only when ZOHO\_ACTION is EXPORT. These formats don't have any generic parseable header/footer. See this link for more details about these formats.
Error Handling
Sample error response : IMPORT DATA
Sample error response for import data in Table EmployeeDetails in the workspace EmployeeDB
Sample error response for import data in Table EmployeeDetails in the workspace EmployeeDB
Sample error response for import data in Table EmployeeDetails in the workspace EmployeeDB
Sample error response for import data in Table EmployeeDetails in the workspace EmployeeDB
Sample error response for import data in Table EmployeeDetails in the workspace EmployeeDB
Sample error response for import data in Table EmployeeDetails in the workspace EmployeeDB
XML Format:
xml version="1.0" encoding="UTF-8"?


`7138`
Table EmployeeDetails is not present in the workspace EmployeeDB
xml version="1.0" encoding="UTF-8"?


`7138`
Table EmployeeDetails is not present in the workspace EmployeeDB
xml version="1.0" encoding="UTF-8"?


`7138`
Table EmployeeDetails is not present in the workspace EmployeeDB
xml version="1.0" encoding="UTF-8"?


`7138`
Table EmployeeDetails is not present in the workspace EmployeeDB
xml version="1.0" encoding="UTF-8"?


`7138`
Table EmployeeDetails is not present in the workspace EmployeeDB
xml version="1.0" encoding="UTF-8"?


`7138`
Table EmployeeDetails is not present in the workspace EmployeeDB
JSON Format:
{
"response":
{
"url": "/api/demouser/EmployeeDB/EmployeeDetails",
"action": "IMPORT",
"error":
{
"code":7138,
"message": "Table EmployeeDetails is not present in the workspace EmployeeDB"
}
}
}
{
"response":
{
"url": "/api/demouser/EmployeeDB/EmployeeDetails",
"action": "IMPORT",
"error":
{
"code":7138,
"message": "Table EmployeeDetails is not present in the workspace EmployeeDB"
}
}
}
{
"response":
{
"url": "/api/demouser/EmployeeDB/EmployeeDetails",
"action": "IMPORT",
"error":
{
"code":7138,
"message": "Table EmployeeDetails is not present in the workspace EmployeeDB"
}
}
}
{
"response":
{
"url": "/api/demouser/EmployeeDB/EmployeeDetails",
"action": "IMPORT",
"error":
{
"code":7138,
"message": "Table EmployeeDetails is not present in the workspace EmployeeDB"
}
}
}
{
"response":
{
"url": "/api/demouser/EmployeeDB/EmployeeDetails",
"action": "IMPORT",
"error":
{
"code":7138,
"message": "Table EmployeeDetails is not present in the workspace EmployeeDB"
}
}
}
{
"response":
{
"url": "/api/demouser/EmployeeDB/EmployeeDetails",
"action": "IMPORT",
"error":
{
"code":7138,
"message": "Table EmployeeDetails is not present in the workspace EmployeeDB"
}
}
}
API execution could result in Error conditions. In such cases, you may follow the below steps to identify an error condition and to handle the same:
Check the http response code. If it is 4xx or 5xx (eg., 400, 500, 401 etc.,), then it is an error.
In case of error, the error information would be sent in the response body.
The format of the error content can be specified by the parameter ZOHO\_ERROR\_FORMAT. The value it can be either:
XML
JSON
XML Format
xml version="1.0" encoding="UTF-8" ?


[error details]
JSON Format
{
"response":
{
"uri": "/api///",
"action": "",
"error": {[error details]}
}
}
Common Parameters in Query String of the API URL
In this section we will discuss about the mandatory and optional parameters that could be passed in the query string of every API call.
Mandatory Parameters:
Auth Token
Auth Token is an unique token that authenticates the user. Click here to know how to generate an Auth Token.
ZOHO\_ACTION
This parameter specifies the action to be performed by the API request. The sample values are:
- ADDROW - To add a row of data into a table.
- IMPORT - To import data in bulk into a table in CSV/TSV/Tabular Text formats
- UPDATE - To update existing rows in a table.
- DELETE - To delete rows in a table.
- EXPORT - To export table or report in different formats.
Note:
Value of ZOHO\_ACTION parameter should be in the same case(UPPER CASE) as given in this document.
ZOHO\_OUTPUT\_FORMAT
This parameter specifies the output format for the response. Following are the following supported formats:
- XML
- JSON
Incase ZOHO\_ACTION is EXPORT then following additional formats are supported.
- CSV
- HTML
- IMAGE
ZOHO\_ERROR\_FORMAT
Specifies the output format for the response in case an error occurs when trying to process the request. Following are the supported formats:
- XML
- JSON
ZOHO\_API\_VERSION
The API version of Zoho Analytics based on which the application(/service) has been written. This parameter allows Zoho Analytics to handle applications based on the older versions. The current API version is 1.0
Optional Parameters:
These parameters have to be sent in the body of the POST request.
ZOHO\_DATE\_FORMAT
This parameter can be used during Import of data, which has a date column, whose format is not properly identified by Zoho Analytics.
Example: ZOHO\_DATE\_FORMAT=dd-MMM-yyyy
Data API
This section lists the APIs which can be used to perform data addition, bulk import, deletion and updates into your Zoho Analytics data tables. This also provides APIs to export your tables, reports & dashboards in PDF, Excel, JSON, HTML, Image and CSV formats.
Add Row
Download client libraries : C# | GO | JAVA | PHP | PYTHON
Sample Request:
using ZReports;
namespace Test
{
AUTHTOKEN = "\*\*\*\*\*\*\*\*\*\*\*\*";
EMAIL = "user@zylker.com";
DBNAME = "EmployeeDB";
TBNAME = "EmployeeTB";
class Program
{
public IReportClient getClient()
{
IReportClient RepClient = new ReportClient(AUTHTOKEN);
return RepClient;
}
public void addRow(IReportClient RepClient)
{
string tableURI = RepClient.GetURI(EMAIL, DBNAME, TBNAME);
Dictionary ColumnValues = new Dictionary();
ColumnValues.Add("Region", "South");
Dictionary addRowRes = RepClient.AddRow(tableURI, ColumnValues,
config);
}
static void Main(string[] args)
{
Program obj = new Program();
IReportClient rc = obj.getClient();
obj.addRow(rc);
}
}
}
package main
import (
"fmt"
"zoho/pkg/reportclient"
)
var(
email = "user@zylker.com"
dbname = "Employee"
tbname = "sample"
authtoken = "\*\*\*\*\*\*\*\*\*\*\*\*"
)
func addrow() {
url := reportclient.GetUri(email, dbname, tbname)
columnvalues := map[string]string{}
columnvalues["Id"] = "999"
columnvalues["Name"] = "zzz"
resultmap , err := reportclient.AddRow(url, columnvalues)
if(err != nil){
fmt.Println(err.ErrorMessage)
fmt.Println(err.ErrorCode)
fmt.Println(err.Action)
fmt.Println(err.HttpStatusCode)
}else{
fmt.Println(resultmap)
}
}
func main() {
reportclient.SetAuthToken(authtoken)
addrow()
}
import com.adventnet.zoho.client.report.\*;
public class Sample
{
String email = "user@zylker.com";
String dbname = "EmployeeDB";
String tbname = "EmployeeTB";
String authtoken = "\*\*\*\*\*\*\*\*\*\*\*\*";
Map config = new HashMap();
Map colval = new HashMap();
private ReportClient rc = new ReportClient(authtoken);
rc.setIamServerURL("https://:/iam");
rc.setReportServerURL("https://:");
public void addrow() throws Exception
{
String uri = rc.getURI(email,dbname,tbname);
colval.put("Id", 101);
colval.put("Name", "sam");
Map result = rc.addRow(uri,colval,config);
System.out.println(result);
}
public static void main(String[] args) throws Exception
{
Sample obj = new Sample();
obj.addrow();
}
}
php
require 'ReportClient.php';
$EMAIL\_ID = "abc@zylker.com";
$DB\_NAME = "EmployeeDB";
$TABLE\_NAME = "EmployeeTB";
$AUTHTOKEN = "\*\*\*\*\*\*\*\*\*\*\*\*";
$report\_client\_request = new ReportClient($AUTHTOKEN);
$uri = $report\_client\_request-getURI($EMAIL\_ID, $DB\_NAME, $TABLE\_NAME);
$column\_values = array("Employee Name" => "Shankar", "Employee ID" => "2015",
"Experience" => "5");
$response\_array = $report\_client\_request->addRow($uri, $column\_values);
?>
from \_\_future\_\_ import with\_statement
from ReportClient import ReportClient
import sys
class Sample:
LOGINEMAILID="abc@zylker.com"
AUTHTOKEN="f7d016b46be276cd4a1232a592f40101"
DATABASENAME="Employee"
TABLENAME="Employee"
rc = None
rc = ReportClient(self.AUTHTOKEN)
def AddRow(self,rc):
uri = rc.getURI(self.LOGINEMAILID,self.DATABASENAME,self.TABLENAME)
rowData = {"Date":"01 Jan, 2009 00:00:00","Region":"East","Product Category":
"Samples","Product":"SampleProduct","Customer Name":"Sample",
"Sales":2000,"Cost":2000}
result = rc.addRow(uri,rowData,None)
print result
obj = Sample()
obj.AddRow(obj.rc)
curl -d "ZOHO\_ACTION=ADDROW&ZOHO\_OUTPUT\_FORMAT=XML&ZOHO\_ERROR\_FORMAT=XML
&ZOHO\_API\_VERSION=1.0&authtoken=f7d016b46be276cdasda32a592f40101&Id=999
&Name=Gary&Date Of Birth=12-Jun-1980&Salary=10000&Country=USA"
https://:/api/abc@zylker.com/EmployeeDB/EmployeeDetails
Sample Response JSON Format:
{
"response":
{
"url": "/api/abc@zylker.com/EmployeeDB/EmployeeDetails",
"action": "ADDROW",
"result":
{
"column\_order":["Name","Date Of Birth","Salary","Country"],
"rows":["Gary","12-Jun-1980",10000,"USA"]
}
}
}
Sample Response XML Format:
xml version="1.0" encoding="UTF-8" ?




Gary
12-Jun-1980
10000
USA

This API allows you to add a single row into a specified table.
Request URI
https://:/api///
Common Parameters
| Parameter | Possible Values | Description |
|---|---|---|
| ZOHO\_ACTION | ADDROW | This parameter specifies the action to be performed by the API request.Note: Value of ZOHO\_ACTION parameter should be in the same case(UPPER CASE) as given in this document. |
| ZOHO\_OUTPUT\_FORMAT | XML/JSON | This parameter specifies the output format for the response. |
| ZOHO\_ERROR\_FORMAT | XML/JSON | Specifies the output format for the response in case an error occurs when trying to process the request. |
| authtoken | user authtoken | Auth Token is an unique token that authenticates the user. |
| ZOHO\_API\_VERSION | 1.0 | The API version of Zoho Analytics based on which the application(/service) has been written. This parameter allows the Zoho Analytics to handle applications based on the older versions.The current API version is 1.0 |
Action Specific Parameters(Data for the Row)
The column values for the row should be passed as POST parameters in 
=
format. (The parameters should be in application/x-www-form-urlencoded format).
- Refers to the name of the column in the table to which the value is added.
- Refers to the corresponding value to be added for this column.
Delete Data
Download client libraries : C# | GO | JAVA | PHP | PYTHON
Sample Request:
using ZReports;
namespace Test
{
AUTHTOKEN = "\*\*\*\*\*\*\*\*\*\*\*\*";
EMAIL = "user@zylker.com";
DBNAME = "EmployeeDB";
TBNAME = "EmployeeTB";
class Program
{
public IReportClient getClient()
{
IReportClient RepClient = new ReportClient(AUTHTOKEN);
return RepClient;
}
public void deleteRow(IReportClient RepClient)
{
string tableURI = RepClient.GetURI(EMAIL, DBNAME, TBNAME);
string criteria = "\"Region\"='South'";
RepClient.DeleteData(tableURI, criteria, null);
}
static void Main(string[] args)
{
Program obj = new Program();
IReportClient rc = obj.getClient();
obj.deleteRow(rc);
}
}
}
package main
import (
"fmt"
"zoho/pkg/reportclient"
)
var(
email = "user@zylker.com"
dbname = "Employee"
tbname = "sample"
authtoken = "\*\*\*\*\*\*\*\*\*\*\*\*"
)
func deletedata() {
url := reportclient.GetUri(email, dbname, tbname)
params := map[string]string{}
params["ZOHO\_CRITERIA"] = "Id=2"
err := reportclient.DeleteData(url, params)
if(err != nil){
fmt.Println(err.ErrorMessage)
fmt.Println(err.ErrorCode)
fmt.Println(err.Action)
fmt.Println(err.HttpStatusCode)
}else{
fmt.Println("Success")
}
}
func main() {
reportclient.SetAuthToken(authtoken)
deletedata()
}
import com.adventnet.zoho.client.report.\*;
public class Sample
{
String email = "user@zylker.com";
String dbname = "EmployeeDB";
String tbname = "EmployeeTB";
String authtoken = "\*\*\*\*\*\*\*\*\*\*\*\*";
Map config = new HashMap();
private ReportClient rc = new ReportClient(authtoken);
rc.setIamServerURL("https://:/iam");
rc.setReportServerURL("https://:");
public void deletedata() throws Exception
{
String uri = rc.getURI(email,dbname,tbname);
rc.deleteData(uri,"id=100",config);
}
public static void main(String[] args) throws Exception
{
Sample obj = new Sample();
obj.deletedata();
}
}
php
require 'ReportClient.php';
$EMAIL\_ID = "abc@zylker.com";
$DB\_NAME = "EmployeeDB";
$TABLE\_NAME = "EmployeeTB";
$AUTHTOKEN = "\*\*\*\*\*\*\*\*\*\*\*\*";
$report\_client\_request = new ReportClient($AUTHTOKEN);
$uri = $report\_client\_request-getURI($EMAIL\_ID, $DB\_NAME, $TABLE\_NAME);
$criteria = "Experience = 3";
$report\_client\_request->deleteData($uri ,$criteria);
?>
from \_\_future\_\_ import with\_statement
from ReportClient import ReportClient
import sys
class Sample:
LOGINEMAILID="abc@zylker.com"
AUTHTOKEN="\*\*\*\*\*\*\*\*\*\*\*\*"
DATABASENAME="Employee"
TABLENAME="Employee"
rc = None
rc = ReportClient(self.AUTHTOKEN)
def DeleteData(self,rc):
uri = rc.getURI(self.LOGINEMAILID,self.DATABASENAME,self.TABLENAME)
rc.deleteData(uri,"\"Employee Name\"='Sample'",None);
obj = Sample()
obj.DeleteData(obj.rc)
curl -d "ZOHO\_ACTION=DELETE&ZOHO\_OUTPUT\_FORMAT=XML&ZOHO\_ERROR\_FORMAT=XML
&ZOHO\_API\_VERSION=1.0&authtoken=f7d016b46be2acsd4cfa32a592f40101
&ZOHO\_CRITERIA=("Department" = 'Finance')"
https://:/api/abc@zylker.com/EmployeeDB/EmployeeDetails
Sample Response JSON Format:
{
"response":
{
"uri": "/api/abc@zylker.com/EmployeeDB/EmployeeDetails",
"action": "DELETE",
"criteria": "\"Department\" = \'Finance\'",
"result":
{
"message": "Deleted rows",
"deletedrows":"4"
}
}
}
Sample Response XML Format:
xml version="1.0" encoding="UTF-8" ?

"Department" = 'Finance'

Deleted rows
4
The data present in a table can be deleted using this API.
Request URI
https://:/api///
Common Parameters
| Parameter | Possible Values | Description |
|---|---|---|
| ZOHO\_ACTION | DELETE | This parameter specifies the action to be performed by the API request.Note: Value of ZOHO\_ACTION parameter should be in the same case(UPPER CASE) as given in this document. |
| ZOHO\_OUTPUT\_FORMAT | XML/JSON | This parameter specifies the output format for the response. |
| ZOHO\_ERROR\_FORMAT | XML/JSON | Specifies the output format for the response in case an error occurs when trying to process the request. |
| authtoken | user authtoken | Auth Token is an unique token that authenticates the user. |
| ZOHO\_API\_VERSION | 1.0 | The API version of Zoho Analytics based on which the application(/service) has been written. This parameter allows the Zoho Analytics to handle applications based on the older versions.The current API version is 1.0. |
Action Specific Parameters
| Parameter | Possible Values | Description |
|---|---|---|
| ZOHO\_CRITERIA (optional) |
Criteria | If that parameter is not sent, then all the rows are deleted. If criteria is sent the rows matching the criteria alone are deleted.Please view this link for more details about the format for ZOHO\_CRITERIA. |
Update Data
Download client libraries : C# | GO | JAVA | PHP | PYTHON
Sample Request:
using ZReports;
namespace Test
{
AUTHTOKEN = "\*\*\*\*\*\*\*\*\*\*\*\*";
EMAIL = "user@zylker.com";
DBNAME = "EmployeeDB";
TBNAME = "EmployeeTB";
class Program
{
public IReportClient getClient()
{
IReportClient RepClient = new ReportClient(AUTHTOKEN);
return RepClient;
}
public void updateRow(IReportClient RepClient)
{
string tableURI = RepClient.GetURI(EMAIL, DBNAME, TBNAME);
Dictionary ColumnValues = new Dictionary();
ColumnValues.Add("Region", "North");
string criteria = "\"Region\"='South'";
RepClient.UpdateData(tableURI, ColumnValues, criteria, null);
}
static void Main(string[] args)
{
Program obj = new Program();
IReportClient rc = obj.getClient();
obj.updateRow(rc);
}
}
}
package main
import (
"fmt"
"zoho/pkg/reportclient"
)
var(
email = "user@zylker.com"
dbname = "Employee"
tbname = "sample"
authtoken = "\*\*\*\*\*\*\*\*\*\*\*\*"
)
func updatedata() {
url := reportclient.GetUri(email, dbname, tbname)
params := map[string]string{}
params["Salary"] = "100"
params["ZOHO\_CRITERIA"] = "id=1"
resultmap , err := reportclient.UpdateData(url, params)
if(err != nil){
fmt.Println(err.ErrorMessage)
fmt.Println(err.ErrorCode)
fmt.Println(err.Action)
fmt.Println(err.HttpStatusCode)
}else{
fmt.Println(resultmap)
}
}
func main() {
reportclient.SetAuthToken(authtoken)
updatedata()
}
import com.adventnet.zoho.client.report.\*;
public class Sample
{
String email = "user@zylker.com";
String dbname = "EmployeeDB";
String tbname = "EmployeeTB";
String authtoken = "\*\*\*\*\*\*\*\*\*\*\*\*";
Map config = new HashMap();
Map colval = new HashMap();
private ReportClient rc = new ReportClient(authtoken);
rc.setIamServerURL("https://:/iam");
rc.setReportServerURL("https://:");
public void updatedata() throws Exception
{
String uri = rc.getURI(email,dbname,tbname);
colval.put("Salary", 1000);
rc.updateData(uri,colval,"Id=101",config);
}
public static void main(String[] args) throws Exception
{
Sample obj = new Sample();
obj.updatedata();
}
}
php
require 'ReportClient.php';
$EMAIL\_ID = "abc@zylker.com";
$DB\_NAME = "EmployeeDB";
$TABLE\_NAME = "EmployeeTB";
$AUTHTOKEN = "\*\*\*\*\*\*\*\*\*\*\*\*";
$report\_client\_request = new ReportClient($AUTHTOKEN);
$uri = $report\_client\_request-getURI($EMAIL\_ID, $DB\_NAME, $TABLE\_NAME);
$column\_values = array("Salary" => "10000");
$criteria = "Experience = 2";
$report\_client\_request->updateData($uri ,$columnvalues, $criteria);
?>
from \_\_future\_\_ import with\_statement
from ReportClient import ReportClient
import sys
class Sample:
LOGINEMAILID="abc@zylker.com"
AUTHTOKEN="\*\*\*\*\*\*\*\*\*\*\*\*"
DATABASENAME="Employee"
TABLENAME="Employee"
rc = None
rc = ReportClient(self.AUTHTOKEN)
def updateData(self,rc):
uri = rc.getURI(self.LOGINEMAILID,self.DATABASENAME,self.TABLENAME)
updateInfo = {"Region":"West","Product":"SampleProduct\_2"}
rc.updateData(uri,updateInfo,"\"Customer Name\"='Sample'",None);
obj = Sample()
obj.updateData(obj.rc)
curl -d "ZOHO\_ACTION=UPDATE&ZOHO\_OUTPUT\_FORMAT=XML&ZOHO\_ERROR\_FORMAT=XML
&ZOHO\_API\_VERSION=1.0&authtoken=f7d016b46bedswcd4cfa32a592f40101&Name=as
&ZOHO\_CRITERIA=("Department" = 'Finance')"
https://:/api/abc@zylker.com/EmployeeDB/EmployeeDetails
Sample Response JSON Format:
{
"response":
{
"uri": "/api/abc@zylker.com/EmployeeDB/EmployeeDetails",
"action": "UPDATE",
"criteria": "\"Department\" = 'Finance'",
"result":
{
"updatedColumns":["Salary","Deduction","Perks"],
"updatedRows":"4"
}
}
}
Sample Response XML Format:
xml version="1.0" encoding="UTF-8" ?

"Department" = 'Finance'


Salary
Deduction
Perks
4
The data present in a table can be updated using this API.
Request URI
https://:/api///
Common Parameters
| Parameter | Possible Values | Description |
|---|---|---|
| ZOHO\_ACTION | UPDATE | This parameter specifies the action to be performed by the API request.Note: Value of ZOHO\_ACTION parameter should be in the same case(UPPER CASE) as given in this document. |
| ZOHO\_OUTPUT\_FORMAT | XML/JSON | This parameter specifies the output format for the response. |
| ZOHO\_ERROR\_FORMAT | XML/JSON | Specifies the output format for the response in case an error occurs when trying to process the request. |
| authtoken | user authtoken | Auth Token is an unique token that authenticates the user. |
| ZOHO\_API\_VERSION | 1.0 | The API version of Zoho Analytics based on which the application(/service) has been written. This parameter allows the Zoho Analytics to handle applications based on the older versions.The current API version is 1.0. |
Action Specific Parameters
| Parameter | Possible Values | Description |
|---|---|---|
| ZOHO\_CRITERIA (optional) |
Criteria | If that parameter is not sent, then all the rows are updated. If criteria is sent the rows matching the criteria alone are updated.For more details about the format for the criteria view this link. |
Specifying the data to be updated (POST params)
Pass the columns whose values you would like to update in a 
=
format. (The parameters should be in application/x-www-form-urlencoded format).
- Refers to the name of the column in the table whose value is to be updated.
- Refers to the corresponding value to be updated in the column
For specifying empty (null) values, the parameter should be sent with empty values. In the example above, the Deduction value is taken to be empty.
Import Data
Download client libraries : C# | GO | JAVA | PHP | PYTHON
Sample Request:
using ZReports;
namespace Test
{
AUTHTOKEN = "\*\*\*\*\*\*\*\*\*\*\*\*";
EMAIL = "user@zylker.com";
DBNAME = "EmployeeDB";
TBNAME = "EmployeeTB";
class Program
{
public IReportClient getClient()
{
IReportClient RepClient = new ReportClient(AUTHTOKEN);
return RepClient;
}
public void importData(IReportClient RepClient)
{
string tableURI = RepClient.GetURI(EMAIL, DBNAME, TBNAME);
Dictionary ImportConfig = new Dictionary();
ImportConfig.Add("ZOHO\_ON\_IMPORT\_ERROR", "ABORT");
Dictionary ImportRes = RepClient.ImportData(tableURI,
ZohoReportsConstants.APPEND,"C:\\workspace\\mydata.csv",ImportConfig);
}
static void Main(string[] args)
{
Program obj = new Program();
IReportClient rc = obj.getClient();
obj.importData(rc);
}
}
}
package main
import (
"fmt"
"zoho/pkg/reportclient"
)
var(
email = "user@zylker.com"
dbname = "Employee"
tbname = "sample"
authtoken = "\*\*\*\*\*\*\*\*\*\*\*\*"
)
func importdata() {
url := reportclient.GetUri(email, dbname, tbname)
params := map[string]string{}
file := "/home/sample.csv"
importtype := "APPEND"
autoidentity := "true"
onerror := "ABORT"
resp , err := reportclient.ImportData(url, file, importtype, autoidentity, onerror, params)
if(err != nil){
fmt.Println(err.ErrorMessage)
fmt.Println(err.ErrorCode)
fmt.Println(err.Action)
fmt.Println(err.HttpStatusCode)
}else{
fmt.Println(resp.ImportErrors)
fmt.Println(resp.ColumnDetails)
fmt.Println(resp.ImportType)
fmt.Println(resp.Warnings)
fmt.Println(resp.SelectedColumnCount)
fmt.Println(resp.SuccessRowCount)
fmt.Println(resp.ImportOperation)
fmt.Println(resp.TotalColumnCount)
fmt.Println(resp.TotalRowCount)
}
}
func main() {
reportclient.SetAuthToken(authtoken)
importdata()
}
import com.adventnet.zoho.client.report.\*;
public class Sample
{
String email = "user@zylker.com";
String dbname = "EmployeeDB";
String tbname = "EmployeeTB";
String authtoken = "\*\*\*\*\*\*\*\*\*\*\*\*";
Map config = new HashMap();
File csvFile = new File("samples/StoreSales.csv");
private ReportClient rc = new ReportClient(authtoken);
rc.setIamServerURL("https://:/iam");
rc.setReportServerURL("https://:");
public void importdata() throws Exception
{
String uri = rc.getURI(email,dbname,tbname);
config.put("ZOHO\_AUTO\_IDENTIFY","true");
config.put("ZOHO\_ON\_IMPORT\_ERROR","ABORT");
config.put("ZOHO\_CREATE\_TABLE","false");
Object result = rc.importData(uri,"APPEND",csvFile,config,false);
}
public static void main(String[] args) throws Exception
{
Sample obj = new Sample();
obj.importdata();
}
}
php
require 'ReportClient.php';
$EMAIL\_ID = "abc@zylker.com";
$DB\_NAME = "EmployeeDB";
$TABLE\_NAME = "EmployeeTB";
$AUTHTOKEN = "\*\*\*\*\*\*\*\*\*\*\*\*";
$report\_client\_request = new ReportClient($AUTHTOKEN);
$uri = $report\_client\_request-getURI($EMAIL\_ID, $DB\_NAME, $TABLE\_NAME);
$import\_type = "APPEND";
$file = $\_FILES['file'];
$auto\_identify = "TRUE";
$on\_error = "ABORT";
$response\_obj = $report\_client->importData($table\_uri, $import\_type, $file,
$auto\_identify, $on\_error);
?>
from \_\_future\_\_ import with\_statement
from ReportClient import ReportClient
import sys
class Sample:
LOGINEMAILID="abc@zylker.com"
AUTHTOKEN="\*\*\*\*\*\*\*\*\*\*\*\*"
DATABASENAME="Employee"
TABLENAME="Employee"
rc = None
rc = ReportClient(self.AUTHTOKEN)
def importData(self,rc):
uri = rc.getURI(self.LOGINEMAILID,self.DATABASENAME,self.TABLENAME)
try:
with open('StoreSales.csv', 'r') as f:
importContent = f.read()
except Exception,e:
print "Error Check if file StoreSales.csv exists in the current directory"
print "(" + str(e) + ")"
return
impResult = rc.importData(uri,"APPEND",importContent,None)
print "Added Rows :" +str(impResult.successRowCount) + " and Columns :" +
str(impResult.selectedColCount)
obj = Sample()
obj.importData(obj.rc)
curl -XPOST -H "Content-type: multipart/form-data"
-d 'ZOHO\_ACTION=IMPORT&ZOHO\_OUTPUT\_FORMAT=XML&ZOHO\_ERROR\_FORMAT=XML
&ZOHO\_API\_VERSION=1.0&authtoken=f7d016b46be276c3w24a32a592f40101
&ZOHO\_IMPORT\_TYPE=APPEND&ZOHO\_AUTO\_IDENTIFY=TRUE&ZOHO\_ON\_IMPORT\_ERROR=ABORT
&ZOHO\_FILE=sample.csv'
https://:/api/abc@zylker.com/sample/Employee
Sample Response JSON Format:
{
" response":
{
"uri": "/api/abc@zylker.com/EmployeeDB/EmployeeDetails",
"action": "IMPORT",
"result":
{
"importSummary":
{
"totalColumnCount":3,
"selectedColumnCount":3,
"totalRowCount":50,
"successRowCount":48,
"warnings":0,
"importOperation": "created",
"importType": "APPEND"
},
"columnDetails":
{
"Name": "Plain Text",
"Date Of Birth": "Date",
"Salary": "Number"
},
"importErrors": "[Line: 5 Field: 3] a1213 -WARNING: Invalid Number value"
}
}
}
Sample Response XML Format:
xml version="1.0" encoding="UTF-8" ?



3 
3
50
48
0
created
APPEND

Name 
Date Of Birth
Salary


[Line: 5 Field: 3] a1213 -WARNING: Invalid Number value
With the Zoho Analytics On-Premise API, you can add/update data in bulk. The data to be added/updated should be in CSV or JSON file formats.
Request URI
https://:/api///
Common Parameters
| Parameter | Possible Values | Description |
|---|---|---|
| ZOHO\_ACTION | IMPORT | This parameter specifies the action to be performed by the API request.Note: Value of ZOHO\_ACTION parameter should be in the same case(UPPER CASE) as given in this document. |
| ZOHO\_OUTPUT\_FORMAT | XML/JSON | This parameter specifies the output format for the response. |
| ZOHO\_ERROR\_FORMAT | XML/JSON | Specifies the output format for the response in case an error occurs when trying to process the request. |
| authtoken | user authtoken | Auth Token is an unique token that authenticates the user. |
| ZOHO\_API\_VERSION | 1.0 | The API version of Zoho Analytics based on which the application(/service) has been written. This parameter allows Zoho Analytics to handle applications based on the older versions.The current API version is 1.0. |
| ZOHO\_FILE or ZOHO\_IMPORT\_DATA | File or string | ZOHO\_FILE - The file to be imported. ZOHO\_IMPORT\_DATA - The strng to be imported. |
Action Specific Parameters
| Parameter | Possible Values | Description |
|---|---|---|
| ZOHO\_CRITERIA (optional) |
Criteria | If that parameter is not sent, then all the rows are updated. If criteria is sent the rows matching the criteria alone are updated. |
| ZOHO\_FILE (mandatory) |
File | The file to import. |
| ZOHO\_IMPORT\_FILETYPE (optional) |
CSV/JSON | Default value is CSV. Format of the file to be imported. Supported formats are: |
| ZOHO\_IMPORT\_TYPE (mandatory) | APPEND/TRUNCATEADD/UPDATEADD | |
| ZOHO\_AUTO\_IDENTIFY (mandatory) |
TRUE/FALSE | Used to specify whether to auto identify the CSV format. |
| ZOHO\_ON\_IMPORT\_ERROR (mandatory) |
ABORT/SKIPROW/SETCOLUMNEMPTY | This parameter controls the action to be taken incase there is an error during import. |
| ZOHO\_CREATE\_TABLE (optional) |
true/false. | Default is false. |
| ZOHO\_SELECTED\_COLUMNS (optional) |
List of comma separated column names. E.g.,: Name, Department |
Specify the columns to be imported into the Zoho Analytics table from the data being uploaded. Note: Incase of JSON files you need to specify the column names capturing the full JSON tree heirrachy eg., employee.Name, employee.Department |
| ZOHO\_MATCHING\_COLUMNS (mandatory only when the ZOHO\_IMPORT\_TYPE is UPDATEADD) |
List of comma separated column names. E.g.,: Name,Department |
The values in the columns to be matched will be used for comparision to check whether data row(s) being imported matches with an existing row(s) in the table. The existing rows in the table that match will be updated with values from data imported. The remaining rows are appended to the table as new rows. |
| ZOHO\_SKIPTOP (optional) |
 |
Number of rows that are to be skipped from the top in the CSV file being imported. |
| ZOHO\_THOUSAND\_SEPARATOR (optional) |
0 / 1 / 2 / 3 | Default is 0. This parameter controls the action to be taken in case there is a thousand separator in the data. 0 - COMMA 1 - DOT 2 - SPACE 3 - SINGLE QUOTE |
| ZOHO\_DECIMAL\_SEPARATOR (optional) |
0 / 1 | Default is 0. This parameter controls the action to be taken in case there is a decimal separator in the data. 0 - DOT 1 - COMMA |
| ZOHO\_DATE\_FORMAT (optional) |
Format of the date. E.g. dd-MMM-YYYY |
The format of date value. Specify this incase any date field is being imported and its format cannot be auto recognized by Zoho Analytics. |
| ZOHO\_IMPORT\_JSON\_RETCOLNAMES (optional) |
true/false. | Default value is false. This parameter is applicable only for importing JSON files. This defines how the columns names are to be constructed from the JSON file. eg. , employee.Name, employee.Department |
CSV Format Details
These parameters need to be specified if the ZOHO\_AUTO\_IDENTIFY is set to false.
| Parameter | Possible Values | Description |
|---|---|---|
| ZOHO\_COMMENTCHAR |  |
Comment Character. If the character mentioned is found at the beginning of the row, the csv row will be skipped. |
| ZOHO\_DELIMITER | 0 / 1 / 2 / 3 | Delimiter which separates the values in the file. 0 - if the delimiter is COMMA 1 - if the delimiter is TAB 2 - if the delimiter is SEMICOLON 3 - if the delimiter is SPACE |
| ZOHO\_QUOTED | 0 / 1 / 2 | The Text Qualifier. 0 - None 1 - SINGLE QUOTE 2 - DOUBLE QUOTE |
Export Data
Download client libraries : C# | GO | JAVA | PHP | PYTHON
Sample Request:
using ZReports;
namespace Test
{
AUTHTOKEN = "\*\*\*\*\*\*\*\*\*\*\*\*";
EMAIL = "user@zylker.com";
DBNAME = "EmployeeDB";
TBNAME = "EmployeeTB";
class Program
{
public IReportClient getClient()
{
IReportClient RepClient = new ReportClient(AUTHTOKEN);
return RepClient;
}
public object export(IReportClient RepClient)
{
string tableURI = RepClient.GetURI(EMAIL, DBNAME, TBNAME);
Dictionary resObj = RepClient.ExportDataAsDictionary(tableURI,
"\"Region\"='West'", null);
Object[] columns = (Object[])resObj["column\_order"];
Object[] rows = (Object[])resObj["rows"];
}
static void Main(string[] args)
{
Program obj = new Program();
IReportClient rc = obj.getClient();
obj.export(rc);
}
}
}
package main
import (
"fmt"
"zoho/pkg/reportclient"
)
var(
email = "user@zylker.com"
dbname = "Employee"
tbname = "sample"
authtoken = "\*\*\*\*\*\*\*\*\*\*\*\*"
)
func exportdata() {
url := reportclient.GetUri(email, dbname, tbname)
outputformat := "pdf"
filename := "sample"
params := map[string]string{}
err := reportclient.ExportData(url, filename, outputformat, params)
if(err != nil){
fmt.Println(err.ErrorMessage)
fmt.Println(err.ErrorCode)
fmt.Println(err.Action)
fmt.Println(err.HttpStatusCode)
}else{
fmt.Println("Success")
}
}
func main() {
reportclient.SetAuthToken(authtoken)
exportdata()
}
import com.adventnet.zoho.client.report.\*;
public class Sample
{
String email = "user@zylker.com";
String dbname = "EmployeeDB";
String tbname = "EmployeeTB";
String authtoken = "\*\*\*\*\*\*\*\*\*\*\*\*";
File csvFile = new File("samples/StoreSales.csv");
private ReportClient rc = new ReportClient(authtoken);
rc.setIamServerURL("https://:/iam");
rc.setReportServerURL("https://:");
public void exportdata() throws Exception
{
String uri = rc.getURI(email,dbname,tbname);
rc.exportData(uri,"CSV",csvFile,null,null);
}
public static void main(String[] args) throws Exception
{
Sample obj = new Sample();
obj.exportdata();
}
}
php
require 'ReportClient.php';
$EMAIL\_ID = "abc@zylker.com";
$DB\_NAME = "EmployeeDB";
$TABLE\_NAME = "EmployeeTB";
$AUTHTOKEN = "\*\*\*\*\*\*\*\*\*\*\*\*";
$report\_client\_request = new ReportClient($AUTHTOKEN);
$uri = $report\_client\_request-getURI($EMAIL\_ID, $DB\_NAME, $TABLE\_NAME);
$output\_format = "CSV";
$criteria = "Salary = 5000";
$report\_client\_response = $report\_client\_request->exportData($uri, $output\_format);
$file = "dummy/".$TABLE\_NAME.".".$output\_format;
file\_put\_contents($file, $report\_client\_response, FILE\_APPEND);
?>
from \_\_future\_\_ import with\_statement
from ReportClient import ReportClient
import sys
class Sample:
LOGINEMAILID="abc@zylker.com"
AUTHTOKEN="\*\*\*\*\*\*\*\*\*\*\*\*"
DATABASENAME="Employee"
TABLENAME="Employee"
rc = None
rc = ReportClient(self.AUTHTOKEN)
def exportdata(self,rc):
uri = rc.getURI(self.LOGINEMAILID,self.DATABASENAME,self.TABLENAME)
fileobj = open("/home/sample.csv","rw+")
rc.exportData(uri,"CSV",fileobj)
fileobj.close()
obj = Sample()
obj.exportdata(obj.rc)
curl -d "ZOHO\_ACTION=EXPORT&ZOHO\_OUTPUT\_FORMAT=XML&ZOHO\_ERROR\_FORMAT=XML
&ZOHO\_API\_VERSION=1.0&authtoken=f7d016b46be276cd4cfaq2a592f40101"
https://:/api/abc@zylker.com/EmployeeDB/EmployeeDetails
Sample Response JSON Format:
{
"response":
{
"uri": "/api/abc@zylker.com/EmployeeDB/EmployeeDetails",
"action": "EXPORT",
"result":
{
"column\_order":["Name","Department","Date Of Birth"],
"rows":
[
["John","Finance","12 May 1972"],
["Joan","Admin","15 June 1975"]
]
}
}
}
Sample Response XML Format:
xml version="1.0" encoding="UTF-8" ?




Gary
12-Jun-1980
10000
USA

John
12-Jun-1981
10000
Canada

Joan
12-Jun-1982
10000
Mexico
Using this API users can export/pull data from tables or reports (pivots, charts etc.,) in different formats.
Request URI
https://:/api///
Common Parameters
| Parameter | Possible Values | Description |
|---|---|---|
| ZOHO\_ACTION | EXPORT | This parameter specifies the action to be performed by the API request.Note: Value of ZOHO\_ACTION parameter should be in the same case(UPPER CASE) as given in this document. |
| ZOHO\_OUTPUT\_FORMAT | XML/JSON/CSV/PDF/HTML/IMAGE | This parameter specifies the output format for the response. |
| ZOHO\_ERROR\_FORMAT | XML/JSON | Specifies the output format for the response in case an error occurs when trying to process the request. |
| authtoken | user authtoken | Auth Token is an unique token that authenticates the user. |
| ZOHO\_API\_VERSION | 1.0 | The API version of Zoho Analytics based on which the application(/service) has been written. This parameter allows the Zoho Analytics to handle applications based on the older versions.The current API version is 1.0. |
Action Specific Parameters
| Parameter | Possible Values | Description |
|---|---|---|
| ZOHO\_CRITERIA (optional) |
Criteria | If that parameter is not sent, then all the rows are exported. If criteria is sent the rows matching the criteria alone are exported.For more details about the format for the criteria refer this link. |
(optional) |
SQL Query | Literal SQL Query can be used as criteria. Export using joining tables and specific columns can be done using ZOHO\_SQLQUERY. Note :Shared users are not allowed to use this parameter. |
| GENERATETOC (optional - only for dashboards) |
true / false | true - To generate Table Of Contents.By default it will be false. |
| ZOHO\_DASHBOARD\_LAYOUT (optional - only for dashboards) |
0 or 1 | 0 - For Each Report in New Page 1 - For Layout as in Dashboard |
Additional optional parameters.
All the parameters that all defined below are optional one.
CSV Format
| Parameter 1 | Possible Values | Description |
|---|---|---|
| ZOHO\_DELIMITER | Value between 0 - 3 0 - COMMA 1 - TAB 2 - SEMICOLON 3 - SPACE |
The delimiter character used for separating the fields in a row in the CSV. |
| ZOHO\_RECORD\_DELIMITER | Value between 0 - 2 0 - DOS 1 - UNIX 2 - MAC |
The record delimiter (newline character) to use. |
| ZOHO\_QUOTED | Value between 0 - 1 0 - SINGLE 1 - DOUBLE |
The quote character to use for quoting the values. |
| ZOHO\_INCLUDE\_HEADER | true / false | true - To include the column names in the first row of the CSV exported. false - To not include the column names in the CSV exported. |
| ZOHO\_SHOW\_HIDDENCOLS | true / false | Controls where the columns that have been hidden in the table/report have to be exported. true - To include the hidden columns of the table/report in the data exported false - To not include the hidden columns of the table/report in the data exported. |
XML Format
| Parameter | Possible Values | Description |
|---|---|---|
| ZOHO\_SHOW\_HIDDENCOLS | true / false | Controls where the columns that have been hidden in the table/report have to be exported. true - To include the hidden columns of the table/report in the data exported false - To not include the hidden columns of the table/report in the data exported. |
HTML Format
| Parameter | Possible Values | Description |
|---|---|---|
| ZOHO\_SHOW\_HIDDENCOLS | true / false | Controls where the columns that have been hidden in the table/report have to be exported. true - To include the hidden columns of the table/report in the data exported false - To not include the hidden columns of the table/report in the data exported. |
PDF Format
| Parameter | Possible Values | Description |
|---|---|---|
| ZOHO\_PAPERSIZE | Value between 0 - 5 0 - LETTER 1 - LEGAL 2 - TABLOID 3 - A3 4 - A4 5 - AUTO |
The size of the paper. |
| ZOHO\_SHOW\_TITLE | Value between 0 - 2 0 - AT TOP 1 - AT BOTTOM 2 - NONE |
Controls the title positioning. |
| ZOHO\_SHOW\_DESC | Value between 0 - 2 0 - AT TOP 1 - AT BOTTOM 2 - NONE |
Controls the description positioning. |
| ZOHO\_PAPERSTYLE | Portrait / Landscape | |
| ZOHO\_SHOW\_HIDDENCOLS | true / false | Controls where the columns that have been hidden in the table/report have to be exported.true - To include the hidden columns of the table/report in the data exportedfalse - To not include the hidden columns of the table/report in the data exported. |
| ZOHO\_SELECTED\_COLUMNS | List of comma separated column names | Controls the column names that need to be exported. If it is not given then all the columns, in the table/report, are exported. |
| Margin Settings: | ||
| ZOHO\_TOPMARGIN ZOHO\_BOTTOMMARGIN ZOHO\_LEFTMARGIN ZOHO\_RIGHTMARGIN |
Decimal values between 0 to 1 | The margin in inches for that edge. Can be decimal between 0 to 1 (like 0.5). |
| Header/Footer Settings: | ||
| ZOHO\_HEAD\_LEFT ZOHO\_HEAD\_RIGHT ZOHO\_HEAD\_CENTER ZOHO\_FOOT\_LEFT ZOHO\_FOOT\_RIGHT ZOHO\_FOOT\_CENTER |
Value between 0 - 5 0 - Leave it blank 1 - Include Title 2 - Current Date/Time 3 - Include Page number in the format "Page #" 4 - Include page number in the format "Page # Of #" 5 - CUSTOM - Include custom text in footer |
The header or footer value that needs to be generated for each page at that particular position. |
| Custom Header/Footer value | ||
| ZOHO\_HEAD\_LEFT\_TEXT ZOHO\_HEAD\_RIGHT\_TEXT ZOHO\_HEAD\_CENTER\_TEXT ZOHO\_FOOT\_LEFT\_TEXT ZOHO\_FOOT\_RIGHT\_TEXT ZOHO\_FOOT\_CENTER\_TEXT |
Custom text. | If any of the header/footer setting is 5 (.ie, CUSTOM) then the corresponding custom value/text should be passed. |
IMAGE Format
| Parameter | Possible Values | Description |
|---|---|---|
| ZOHO\_WIDTH |  |
The width of the image. |
| ZOHO\_HEIGHT |  |
The height of the image |
| ZOHO\_TITLE | true / false | Controls whether the title of the report is to be added to the image. true - Include the title. false - Do not include title. |
| ZOHO\_DESCRIPTION | true/false | Controls whether the description of the report is to be added to the image. true - Include the description. false - Do not include description. |
| ZOHO\_SHOWLEGEND | true / false | Controls whether the legend is to be included in the image generated. true - Include the legend in the image. false - Do not include the legend in the image. |
| ZOHO\_IMAGE\_FORMAT | png / jpg | The format of the exported image. It could be either in PNG or JPG formats. |
JSON Format
| Parameter | Possible Values | Description |
|---|---|---|
| ZOHO\_SHOW\_HIDDENCOLS | true / false | Controls where the columns that have been hidden in the table/report have to be exported. true - To include the hidden columns of the table/report in the data exported false - To not include the hidden columns of the table/report in the data exported. |
| ZOHO\_CALLBACK\_FUNCTION | Name of the json callback function | Processes JSON response elsewhere in the JavaScript code on the page |
Example: JSON callback. 1. Define the callback function.
2.Invoke the api request with output format as JSON and ZOHO\_CALLBACK\_FUNCTION=sampleFunction.
When the page is loaded, the response will be returned as,
sampleFunction
({
"response":
{
"uri": "/api/abc@zylker.com/EmployeeDB/EmployeeDetails",
"action": "EXPORT",
"result":
{
column\_order:["Name","Department","Date Of Birth"],
rows:[
["John","Finance","12 May 1972"],
["Joan","Admin","15 June 1975"]
]
}
}
});
JSON Callbacks - JSONP:
Zoho Analytics On-Premise API supports Callback function for handling API responses asynchronously. This is supported in Export API calls, when the output format is chosen as JSON.
The Export API method call, with JSON output format, supports an additional parameter called ZOHO\_CALLBACK\_FUNCTION to enable callback. Using the Callback function, developers can invoke the Export API request inside the 