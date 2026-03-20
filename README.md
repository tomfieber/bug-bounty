# Recon

## Whois

```bash
whois $domain
```

## DNS

```bash
dig $domain
```

```bash
dig +short $domain
```

Subdomain Bruteforcing

```bash
dnsenum --enum inlanefreight.com -f /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt
```

Zone transfer

```bash
dig axfr @nsztm1.digi.ninja zonetransfer.me
```

Vhosts

```bash
gobuster vhost -u http://$ip -w <wordlist_file> --append-domain
```

## Fingerprinting

Headers

```bash
curl -I https://inlanefreight.com
```

WAF

```bash
wafw00f inlanefreight.com
```

Vuln Scanning

```bash
nikto -h inlanefreight.com -Tuning b
```

```bash
nuclei -l inlanefreight.com
```

## Crawling

Check for robots.txt, well-known, etc.

ReconSpider

```bash
python3 ReconSpider.py http://inlanefreight.com
```

NOTE: Requires `scapy`.

## Google Dorking

| Operator                | Operator Description                                         | Example                                             | Example Description                                                                     |
| :---------------------- | :----------------------------------------------------------- | :-------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| `site:`                 | Limits results to a specific website or domain.              | `site:example.com`                                  | Find all publicly accessible pages on example.com.                                      |
| `inurl:`                | Finds pages with a specific term in the URL.                 | `inurl:login`                                       | Search for login pages on any website.                                                  |
| `filetype:`             | Searches for files of a particular type.                     | `filetype:pdf`                                      | Find downloadable PDF documents.                                                        |
| `intitle:`              | Finds pages with a specific term in the title.               | `intitle:"confidential report"`                     | Look for documents titled "confidential report" or similar variations.                  |
| `intext:` or `inbody:`  | Searches for a term within the body text of pages.           | `intext:"password reset"`                           | Identify webpages containing the term “password reset”.                                 |
| `cache:`                | Displays the cached version of a webpage (if available).     | `cache:example.com`                                 | View the cached version of example.com to see its previous content.                     |
| `link:`                 | Finds pages that link to a specific webpage.                 | `link:example.com`                                  | Identify websites linking to example.com.                                               |
| `related:`              | Finds websites related to a specific webpage.                | `related:example.com`                               | Discover websites similar to example.com.                                               |
| `info:`                 | Provides a summary of information about a webpage.           | `info:example.com`                                  | Get basic details about example.com, such as its title and description.                 |
| `define:`               | Provides definitions of a word or phrase.                    | `define:phishing`                                   | Get a definition of "phishing" from various sources.                                    |
| `numrange:`             | Searches for numbers within a specific range.                | `site:example.com numrange:1000-2000`               | Find pages on example.com containing numbers between 1000 and 2000.                     |
| `allintext:`            | Finds pages containing all specified words in the body text. | `allintext:admin password reset`                    | Search for pages containing both "admin" and "password reset" in the body text.         |
| `allinurl:`             | Finds pages containing all specified words in the URL.       | `allinurl:admin panel`                              | Look for pages with "admin" and "panel" in the URL.                                     |
| `allintitle:`           | Finds pages containing all specified words in the title.     | `allintitle:confidential report 2023`               | Search for pages with "confidential," "report," and "2023" in the title.                |
| `AND`                   | Narrows results by requiring all terms to be present.        | `site:example.com AND (inurl:admin OR inurl:login)` | Find admin or login pages specifically on example.com.                                  |
| `OR`                    | Broadens results by including pages with any of the terms.   | `"linux" OR "ubuntu" OR "debian"`                   | Search for webpages mentioning Linux, Ubuntu, or Debian.                                |
| `NOT`                   | Excludes results containing the specified term.              | `site:bank.com NOT inurl:login`                     | Find pages on bank.com excluding login pages.                                           |
| `*` (wildcard)          | Represents any character or word.                            | `site:socialnetwork.com filetype:pdf user* manual`  | Search for user manuals (user guide, user handbook) in PDF format on socialnetwork.com. |
| `..` (range search)     | Finds results within a specified numerical range.            | `site:ecommerce.com "price" 100..500`               | Look for products priced between 100 and 500 on an e-commerce website.                  |
| `" "` (quotation marks) | Searches for exact phrases.                                  | `"information security policy"`                     | Find documents mentioning the exact phrase "information security policy".               |
| `-` (minus sign)        | Excludes terms from the search results.                      | `site:news.com -inurl:sports`                       | Search for news articles on news.com excluding sports-related content.                  |
## Finalrecon

