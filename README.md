# General Checks

This is just a list of general checks around common application functionality.
## Login page

- [ ] Does the app allow self-registration
	- [ ] Two accounts with the same name
	- [ ] Unicode normalization issues?
- [ ] Check for weak credentials
- [ ] Check for default credentials
- [ ] Check for rate limiting
- [ ] Check for account lockout
- [ ] Test for [SQL injection](notes/sql-injection.md)
- [ ] Test for [NoSQL injection](notes/nosql-injection.md)
- [ ] Check for username enumeration
	- [ ] Error messages
	- [ ] Timing disparity
	- [ ] Content-length
	- [ ] Try with a very long password
- [ ] Is there MFA
	- [ ] Can it be bypassed?
	- [ ] Brute forced if no rate limiting?
	- [ ] How are MFA tokens handled?
		- [ ] Do they expire?
		- [ ] Can they be used more than once?
	- [ ] Navigate directly to authenticated functionality
- [ ] Forgot password functionality?
	- [ ] How is it handled?
	- [ ] Current password required?
	- [ ] Can we change where email goes?
- [ ] Is it using SAML/[OAuth](notes/oauth.md)?
- [ ] Check for issues in client-side JS
- [ ] Can we bypass auth with IP spoofing?
- [ ] Check for [open redirects](notes/open-redirects.md)

## Registration

- [ ] Can anyone register? 
- [ ] What is required for registration?
	- [ ] email, phone number, etc.
	- [ ] Is it strictly enforced?
- [ ] Check for mass assignment
- [ ] Check for unicode normalization issues
- [ ] Registration via API endpoints

## User input

- [ ] Is the input reflected anywhere on the page?
	- [ ] What is the context?
- [ ] Check for [XSS](notes/xss.md)
- [ ] Check for [SQL injection](notes/sql-injection.md)
- [ ] Check for [SSTI](notes/ssti.md)
- [ ] What is the content-type of the request?
	- [ ] Check for [XXE](notes/xxe.md)
	- [ ] Try converting JSON to XML

## State-Changing Actions

- [ ] Check for [CSRF](notes/csrf.md)
- [ ] Check for [broken access control](notes/broken-access-control.md)

## Sensitive data returned

- [ ] Check [CORS](notes/cors.md)
- [ ] Try to send a `POST` or `PUT` request with the data in the body to see if it's possible to update

## Query strings

- [ ] Check for [file inclusion](notes/file-inclusion.md)
- [ ] Check for SQLi
- [ ] Check the network tab to see if the application is sending a secondary request to an internal API: `?user=123` --> `/api/user/123`
	- [ ] Check for [client-side path traversal](notes/client-side-path-traversal.md)

## File Upload

- [ ] What technologies are in use?
    - Important to note to understand what type of web shell might work.
- [ ] What file types are allowed?
- [ ] Is it possible to upload other filetypes by:
    - Changing the extension
    - Changing the content type
        - Try changing to text/html with an XSS payload
    - Removing the content type
    - Appending an allowed file extension
- [ ] Is the check done on the client-side or the server-side?
- [ ] How is a normal file upload processed?
    - Is the filename changed?
    - Is the file stored in a predictable place?
    - Is it possible to access the uploaded file? How?
- [ ] Is it possible to store the file in another location?
    - Check for path traversal in the filename
    - Try over-writing sensitive files, e.g., authorized_keys -- **Be careful with this!**
- [ ] Is the filename reflected in the response?
    - Check for an XSS or RCE in the filename
- [ ] Try uploading an html file with an XSS payload
    - Make sure this is not intended behavior before reporting this. This is common in S3 buckets, but there's very little (if any) impact.
- [ ] Can we upload an SVG
    - Check for XSS depending on where the file is uploaded. Remember that XSS executes in the context of the site.
    - Check for XXE within the SVG if there is some kind of server-side functionality
- [ ] Keep an eye out for CSP bypasses or uses in other parts of the app
    - If we can upload js and use that to bypass CSP with XSS in another part of the app
    - Is there another functionality that uses XML files from uploads? SVGs?

## Invite Functionality

- [ ] Can we control what org we join? 

## JWT

- [ ] Check [JWT](notes/jwt.md) cheatsheet
- [ ] Can we re-use JWTs between systems (e.g., dev --> prod)? 