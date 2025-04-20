Setting Up White Label BI / Embedded Analytics Solution
Zoho Analytics provides a completely customizable white label BI / embedded analytics solution. This section is about how to set up a white label BI solution for your account.
Request White Label Solution
The white label BI solution of Zoho Analytics is available to customers on request. Register through the form given below. We will get in touch with you at the earliest, and provide you with a demo, before setting up your white label instance.
Request a Demo
Customizing The White Label Solution
You can completely rebrand Zoho Analytics, once the White Label solution has been enabled for your account.
Follow the below steps to customize your White Label solution.
- Login to your Zoho Analytics account.
- Click the Settings icon at the top right corner.
- The Settings page will open. Select White Label.
- The White Label Settings Page will open. Provide the following rebranding details. Options will vary depending on the type (Non SSO, SSO, SAML or JWT) you have requested.
- Domain Name: Enter the website address where the white label solution has to be hosted. (eg: analytics.finepick.com).
Do note that once the domain name is configured, Zoho Analytics will not allow you to edit the domain name by yourself. Write to us at support@zohoanalytics.com, in case you wish to make any changes. - Product Name: Enter the product name. This name will be used in all instances where the name Zoho Analytics is used in the Service.
- Product Logo: Upload a logo for your White Label application. The supported file formats are .gif, .jpg, .png and .bmp and the recommended size of the image is 300x60px. This name be used in all instances where the Zoho Analytics logo is used in the Service.
- Favicon: Upload an icon that you want to display along with the page title in the browser tab. The recommended size of the image is 30x30px.
- Support Mail Id: Enter a support email address. This email address will be used in all instances for email communications where the Zoho Analytics support (support@zohoanalytics.com) email address is currently used.
- Login URL (Applicable for SSO, SAML and JWT): Enter the app/site URL where log in happens in your application. This will be displayed to your user in case he has not logged into your product/service that is integrated with Zoho Analytics and accesses the domain URL directly.
- Logout URL (Applicable for SSO, SAML and JWT): Enter the URL to which the user has to be redirected upon logging out of your application.
- Trusted IP ranges (Applicable for SSO): Enter the IP Address of your app/site from which the authentication request will be sent to Zoho Analytics. You can add multiple IP ranges by clicking the "+ Add New IP Range" link.
- Metadata file (Applicable for SAML): SAML metadata is an XML document that contains the information necessary for interaction with SAML-enabled identity or service providers. Upload your SAML metadata file here.
- JWT Algorithm (Applicable for JWT): Select the JWT Algorithm type as RS256 or HS256.
- RS256 - In case of RS256, upload the RSA Public Key to authenticate signin to your application.
HS256 - In case of HS256, you will get a Secret Key in the White Label Settings page after you complete the setup steps. You can use the JWT Secret Key for setting up the authentication in your application.
Note: The JWT Secret Key can be used to generate JWT Token. Hence, we highly recommend you to keep it confidential.
- Ensure you have set all the fields and click Submit.
- Domain Name: Enter the website address where the white label solution has to be hosted. (eg: analytics.finepick.com).
- The next section will open, requesting you to complete domain redirection and verification.
Click the Click here to verify CNAME link to configure the CNAME mapping of your subdomain. This varies based on the data center in which your Zoho account is in.
The following table lists the CNAME mapping of the subdomain for each data center.Datacenter Cname Mapping Domain US analytics.cs.zohohost.com EU analytics.cs.zohohost.eu IN analytics.cs.zohohost.in AU analytics.cs.zohohost.com.au - Click the Click here to verify domain link to verify the domain ownership. The Domain Verification dialog will open. You can verify using one of the following methods.
- By adding CNAME
- By adding TXT
- By adding File
- By adding CNAME
Once you have completed verifying your domain, our engineering team will customize the White Label Solution as per your specifications. This will take a couple of days. Our team will notify you via an email or a call when your white label solution is ready.
In case of JWT Algorithm with HS256, the following screen will be shown. You can copy the Secret Key for setting up the authentication in your application.