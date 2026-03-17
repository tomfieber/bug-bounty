# General Checks

This is just a list of general checks around common application functionality.

## Login page

- [ ] Does the app allow self-registration
  - Two accounts with the same name
  - Unicode normalization issues?
- [ ] Check for weak credentials
- [ ] Check for default credentials
- [ ] Test [[notes/brute-forcing|Brute force]]
	- [ ] Check for rate limiting
	- [ ] Check for account lockout
- [ ] Test for [[notes/sql-injection|SQL Injection]]
- [ ] Test for [[notes/nosql-injection|NoSQL Injection]]
- [ ] Check for username enumeration
  - Error messages
  - Timing disparity
  - Content-length
  - Try with a very long password
- [ ] Is there MFA
  - Can it be bypassed?
  - Brute forced if no rate limiting?
  - How are MFA tokens handled?
    - Do they expire?
    - Can they be used more than once?
  - [ ] Navigate directly to authenticated functionality
- [ ] Forgot password functionality?
  - How is it handled?
  - Current password required?
  - Can we change where email goes?
- [ ] Is it using SAML/[[notes/oauth|OAuth]]?
- [ ] Check for issues in client-side JS
- [ ] Can we bypass auth with IP spoofing?
- [ ] Check for [[notes/open-redirects|open redirects]]
- [ ] Password reset poisoning (Host header injection to redirect reset link to attacker domain)
- [ ] Check if login works over HTTP (credentials sent in cleartext)

## Registration

- [ ] Can anyone register?
- [ ] What is required for registration?
  - email, phone number, etc.
  - Is it strictly enforced?
- [ ] Check for mass assignment
- [ ] Check for unicode normalization issues
- [ ] Registration via API endpoints
- [ ] Can we register with an existing user's email by varying case or adding dots/tags? (e.g., `user+tag@gmail.com`)
- [ ] Is email/phone verification required before account is active?
- [ ] Check for race conditions in registration (create two accounts simultaneously with the same email)

## User input

- [ ] Is the input reflected anywhere on the page?
  - What is the context?
- [ ] Check for [[notes/xss|XSS]]
- [ ] Check for [[notes/sql-injection|SQL injection]]
- [ ] Check for [[notes/ssti|SSTI]]
- [ ] Check for [[notes/command-injection|command injection]] (especially in fields that interact with the OS: filenames, hostnames, ping/traceroute tools, PDF generators)
- [ ] What is the content-type of the request?
  - Check for [[notes/xxe|XXE]]
  - Try converting JSON to XML
- [ ] Check for [[notes/prototype-pollution|prototype pollution]] in JSON inputs

## State-Changing Actions

- [ ] Check for [[notes/csrf|CSRF]]
- [ ] Check for [[notes/broken-access-control|broken access control]]
- [ ] Check for race conditions on critical operations (balance transfers, coupon redemption, invite acceptance)
- [ ] Check for missing confirmation steps on destructive actions (account deletion, data export)

## Sensitive data returned

- [ ] Check [[notes/cors|CORS]]
- [ ] Try to send a `POST` or `PUT` request with the data in the body to see if it's possible to update
- [ ] Check if sensitive data is exposed in URL parameters (leaked via Referer header, browser history, logs)
- [ ] Check autocomplete on sensitive fields (passwords, credit cards) — `autocomplete="off"` missing?

## Query strings

- [ ] Check for [[notes/file-inclusion|file inclusion]]
- [ ] Check for SQLi
- [ ] Check the network tab to see if the application is sending a secondary request to an internal API: `?user=123` --> `/api/user/123`
  - Check for [[notes/client-side-path-traversal|client-side path traversal]]
- [ ] Check for [[notes/ssrf|SSRF]] in any URL/redirect parameters
- [ ] Check for HTTP parameter pollution (duplicate params: `?id=1&id=2`)

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
- [ ] Can we replay/reuse invite tokens?
- [ ] Can we escalate privileges by modifying the invite request (e.g., changing the role parameter)?
- [ ] Can we enumerate valid invite tokens?
- [ ] Is there an expiration on invite links?

## JWT

- [ ] Check [[notes/jwt|JWT]] cheatsheet
- [ ] Can we re-use JWTs between systems (e.g., dev --> prod)?

## Session Management

- [ ] Are session tokens sufficiently random and long?
- [ ] Do sessions expire after a reasonable idle period?
- [ ] Is the session invalidated server-side on logout? (Or just cookie deleted client-side?)
- [ ] Is a new session token issued after login? (Session fixation)
- [ ] Are sessions invalidated after password change?
- [ ] Check for concurrent session handling — can we login from multiple locations?
- [ ] Check cookie flags: `Secure`, `HttpOnly`, `SameSite`

## API Endpoints

- [ ] Check [[notes/api-testing|API testing]] cheatsheet
- [ ] Check for unauthenticated access to API endpoints
- [ ] Test all HTTP methods (GET, POST, PUT, DELETE, PATCH, OPTIONS)
- [ ] Check for mass assignment in POST/PUT requests
- [ ] Check for verbose error responses that leak internal info
- [ ] Look for hidden/undocumented endpoints (check JS files, API docs, Swagger/OpenAPI)
- [ ] Check for rate limiting on sensitive endpoints
- [ ] Test API versioning — try accessing older API versions (`/api/v1/` vs `/api/v2/`)

## Security Headers & Configuration

- [ ] Check for missing or misconfigured security headers:
  - `Content-Security-Policy`
  - `X-Content-Type-Options: nosniff`
  - `X-Frame-Options` (clickjacking)
  - `Strict-Transport-Security` (HSTS)
  - `Referrer-Policy`
  - `Permissions-Policy`
- [ ] Check for information disclosure in response headers (`Server`, `X-Powered-By`, `X-AspNet-Version`)
- [ ] Check for `.git`, `.svn`, `.env`, `.DS_Store`, `backup.zip`, etc. exposed on the web root
- [ ] Check `robots.txt` and `sitemap.xml` for interesting paths

## Error Handling

- [ ] Do error pages reveal stack traces, framework versions, or internal paths?
- [ ] Test with malformed input to trigger error pages
- [ ] Check for custom vs. default error pages (default pages leak technology info)
- [ ] Check for different error behavior between environments (e.g., debug mode left on in production)