```bash
./finalrecon.py --headers --whois --url http://inlanefreight.com
```

# Web Fuzzing

## Recursive Fuzzing

```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -ic -v -u http://IP:PORT/FUZZ -e .html -recursion
```

```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -ic -u http://IP:PORT/FUZZ -e .html -recursion -recursion-depth 2 -rate 500
```

## Fuzzing Parameters

```bash
ffuf -u http://IP:PORT/post.php -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "y=FUZZ" -w /usr/share/seclists/Discovery/Web-Content/common.txt -mc 200 -v
```

## Vhost Fuzzing

```bash
gobuster vhost -u http://inlanefreight.htb:81 -w /usr/share/seclists/Discovery/Web-Content/common.txt --append-domain
```

## Subdomain Fuzzing

```bash
gobuster dns -d inlanefreight.com -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
```


# Login page

## Login Bypass

Check for weak credentials
Check for default credentials
Test [Brute force](notes/brute-forcing.md)
- Check for rate limiting
- Check for account lockout
Check for username enumeration
- Error messages
- Timing disparity
- Content-length
- Try with a very long password
Is there MFA
- Can it be bypassed?
- Brute forced if no rate limiting?
- How are MFA tokens handled?
	- Do they expire?
	- Can they be used more than once?
- Navigate directly to authenticated functionality
Forgot password functionality?
  - How is it handled?
  - Current password required?
  - Can we change where email goes?
Is it using SAML/[OAuth](notes/oauth.md)?
Check for issues in client-side JS
Can we bypass auth with IP spoofing?
Check for [open redirects](notes/open-redirects.md)
Password reset poisoning (Host header injection to redirect reset link to attacker domain)
Check if login works over HTTP (credentials sent in cleartext)
Try login with different methods (POST -> GET, GET -> POST)


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
- [ ] Check for [XSS](notes/xss.md)
- [ ] Check for [SQL injection](notes/sql-injection.md)
- [ ] Check for [SSTI](notes/ssti.md)
- [ ] Check for [SSI](notes/ssi.md)
- [ ] Check for [command injection](notes/command-injection.md) (especially in fields that interact with the OS: filenames, hostnames, ping/traceroute tools, PDF generators)
- [ ] What is the content-type of the request?
  - Check for [XXE](notes/xxe.md)
  - Try converting JSON to XML
- [ ] Check for [prototype pollution](notes/prototype-pollution.md) in JSON inputs

## State-Changing Actions

- [ ] Check for [CSRF](notes/csrf.md)
- [ ] Check for [broken access control](notes/broken-access-control.md)
- [ ] Check for race conditions on critical operations (balance transfers, coupon redemption, invite acceptance)
- [ ] Check for missing confirmation steps on destructive actions (account deletion, data export)

## Sensitive data returned

- [ ] Check [CORS](notes/cors.md)
- [ ] Try to send a `POST` or `PUT` request with the data in the body to see if it's possible to update
- [ ] Check if sensitive data is exposed in URL parameters (leaked via Referer header, browser history, logs)
- [ ] Check autocomplete on sensitive fields (passwords, credit cards) — `autocomplete="off"` missing?

## Query strings

- [ ] Check for [file inclusion](notes/file-inclusion.md)
- [ ] Check for SQLi
- [ ] Check the network tab to see if the application is sending a secondary request to an internal API: `?user=123` --> `/api/user/123`
  - Check for [client-side path traversal](notes/client-side-path-traversal.md)
- [ ] Check for [SSRF](notes/ssrf.md) in any URL/redirect parameters
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

- [ ] Check [JWT](notes/jwt.md) cheatsheet
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

- [ ] Check [API testing](notes/api-testing.md) cheatsheet
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
