
# OWASP Web Security Testing Guide (WSTG) Checklist

This checklist is based on the OWASP Web Security Testing Guide and provides a comprehensive framework for testing web application security. Each test includes objectives to guide your testing approach.

## Information Gathering

- [ ] [WSTG-INFO-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/01-Conduct_Search_Engine_Discovery_Reconnaissance_for_Information_Leakage) - **Conduct Search Engine Discovery Reconnaissance for Information Leakage**

  - Identify what sensitive design and configuration information of the application, system, or organization is exposed directly (on the organization's site) or indirectly (via third-party services).

- [ ] [WSTG-INFO-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server) - **Fingerprint Web Server**

  - Determine the version and type of a running web server to enable further discovery of any known vulnerabilities.

- [ ] [WSTG-INFO-03](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/03-Review_Webserver_Metafiles_for_Information_Leakage) - **Review Webserver Metafiles for Information Leakage**

  - Identify hidden or obfuscated paths and functionality through the analysis of metadata files.
  - Extract and map other information that could lead to a better understanding of the systems at hand.

- [ ] [WSTG-INFO-04](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/04-Enumerate_Applications_on_Webserver) - **Enumerate Applications on Webserver**

  - Enumerate the applications within the scope that exist on a web server.

- [ ] [WSTG-INFO-05](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/05-Review_Web_Page_Content_for_Information_Leakage) - **Review Web Page Content for Information Leakage**

  - Review web page comments, metadata, and redirect bodies to find any information leakage.
  - Gather JavaScript files and review the JS code to better understand the application and to find any information leakage.
  - Identify if source map files or other frontend debug files exist.

- [ ] [WSTG-INFO-06](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/06-Identify_Application_Entry_Points) - **Identify Application Entry Points**

  - Identify possible entry and injection points through request and response analysis.

- [ ] [WSTG-INFO-07](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/07-Map_Execution_Paths_Through_Application) - **Map Execution Paths Through Application**

  - Map the target application and understand the principal workflows.

- [ ] [WSTG-INFO-08](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/08-Fingerprint_Web_Application_Framework) - **Fingerprint Web Application Framework**

  - Fingerprint the components used by the web applications.

- [ ] [WSTG-INFO-09](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/09-Fingerprint_Web_Application) - **Fingerprint Web Application**

- [ ] [WSTG-INFO-10](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/10-Map_Application_Architecture) - **Map Application Architecture**
  - Understand the architecture of the application and the technologies in use.

## Configuration and Deployment Management Testing

- [ ] [WSTG-CONF-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/01-Test_Network_Infrastructure_Configuration) - **Test Network Infrastructure Configuration**

  - Review the applications' configurations set across the network and validate that they are not vulnerable.
  - Validate that used frameworks and systems are secure and not susceptible to known vulnerabilities due to unmaintained software or default settings and credentials.

- [ ] [WSTG-CONF-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/02-Test_Application_Platform_Configuration) - **Test Application Platform Configuration**

  - Ensure that default and known files have been removed.
  - Validate that no debugging code or extensions are left in the production environments.
  - Review the logging mechanisms set in place for the application.

- [ ] [WSTG-CONF-03](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/03-Test_File_Extensions_Handling_for_Sensitive_Information) - **Test File Extensions Handling for Sensitive Information**

  - Brute force sensitive file extensions that might contain raw data such as scripts, credentials, etc.
  - Validate that no system framework bypasses exist for the rules that have been set.

- [ ] [WSTG-CONF-04](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/04-Review_Old_Backup_and_Unreferenced_Files_for_Sensitive_Information) - **Review Old Backup and Unreferenced Files for Sensitive Information**

  - Find and analyse unreferenced files that might contain sensitive information.

- [ ] [WSTG-CONF-05](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/05-Enumerate_Infrastructure_and_Application_Admin_Interfaces) - **Enumerate Infrastructure and Application Admin Interfaces**

  - Identify hidden administrator interfaces and functionality.

- [ ] [WSTG-CONF-06](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/06-Test_HTTP_Methods) - **Test HTTP Methods**

  - Enumerate supported HTTP methods.
  - Test for access control bypass.
  - Test HTTP method overriding techniques.

- [ ] [WSTG-CONF-07](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/07-Test_HTTP_Strict_Transport_Security) - **Test HTTP Strict Transport Security**

  - Review the HSTS header and its validity.

- [ ] [WSTG-CONF-08](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/08-Test_RIA_Cross_Domain_Policy) - **Test RIA Cross Domain Policy**

- [ ] [WSTG-CONF-09](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/09-Test_File_Permission) - **Test File Permission**

  - Review and identify any rogue file permissions.

- [ ] [WSTG-CONF-10](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/10-Test_for_Subdomain_Takeover) - **Test for Subdomain Takeover**

  - Enumerate all possible domains (previous and current).
  - Identify any forgotten or misconfigured domains.

- [ ] [WSTG-CONF-11](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/11-Test_Cloud_Storage) - **Test Cloud Storage**

  - Assess that the access control configuration for the storage services is properly in place.

- [ ] [WSTG-CONF-12](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/12-Test_for_Content_Security_Policy) - **Testing for Content Security Policy**

  - Review the Content-Security-Policy header or meta element to identify misconfigurations.

- [ ] [WSTG-CONF-13](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/13-Test_for_Path_Confusion) - **Test Path Confusion**

  - Make sure application paths are configured correctly.

- [ ] [WSTG-CONF-14](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/14-Test_Other_HTTP_Security_Header_Misconfigurations) - **Test Other HTTP Security Header Misconfigurations**
  - Identify improperly configured security headers.
  - Assess the impact of misconfigured security headers.
  - Validate the correct implementation of required security headers.

## Identity Management Testing

- [ ] [WSTG-IDNT-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/03-Identity_Management_Testing/01-Test_Role_Definitions) - **Test Role Definitions**

  - Identify and document roles used by the application.
  - Attempt to switch, change, or access another role.
  - Review the granularity of the roles and the needs behind the permissions given.

- [ ] [WSTG-IDNT-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/03-Identity_Management_Testing/02-Test_User_Registration_Process) - **Test User Registration Process**

  - Verify that the identity requirements for user registration are aligned with business and security requirements.
  - Validate the registration process.

- [ ] [WSTG-IDNT-03](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/03-Identity_Management_Testing/03-Test_Account_Provisioning_Process) - **Test Account Provisioning Process**

  - Verify which accounts may provision other accounts and of what type.

- [ ] [WSTG-IDNT-04](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/03-Identity_Management_Testing/04-Testing_for_Account_Enumeration_and_Guessable_User_Account) - **Testing for Account Enumeration and Guessable User Account**

  - Review processes that pertain to user identification (_e.g._ registration, login, etc.).
  - Enumerate users where possible through response analysis.

- [ ] [WSTG-IDNT-05](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/03-Identity_Management_Testing/05-Testing_for_Weak_or_Unenforced_Username_Policy) - **Testing for Weak or Unenforced Username Policy**
  - Determine whether a consistent account name structure renders the application vulnerable to account enumeration.
  - Determine whether the application's error messages permit account enumeration.

## Authentication Testing

- [ ] [WSTG-ATHN-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/01-Testing_for_Credentials_Transported_over_an_Encrypted_Channel) - **Testing for Credentials Transported over an Encrypted Channel**

- [ ] [WSTG-ATHN-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/02-Testing_for_Default_Credentials) - **Testing for Default Credentials**

  - Determine whether the application has any user accounts with default passwords.
  - Review whether new user accounts are created with weak or predictable passwords.

- [ ] [WSTG-ATHN-03](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/03-Testing_for_Weak_Lock_Out_Mechanism) - **Testing for Weak Lock Out Mechanism**

  - Evaluate the account lockout mechanism's ability to mitigate brute force password guessing.
  - Evaluate the unlock mechanism's resistance to unauthorized account unlocking.

- [ ] [WSTG-ATHN-04](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/04-Testing_for_Bypassing_Authentication_Schema) - **Testing for Bypassing Authentication Schema**

  - Ensure that authentication is applied across all services that require it.

- [ ] [WSTG-ATHN-05](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/05-Testing_for_Vulnerable_Remember_Password) - **Testing for Vulnerable Remember Password**

  - Validate that the generated session is managed securely and do not put the user's credentials in danger.

- [ ] [WSTG-ATHN-06](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/06-Testing_for_Browser_Cache_Weaknesses) - **Testing for Browser Cache Weaknesses**

  - Review if the application stores sensitive information on the client-side.
  - Review if access can occur without authorization.

- [ ] [WSTG-ATHN-07](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/07-Testing_for_Weak_Authentication_Methods) - **Testing for Weak Authentication Methods**

  - Determine the resistance of the application against brute force password guessing using available password dictionaries by evaluating the length, complexity, reuse, and aging requirements of passwords.

- [ ] [WSTG-ATHN-08](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/08-Testing_for_Weak_Security_Question_Answer) - **Testing for Weak Security Question Answer**

  - Determine the complexity and how straight-forward the questions are.
  - Assess possible user answers and brute force capabilities.

- [ ] [WSTG-ATHN-09](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/09-Testing_for_Weak_Password_Change_or_Reset_Functionalities) - **Testing for Weak Password Change or Reset Functionalities**

  - Determine whether the password change and reset functionality allows accounts to be compromised.

- [ ] [WSTG-ATHN-10](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/10-Testing_for_Weaker_Authentication_in_Alternative_Channel) - **Testing for Weaker Authentication in Alternative Channel**

  - Identify alternative authentication channels.
  - Assess the security measures used and if any bypasses exists on the alternative channels.

- [ ] [WSTG-ATHN-11](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/11-Testing_Multi-Factor_Authentication) - **Testing Multi-Factor Authentication (MFA)**
  - Identify the type of MFA used by the application.
  - Determine whether the MFA implementation is robust and secure.
  - Attempt to bypass the MFA.

## Authorization Testing

- [ ] [WSTG-ATHZ-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/01-Testing_Directory_Traversal_File_Include) - **Testing Directory Traversal File Include**

  - Identify injection points that pertain to path traversal.
  - Assess bypassing techniques and identify the extent of path traversal.

- [ ] [WSTG-ATHZ-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema) - **Testing for Bypassing Authorization Schema**

  - Assess if unauthenticated, horizontal, or vertical access is possible.

- [ ] [WSTG-ATHZ-03](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/03-Testing_for_Privilege_Escalation) - **Testing for Privilege Escalation**

  - Identify injection points related to privilege manipulation.
  - Fuzz or otherwise attempt to bypass security measures.

- [ ] [WSTG-ATHZ-04](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/04-Testing_for_Insecure_Direct_Object_References) - **Testing for Insecure Direct Object References**

  - Identify points where object references may occur.
  - Assess the access control measures and if they're vulnerable to IDOR.

- [ ] [WSTG-ATHZ-05](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/05-Testing_for_OAuth_Weaknesses) - **Testing for OAuth Weaknesses**
  - Determine if OAuth2 implementation is vulnerable or using a deprecated or custom implementation.

## Session Management Testing

- [ ] [WSTG-SESS-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/01-Testing_for_Session_Management_Schema) - **Testing for Session Management Schema**

  - Gather session tokens, for the same user and for different users where possible.
  - Analyze and ensure that enough randomness exists to stop session forging attacks.
  - Modify cookies that are not signed and contain information that can be manipulated.

- [ ] [WSTG-SESS-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/02-Testing_for_Cookies_Attributes) - **Testing for Cookies Attributes**

  - Ensure that the proper security configuration is set for cookies.

- [ ] [WSTG-SESS-03](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/03-Testing_for_Session_Fixation) - **Testing for Session Fixation**

  - Analyze the authentication mechanism and its flow.
  - Force cookies and assess the impact.

- [ ] [WSTG-SESS-04](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/04-Testing_for_Exposed_Session_Variables) - **Testing for Exposed Session Variables**

  - Ensure that proper encryption is implemented.
  - Review the caching configuration.
  - Assess the channel and methods' security.

- [ ] [WSTG-SESS-05](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/05-Testing_for_Cross_Site_Request_Forgery) - **Testing for Cross Site Request Forgery**

  - Determine whether it is possible to initiate requests on a user's behalf that are not initiated by the user.

- [ ] [WSTG-SESS-06](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/06-Testing_for_Logout_Functionality) - **Testing for Logout Functionality**

  - Assess the logout UI.
  - Analyze the session timeout and if the session is properly killed after logout.

- [ ] [WSTG-SESS-07](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/07-Testing_Session_Timeout) - **Testing Session Timeout**

  - Validate that a hard session timeout exists.

- [ ] [WSTG-SESS-08](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/08-Testing_for_Session_Puzzling) - **Testing for Session Puzzling**

  - Identify all session variables.
  - Break the logical flow of session generation.

- [ ] [WSTG-SESS-09](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/09-Testing_for_Session_Hijacking) - **Testing for Session Hijacking**

  - Identify vulnerable session cookies.
  - Hijack vulnerable cookies and assess the risk level.

- [ ] [WSTG-SESS-10](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/10-Testing_JSON_Web_Tokens) - **Testing JSON Web Tokens**

  - Determine whether the JWTs expose sensitive information.
  - Determine whether the JWTs can be tampered with or modified.

- [ ] [WSTG-SESS-11](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/11-Testing_for_Concurrent_Sessions) - **Testing for Concurrent Sessions**
  - Evaluate the application's session management by assessing the handling of multiple active sessions for a single user account.

## Input Validation Testing

- [ ] [WSTG-INPV-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting) - **Testing for Reflected Cross Site Scripting**

  - Identify variables that are reflected in responses.
  - Assess the input they accept and the encoding that gets applied on return (if any).

- [ ] [WSTG-INPV-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/02-Testing_for_Stored_Cross_Site_Scripting) - **Testing for Stored Cross Site Scripting**

  - Identify stored input that is reflected on the client-side.
  - Assess the input they accept and the encoding that gets applied on return (if any).

- [ ] [WSTG-INPV-03](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/03-Testing_for_HTTP_Verb_Tampering) - **Testing for HTTP Verb Tampering**

- [ ] [WSTG-INPV-04](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution) - **Testing for HTTP Parameter Pollution**

  - Identify the backend and the parsing method used.
  - Assess injection points and try bypassing input filters using HPP.

- [ ] [WSTG-INPV-05](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection) - **Testing for SQL Injection**

  - Identify SQL injection points.
  - Assess the severity of the injection and the level of access that can be achieved through it.

- [ ] [WSTG-INPV-06](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/06-Testing_for_LDAP_Injection) - **Testing for LDAP Injection**

  - Identify LDAP injection points.
  - Assess the severity of the injection.

- [ ] [WSTG-INPV-07](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/07-Testing_for_XML_Injection) - **Testing for XML Injection**

  - Identify XML injection points.
  - Assess the types of exploits that can be attained and their severities.

- [ ] [WSTG-INPV-08](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/08-Testing_for_SSI_Injection) - **Testing for SSI Injection**

  - Identify SSI injection points.
  - Assess the severity of the injection.

- [ ] [WSTG-INPV-09](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/09-Testing_for_XPath_Injection) - **Testing for XPath Injection**

  - Identify XPATH injection points.

- [ ] [WSTG-INPV-10](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/10-Testing_for_IMAP_SMTP_Injection) - **Testing for IMAP SMTP Injection**

  - Identify IMAP/SMTP injection points.
  - Understand the data flow and deployment structure of the system.
  - Assess the injection impacts.

- [ ] [WSTG-INPV-11](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11-Testing_for_Code_Injection) - **Testing for Code Injection**

  - Identify injection points where you can inject code into the application.
  - Assess the injection severity.

- [ ] [WSTG-INPV-12](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection) - **Testing for Command Injection**

  - Identify and assess the command injection points.

- [ ] [WSTG-INPV-13](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/13-Testing_for_Buffer_Overflow) - **Testing for Buffer Overflow**

- [ ] [WSTG-INPV-13](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/13-Testing_for_Format_String_Injection) - **Testing for Format String Injection**

  - Assess whether injecting format string conversion specifiers into user-controlled fields causes undesired behavior from the application.

- [ ] [WSTG-INPV-14](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/14-Testing_for_Incubated_Vulnerability) - **Testing for Incubated Vulnerability**

  - Identify injections that are stored and require a recall step to the stored injection.
  - Understand how a recall step could occur.
  - Set listeners or activate the recall step if possible.

- [ ] [WSTG-INPV-15](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/15-Testing_for_HTTP_Splitting_Smuggling) - **Testing for HTTP Splitting Smuggling**

  - Assess if the application is vulnerable to splitting, identifying what possible attacks are achievable.
  - Assess if the chain of communication is vulnerable to smuggling, identifying what possible attacks are achievable.

- [ ] [WSTG-INPV-16](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/16-Testing_for_HTTP_Incoming_Requests) - **Testing for HTTP Incoming Requests**

  - Monitor all incoming and outgoing HTTP requests to the Web Server to inspect any suspicious requests.
  - Monitor HTTP traffic without changes of end user Browser proxy or client-side application.

- [ ] [WSTG-INPV-17](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/17-Testing_for_Host_Header_Injection) - **Testing for Host Header Injection**

  - Assess if the Host header is being parsed dynamically in the application.
  - Bypass security controls that rely on the header.

- [ ] [WSTG-INPV-18](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/18-Testing_for_Server-side_Template_Injection) - **Testing for Server-side Template Injection**

  - Detect template injection vulnerability points.
  - Identify the templating engine.
  - Build the exploit.

- [ ] [WSTG-INPV-19](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/19-Testing_for_Server-Side_Request_Forgery) - **Testing for Server-Side Request Forgery**

  - Identify SSRF injection points.
  - Test if the injection points are exploitable.
  - Asses the severity of the vulnerability.

- [ ] [WSTG-INPV-20](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/20-Testing_for_Mass_Assignment) - **Testing for Mass Assignment**
  - Identify requests that modify objects
  - Assess if it is possible to modify fields never intended to be modified from outside

## Testing for Error Handling

- [ ] [WSTG-ERRH-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/01-Testing_For_Improper_Error_Handling) - **Testing for Improper Error Handling**

  - Identify existing error output.
  - Analyze the different output returned.

- [ ] [WSTG-ERRH-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/02-Testing_for_Stack_Traces) - **Testing for Stack Traces**

## Testing for Weak Cryptography

- [ ] [WSTG-CRYP-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/01-Testing_for_Weak_Transport_Layer_Security) - **Testing for Weak Transport Layer Security**

  - Validate the service configuration.
  - Review the digital certificate's cryptographic strength and validity.
  - Ensure that the TLS security is not bypassable and is properly implemented across the application.

- [ ] [WSTG-CRYP-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/02-Testing_for_Padding_Oracle) - **Testing for Padding Oracle**

  - Identify encrypted messages that rely on padding.
  - Attempt to break the padding of the encrypted messages and analyze the returned error messages for further analysis.

- [ ] [WSTG-CRYP-03](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/03-Testing_for_Sensitive_Information_Sent_via_Unencrypted_Channels) - **Testing for Sensitive Information Sent via Unencrypted Channels**

  - Identify sensitive information transmitted through the various channels.
  - Assess the privacy and security of the channels used.

- [ ] [WSTG-CRYP-04](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/04-Testing_for_Weak_Encryption) - **Testing for Weak Encryption**
  - Provide a guideline for the identification weak encryption or hashing uses and implementations.

## Business Logic Testing

- [ ] [WSTG-BUSL-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/01-Test_Business_Logic_Data_Validation) - **Test Business Logic Data Validation**

  - Identify data injection points.
  - Validate that all checks are occurring on the backend and can't be bypassed.
  - Attempt to break the format of the expected data and analyze how the application is handling it.

- [ ] [WSTG-BUSL-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/02-Test_Ability_to_Forge_Requests) - **Test Ability to Forge Requests**

  - Review the project documentation looking for guessable, predictable, or hidden functionality of fields.
  - Insert logically valid data in order to bypass normal business logic workflow.

- [ ] [WSTG-BUSL-03](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/03-Test_Integrity_Checks) - **Test Integrity Checks**

  - Review the project documentation for components of the system that move, store, or handle data.
  - Determine what type of data is logically acceptable by the component and what types the system should guard against.
  - Determine who should be allowed to modify or read that data in each component.
  - Attempt to insert, update, or delete data values used by each component that should not be allowed per the business logic workflow.

- [ ] [WSTG-BUSL-04](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/04-Test_for_Process_Timing) - **Test for Process Timing**

  - Review the project documentation for system functionality that may be impacted by time.
  - Develop and execute misuse cases.

- [ ] [WSTG-BUSL-05](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/05-Test_Number_of_Times_a_Function_Can_Be_Used_Limits) - **Test Number of Times a Function Can Be Used Limits**

  - Identify functions that must set limits to the times they can be called.
  - Assess if there is a logical limit set on the functions and if it is properly validated.

- [ ] [WSTG-BUSL-06](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/06-Testing_for_the_Circumvention_of_Work_Flows) - **Testing for the Circumvention of Work Flows**

  - Review the project documentation for methods to skip or go through steps in the application process in a different order from the intended business logic flow.
  - Develop a misuse case and try to circumvent every logic flow identified.

- [ ] [WSTG-BUSL-07](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/07-Test_Defenses_Against_Application_Misuse) - **Test Defenses Against Application Misuse**

  - Generate notes from all tests conducted against the system.
  - Review which tests had a different functionality based on aggressive input.
  - Understand the defenses in place and verify if they are enough to protect the system against bypassing techniques.

- [ ] [WSTG-BUSL-08](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/08-Test_Upload_of_Unexpected_File_Types) - **Test Upload of Unexpected File Types**

  - Review the project documentation for file types that are rejected by the system.
  - Verify that the unwelcomed file types are rejected and handled safely.
  - Verify that file batch uploads are secure and do not allow any bypass against the set security measures.

- [ ] [WSTG-BUSL-09](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/09-Test_Upload_of_Malicious_Files) - **Test Upload of Malicious Files**

  - Identify the file upload functionality.
  - Review the project documentation to identify what file types are considered acceptable, and what types would be considered dangerous or malicious.
  - If documentation is not available then consider what would be appropriate based on the purpose of the application.
  - Determine how the uploaded files are processed.
  - Obtain or create a set of malicious files for testing.
  - Try to upload the malicious files to the application and determine whether it is accepted and processed.

- [ ] [WSTG-BUSL-10](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/10-Test-Payment-Functionality) - **Test Payment Functionality**
  - Determine whether the business logic for the e-commerce functionality is robust.
  - Understand how the payment functionality works.
  - Determine whether the payment functionality is secure.

## Client-side Testing

- [ ] [WSTG-CLNT-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/01-Testing_for_DOM-based_Cross_Site_Scripting) - **Testing for DOM-Based Cross Site Scripting**

  - Identify DOM sinks.
  - Build payloads that pertain to every sink type.

- [ ] [WSTG-CLNT-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/02-Testing_for_JavaScript_Execution) - **Testing for JavaScript Execution**

  - Identify sinks and possible JavaScript injection points.

- [ ] [WSTG-CLNT-03](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/03-Testing_for_HTML_Injection) - **Testing for HTML Injection**

  - Identify HTML injection points and assess the severity of the injected content.

- [ ] [WSTG-CLNT-04](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/04-Testing_for_Client-side_URL_Redirect) - **Testing for Client-side URL Redirect**

  - Identify injection points that handle URLs or paths.
  - Assess the locations that the system could redirect to.

- [ ] [WSTG-CLNT-05](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/05-Testing_for_CSS_Injection) - **Testing for CSS Injection**

  - Identify CSS injection points.
  - Assess the impact of the injection.

- [ ] [WSTG-CLNT-06](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/06-Testing_for_Client-side_Resource_Manipulation) - **Testing for Client-side Resource Manipulation**

  - Identify sinks with weak input validation.
  - Assess the impact of the resource manipulation.

- [ ] [WSTG-CLNT-07](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/07-Testing_Cross_Origin_Resource_Sharing) - **Testing Cross Origin Resource Sharing**

  - Identify endpoints that implement CORS.
  - Ensure that the CORS configuration is secure or harmless.

- [ ] [WSTG-CLNT-08](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/08-Testing_for_Cross_Site_Flashing) - **Testing for Cross Site Flashing**

  - Decompile and analyze the application's code.
  - Assess sinks inputs and unsafe method usages.

- [ ] [WSTG-CLNT-09](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/09-Testing_for_Clickjacking) - **Testing for Clickjacking**

  - Assess application vulnerability to clickjacking attacks.

- [ ] [WSTG-CLNT-10](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/10-Testing_WebSockets) - **Testing WebSockets**

  - Identify the usage of WebSockets.
  - Assess its implementation by using the same tests on normal HTTP channels.

- [ ] [WSTG-CLNT-11](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/11-Testing_Web_Messaging) - **Testing Web Messaging**

  - Assess the security of the message's origin.
  - Validate that it's using safe methods and validating its input.

- [ ] [WSTG-CLNT-12](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/12-Testing_Browser_Storage) - **Testing Browser Storage**

  - Determine whether the website is storing sensitive data in client-side storage.
  - The code handling of the storage objects should be examined for possibilities of injection attacks, such as utilizing unvalidated input or vulnerable libraries.

- [ ] [WSTG-CLNT-13](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/13-Testing_for_Cross_Site_Script_Inclusion) - **Testing for Cross Site Script Inclusion**

  - Locate sensitive data across the system.
  - Assess the leakage of sensitive data through various techniques.

- [ ] [WSTG-CLNT-14](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/14-Testing_for_Reverse_Tabnabbing) - **Testing for Reverse Tabnabbing**

## API Testing

- [ ] [WSTG-APIT-01](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/12-API_Testing/01-API_Reconnaissance) - **API Reconnaissance**

  - Find all API endpoints supported by the backend server code, documented or undocumented.
  - Find all parameters for each endpoint supported by the backend server, documented or undocumented.
  - Discover interesting data related to APIs in HTML and JavaScript sent to clients.

- [ ] [WSTG-APIT-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/12-API_Testing/02-API_Broken_Object_Level_Authorization) - **API Broken Object Level Authorization**

  - The objective of this test is to identify whether the API enforces proper **object-level authorization** checks, ensuring that users can only access and manipulate objects they are authorized to interact with.

- [ ] [WSTG-APIT-99](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/12-API_Testing/99-Testing_GraphQL) - **Testing GraphQL**
  - Assess that a secure and production-ready configuration is deployed.
  - Validate all input fields against generic attacks.
  - Ensure that proper access controls are applied.
