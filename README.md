# Web Application Security Testing Checklist

> Structured checklist for web application security assessments. Each section links to detailed technique cheatsheets in the `notes/` directory.

## Contents

- [Reconnaissance](#reconnaissance)
- [JavaScript Analysis](#javascript-analysis)
- [Authentication & Login](#authentication--login)
- [User Input](#user-input)
- [State-Changing Actions](#state-changing-actions)
- [Sensitive Data Exposure](#sensitive-data-exposure)
- [Query Strings & Parameters](#query-strings--parameters)
- [File Upload](#file-upload)
- [Invite Functionality](#invite-functionality)
- [JWT](#jwt)
- [Session Management](#session-management)
- [API Endpoints](#api-endpoints)
- [Security Headers & Configuration](#security-headers--configuration)
- [Error Handling](#error-handling)

---

## Reconnaissance

- [ ] Check `whois` data
- [ ] Check DNS records with `dig` — see [DNS](notes/dns.md)
- [ ] Fuzz for subdomains and virtual hosts
- [ ] Check for zone transfers
- [ ] Check for subdomain takeover
- [ ] Fingerprint the target
  - WAF — see [WAF Bypass](notes/waf-bypass.md)
  - Response headers
  - Tech stack
- [ ] Run initial vulnerability scans
- [ ] Crawl the site for content discovery — see [Web Fuzzing](notes/web-fuzzing.md)
- [ ] Google dorking

See [Recon](notes/recon.md) for detailed commands and workflows.

---

## JavaScript Analysis

- [ ] Collect all JS files
  - Check for secrets, API keys, credentials
  - Look for additional routes and endpoints
  - Identify subdomains referenced in code
- [ ] Deobfuscate any minified/obfuscated JS

See [JavaScript Deobfuscation](notes/javascript-deobfuscation.md) for tools and techniques.

---

## Authentication & Login

### Login Bypass

- [ ] Check for weak credentials
- [ ] Check for default credentials
- [ ] Test [Brute force](notes/brute-forcing.md)
  - Check for rate limiting
  - Check for account lockout
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
  - Navigate directly to authenticated functionality
- [ ] Forgot password functionality?
  - How is it handled?
  - Current password required?
  - Can we change where email goes?
- [ ] Is it using SAML/[OAuth](notes/oauth.md)?
- [ ] Check for issues in client-side JS
- [ ] Can we bypass auth with IP spoofing?
- [ ] Check for [open redirects](notes/open-redirects.md)
- [ ] Password reset poisoning via [Host header injection](notes/host-header-attacks.md)
- [ ] Check if login works over HTTP (credentials sent in cleartext)
- [ ] Try login with different methods (POST -> GET, GET -> POST)

### Registration

- [ ] Can anyone register?
- [ ] What is required for registration?
  - email, phone number, etc.
  - Is it strictly enforced?
- [ ] Check for mass assignment
- [ ] Check for unicode normalization issues
- [ ] Registration via API endpoints
- [ ] Can we register with an existing user's email by varying case or adding dots/tags? (e.g., `user+tag@gmail.com`)
- [ ] Is email/phone verification required before account is active?
- [ ] Check for [race conditions](notes/race-conditions.md) in registration (create two accounts simultaneously with the same email)

---

## User Input

- [ ] Is input reflected anywhere on the page? In what context?
- [ ] Check for [XSS](notes/xss.md) (reflected, stored, DOM-based)
- [ ] Check for [SQL injection](notes/sql-injection/sql-injection.md)
- [ ] Check for [SSTI](notes/ssti.md)
- [ ] Check for [SSI injection](notes/ssi.md)
- [ ] Check for [command injection](notes/command-injection.md) — especially in fields that interact with the OS (filenames, hostnames, ping/traceroute tools, PDF generators)
- [ ] Check for [NoSQL injection](notes/nosql-injection.md) on JSON-based inputs
- [ ] Check for [LDAP injection](notes/ldap-injection.md) on directory-connected forms
- [ ] Check for [XPath injection](notes/xpath-injection.md) on XML-backed forms
- [ ] Check request content-type
  - Check for [XXE](notes/xxe.md)
  - Try converting JSON to XML
- [ ] Check for [prototype pollution](notes/prototype-pollution.md) in JSON inputs

---

## State-Changing Actions

- [ ] Check for [CSRF](notes/csrf.md)
- [ ] Check for [broken access control / IDOR](notes/broken-access-control.md)
- [ ] Check for [race conditions](notes/race-conditions.md) on critical operations (balance transfers, coupon redemption, invite acceptance)
- [ ] Check for missing confirmation steps on destructive actions (account deletion, data export)

---

## Sensitive Data Exposure

- [ ] Check [CORS](notes/cors.md) configuration
- [ ] Try sending `POST` or `PUT` requests with returned data to test for unauthorized updates
- [ ] Check if sensitive data is exposed in URL parameters (leaked via Referer header, browser history, logs)
- [ ] Check `autocomplete` on sensitive fields (passwords, credit cards) — `autocomplete="off"` missing?

---

## Query Strings & Parameters

- [ ] Check for [file inclusion](notes/file-inclusion.md) (LFI/RFI)
- [ ] Check for [SQL injection](notes/sql-injection/sql-injection.md)
- [ ] Monitor network tab for secondary API requests: `?user=123` → `/api/user/123`
  - Check for [client-side path traversal](notes/client-side-path-traversal.md)
- [ ] Check for [SSRF](notes/ssrf.md) in any URL/redirect parameters
- [ ] Check for HTTP parameter pollution (duplicate params: `?id=1&id=2`)

---

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
  - Check for an [XSS](notes/xss.md) or [RCE](notes/rce.md) in the filename
- [ ] Try uploading an html file with an XSS payload
  - Make sure this is not intended behavior before reporting this. This is common in S3 buckets, but there's very little (if any) impact.
- [ ] Can we upload an SVG
  - Check for [XSS](notes/xss.md) depending on where the file is uploaded. Remember that XSS executes in the context of the site.
  - Check for [XXE](notes/xxe.md) within the SVG if there is some kind of server-side functionality
- [ ] Keep an eye out for CSP bypasses or uses in other parts of the app
  - If we can upload JS and use that to bypass CSP with [XSS](notes/xss.md) in another part of the app
  - Is there another functionality that uses XML files from uploads? SVGs?

See [File Upload](notes/file-upload.md) for payloads, bypasses, and web shells.

---

## Invite Functionality

- [ ] Can we control what org we join?
- [ ] Can we replay/reuse invite tokens?
- [ ] Can we escalate privileges by modifying the invite request (e.g., changing the role parameter)?
- [ ] Can we enumerate valid invite tokens?
- [ ] Is there an expiration on invite links?

---

## JWT

- [ ] Check [JWT](notes/jwt.md) cheatsheet
- [ ] Can JWTs be reused across environments (e.g., dev → prod)?

---

## Session Management

- [ ] Are session tokens sufficiently random and long?
- [ ] Do sessions expire after a reasonable idle period?
- [ ] Is the session invalidated server-side on logout? (Or just cookie deleted client-side?)
- [ ] Is a new session token issued after login? (Session fixation)
- [ ] Are sessions invalidated after password change?
- [ ] Check for concurrent session handling — can we login from multiple locations?
- [ ] Check cookie flags: `Secure`, `HttpOnly`, `SameSite`

---

## API Endpoints

- [ ] Check the [API Testing](notes/api-testing.md) cheatsheet
- [ ] Check for unauthenticated access to API endpoints
- [ ] Test all HTTP methods (GET, POST, PUT, DELETE, PATCH, OPTIONS)
- [ ] Check for mass assignment in POST/PUT requests
- [ ] Check for verbose error responses that leak internal info
- [ ] Look for hidden/undocumented endpoints (check JS files, API docs, Swagger/OpenAPI)
- [ ] Check for rate limiting on sensitive endpoints
- [ ] Test API versioning — try accessing older API versions (`/api/v1/` vs `/api/v2/`)
- [ ] Test for [GraphQL](notes/graphql.md) vulnerabilities if applicable

---

## Security Headers & Configuration

- [ ] Check for missing or misconfigured security headers:
  - `Content-Security-Policy`
  - `X-Content-Type-Options: nosniff`
  - `X-Frame-Options` (clickjacking)
  - `Strict-Transport-Security` (HSTS)
  - `Referrer-Policy`
  - `Permissions-Policy`
- [ ] Check for information disclosure in response headers (`Server`, `X-Powered-By`, `X-AspNet-Version`)
- [ ] Check for exposed files on the web root: `.git`, `.svn`, `.env`, `.DS_Store`, `backup.zip`, `docker-compose.yml`
- [ ] Check `robots.txt` and `sitemap.xml` for interesting paths

---

## Error Handling

- [ ] Do error pages reveal stack traces, framework versions, or internal paths?
- [ ] Test with malformed input to trigger error pages
- [ ] Check for custom vs. default error pages (default pages leak technology info)
- [ ] Check for different error behavior between environments (e.g., debug mode left on in production)
