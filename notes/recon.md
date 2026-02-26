# Recon

Check [bgp.he.net](https://bgp.he.net)

> [!tip]
> Check for owned infrastructure. Akamai, AWS, etc. aren't helpful.

### ASN Mapping

```bash
echo AS12345 | asnmap -silent | naabu -silent
```

```bash
echo AS12345 | asnmap -silent | naabu -silent -nmap-cli 'nmap -sV'
```

**Amass lookup**

```bash
amass intel -asn <ASN_Number> -o asn_ips.txt
```

### Subdomain Enumeration

**bbot**

```bash
bbot -t $domain -p subdomain-enum
```

```bash
cat ~/.bbot/scans/$name/subdomains.txt | anew domain-subs-final
```

**crt.sh**

```bash
curl -s "https://crt.sh/?q=%25.$domain&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | anew domain-subs-final
```

**subfinder**

```bash
subfinder -dL domains -all -stats -nW -oI -o domain-subfinder-out
```

```bash
cat domain-subfinder-out | awk -F ',' '{print $1}' > subfinder-subs-only
```

```bash
cat subfinder-subs-only | anew domain-subs-final
```

**shosubgo**

> [!warning]
> This will burn through a normal shodan API limit

```bash
shosubgo -d $domain -s $SHODAN_API_KEY -o shosubgo-subs-out
```

```bash
cat -p shosubgo-subs-out | anew domain-subs-final
```

### Clean up Wildcards

```bash
cat domain-subs-final | grep -v "_wildcard" > o && mv o domain-subs-final
```

### DNS Brute Force and Resolution

Checking for alterations

```bash
cat domain-subs-final | dnsgen - | puredns resolve --resolvers resolvers.txt
```

```bash
cat domain-subs-final | alterx | dnsx -resp -silent -r resolvers.txt -o subdomains-resolved.txt
```

```bash
cat subdomains-resolved.txt | awk '{print $1}' | sort -u > resolved-subdomains-sorted.txt
```

### Find Live Hosts

```bash
httpx -l resolved-subdomains.txt -status-code -title -content-length -web-server -asn -location -no-color -follow-redirects -t 15 -ports 80,8080,443,8443,4443,8888 -no-fallback -probe-all-ips -random-agent -o live-websites -oa
```

> [!tip]
> Open the CSV file in Google Sheets/Excel and use that to sort by status code

**Check for admin/login endpoints**

```bash
cat live-websites | grep -i "login\|admin" | tee login_endpoints.txt
```

### Find URLs and Paths

**waymore**

```bash
waymore -i $domain -mode B -oU ./waymoreUrls.txt -oR ./waymoreResponses --notify-discord
```

```bash
cat live-websites | waymore -mode B -oU ./waymoreUrls.txt -oR ./waymoreResponses --notify-discord
```

**katana**

```bash
katana -l live-websites -silent -jc -jsl -o katana_results.txt
```

**Find more links with xnLinkFinder**

```bash
xnLinkFinder -i ~/.config/waymore/results/$domain -sp https://$domain -sf $domain -o js_files.txt
```

## JS Analysis

```bash
cat js_files.txt | gf aws-keys | tee aws_keys.txt
cat js_files.txt | gf urls | tee sensitive_urls.txt
```

## Initial Vulnerability Checks

**CSRF Checks**

```bash
cat live-websites | gf csrf | tee csrf_endpoints.txt
```

**LFI Checks**

```bash
cat live-websites | gf lfi | qsreplace "/etc/passwd" | xargs -I@ curl -s @ | grep "root:x:" > lfi_results.txt
```

**SQLi Testing**

```bash
ghauri -u "https://target.com?id=1" --dbs --batch
```

**Sensitive Data Check**

```bash
cat js_files.txt | grep -Ei "key|token|auth|password" > sensitive_data.txt
```

**Open Redirect Search**

```bash
cat urls.txt | grep "=http" | qsreplace "https://evil.com" | xargs -I@ curl -I -s @ | grep "evil.com"
```

## Technology Fingerprinting

```bash
whatweb -a 3 https://target.com
```

```bash
wappalyzer https://target.com
```

- [ ] Check response headers for server info (`X-Powered-By`, `Server`, etc.)
- [ ] Check `/robots.txt`, `/sitemap.xml`, `/.well-known/security.txt`
- [ ] Check for common CMS paths (`/wp-admin`, `/administrator`, `/wp-json/wp/v2/users`)

## Port Scanning

```bash
naabu -host target.com -top-ports 1000 -silent
```

```bash
nmap -sV -sC -p- target.com -oA nmap-full
```

## Google Dorking

```
site:target.com ext:php | ext:asp | ext:jsp | ext:env | ext:log
site:target.com inurl:admin | inurl:login | inurl:dashboard
site:target.com intitle:"index of"
site:target.com filetype:pdf | filetype:doc | filetype:xls
"target.com" inurl:api | inurl:graphql | inurl:swagger
```

## GitHub / Secret Scanning

```bash
# Search for secrets in target's repos
trufflehog github --org=target --only-verified
```

- [ ] Check for leaked API keys, credentials, internal URLs
- [ ] Search for `.env` files, config files, internal documentation
- [ ] Check employee personal repos for target-related code

# Web Recon

Web reconnaissance is the first step in any security assessment or penetration testing engagement. It's akin to a detective's initial investigation, meticulously gathering clues and evidence about a target before formulating a plan of action. In the digital realm, this translates to accumulating information about a website or web application to identify potential vulnerabilities, security misconfigurations, and valuable assets.

The primary goals of web reconnaissance revolve around gaining a comprehensive understanding of the target's digital footprint. This includes:

- `Identifying Assets`: Discovering all associated domains, subdomains, and IP addresses provides a map of the target's online presence.
- `Uncovering Hidden Information`: Web reconnaissance aims to uncover directories, files, and technologies that are not readily apparent and could serve as entry points for an attacker.
- `Analyzing the Attack Surface`: By identifying open ports, running services, and software versions, you can assess the potential vulnerabilities and weaknesses of the target.
- `Gathering Intelligence`: Collecting information about employees, email addresses, and technologies used can aid in social engineering attacks or identifying specific vulnerabilities associated with certain software.

Web reconnaissance can be conducted using either active or passive techniques, each with its own advantages and drawbacks:

|Type|Description|Risk of Detection|Examples|
|---|---|---|---|
|Active Reconnaissance|Involves directly interacting with the target system, such as sending probes or requests.|Higher|Port scanning, vulnerability scanning, network mapping|
|Passive Reconnaissance|Gathers information without directly interacting with the target, relying on publicly available data.|Lower|Search engine queries, WHOIS lookups, DNS enumeration, web archive analysis, social media|

## WHOIS

WHOIS is a query and response protocol used to retrieve information about domain names, IP addresses, and other internet resources. It's essentially a directory service that details who owns a domain, when it was registered, contact information, and more. In the context of web reconnaissance, WHOIS lookups can be a valuable source of information, potentially revealing the identity of the website owner, their contact information, and other details that could be used for further investigation or social engineering attacks.

For example, if you wanted to find out who owns the domain `example.com`, you could run the following command in your terminal:

```bash
whois example.com
```

This would return a wealth of information, including the registrar, registration, and expiration dates, nameservers, and contact information for the domain owner.

However, it's important to note that WHOIS data can be inaccurate or intentionally obscured, so it's always wise to verify the information from multiple sources. Privacy services can also mask the true owner of a domain, making it more difficult to obtain accurate information through WHOIS.

## DNS

The Domain Name System (DNS) functions as the internet's GPS, translating user-friendly domain names into the numerical IP addresses computers use to communicate. Like GPS converting a destination's name into coordinates, DNS ensures your browser reaches the correct website by matching its name with its IP address. This eliminates memorizing complex numerical addresses, making web navigation seamless and efficient.

The `dig` command allows you to query DNS servers directly, retrieving specific information about domain names. For instance, if you want to find the IP address associated with `example.com`, you can execute the following command:

```bash
dig example.com A
```

This command instructs `dig` to query the DNS for the `A` record (which maps a hostname to an IPv4 address) of `example.com`. The output will typically include the requested IP address, along with additional details about the query and response. By mastering the `dig` command and understanding the various DNS record types, you gain the ability to extract valuable information about a target's infrastructure and online presence.

DNS servers store various types of records, each serving a specific purpose:

|Record Type|Description|
|---|---|
|A|Maps a hostname to an IPv4 address.|
|AAAA|Maps a hostname to an IPv6 address.|
|CNAME|Creates an alias for a hostname, pointing it to another hostname.|
|MX|Specifies mail servers responsible for handling email for the domain.|
|NS|Delegates a DNS zone to a specific authoritative name server.|
|TXT|Stores arbitrary text information.|
|SOA|Contains administrative information about a DNS zone.|

## Subdomains

Subdomains are essentially extensions of a primary domain name, often used to organize different sections or services within a website. For example, a company might use `mail.example.com` for their email server or `blog.example.com` for their blog.

From a reconnaissance perspective, subdomains are incredibly valuable. They can expose additional attack surfaces, reveal hidden services, and provide clues about the internal structure of a target's network. Subdomains might host development servers, staging environments, or even forgotten applications that haven't been properly secured.

The process of discovering subdomains is known as subdomain enumeration. There are two main approaches to subdomain enumeration:

|Approach|Description|Examples|
|---|---|---|
|`Active Enumeration`|Directly interacts with the target's DNS servers or utilizes tools to probe for subdomains.|Brute-forcing, DNS zone transfers|
|`Passive Enumeration`|Collects information about subdomains without directly interacting with the target, relying on public sources.|Certificate Transparency (CT) logs, search engine queries|

`Active enumeration` can be more thorough but carries a higher risk of detection. Conversely, `passive enumeration` is stealthier but may not uncover all subdomains. Combining both techniques can significantly increase the likelihood of discovering a comprehensive list of subdomains associated with your target, expanding your understanding of their online presence and potential vulnerabilities.

### Subdomain Brute-Forcing

Subdomain brute-forcing is a proactive technique used in web reconnaissance to uncover subdomains that may not be readily apparent through passive methods. It involves systematically generating many potential subdomain names and testing them against the target's DNS server to see if they exist. This approach can unveil hidden subdomains that may host valuable information, development servers, or vulnerable applications.

One of the most versatile tools for subdomain brute-forcing is `dnsenum`. This powerful command-line tool combines various DNS enumeration techniques, including dictionary-based brute-forcing, to uncover subdomains associated with your target.

To use `dnsenum` for subdomain brute-forcing, you'll typically provide it with the target domain and a wordlist containing potential subdomain names. The tool will then systematically query the DNS server for each potential subdomain and report any that exist.

For example, the following command would attempt to brute-force subdomains of `example.com` using a wordlist named `subdomains.txt`:

```bash
dnsenum example.com -f subdomains.txt
```

### Zone Transfers

DNS zone transfers, also known as AXFR (Asynchronous Full Transfer) requests, offer a potential goldmine of information for web reconnaissance. A zone transfer is a mechanism for replicating DNS data across servers. When a zone transfer is successful, it provides a complete copy of the DNS zone file, which contains a wealth of details about the target domain.

This zone file lists all the domain's subdomains, their associated IP addresses, mail server configurations, and other DNS records. This is akin to obtaining a blueprint of the target's DNS infrastructure for a reconnaissance expert.

To attempt a zone transfer, you can use the `dig` command with the `axfr` (full zone transfer) option. For example, to request a zone transfer from the DNS server `ns1.example.com` for the domain `example.com`, you would execute:

```bash
dig @ns1.example.com example.com axfr
```

However, zone transfers are not always permitted. Many DNS servers are configured to restrict zone transfers to authorized secondary servers only. Misconfigured servers, though, may allow zone transfers from any source, inadvertently exposing sensitive information.

### Virtual Hosts

Virtual hosting is a technique that allows multiple websites to share a single IP address. Each website is associated with a unique hostname, which is used to direct incoming requests to the correct site. This can be a cost-effective way for organizations to host multiple websites on a single server, but it can also create a challenge for web reconnaissance.

Since multiple websites share the same IP address, simply scanning the IP won't reveal all the hosted sites. You need a tool that can test different hostnames against the IP address to see which ones respond.

Gobuster is a versatile tool that can be used for various types of brute-forcing, including virtual host discovery. Its `vhost` mode is designed to enumerate virtual hosts by sending requests to the target IP address with different hostnames. If a virtual host is configured for a specific hostname, Gobuster will receive a response from the web server.

To use Gobuster to brute-force virtual hosts, you'll need a wordlist containing potential hostnames. Here's an example command:

```bash
gobuster vhost -u http://192.0.2.1 -w hostnames.txt
```

In this example, `-u` specifies the target IP address, and `-w` specifies the wordlist file. Gobuster will then systematically try each hostname in the wordlist and report any that results in a valid response from the web server.

### Certificate Transparency (CT) Logs

Certificate Transparency (CT) logs offer a treasure trove of subdomain information for passive reconnaissance. These publicly accessible logs record SSL/TLS certificates issued for domains and their subdomains, serving as a security measure to prevent fraudulent certificates. For reconnaissance, they offer a window into potentially overlooked subdomains.

The `crt.sh` website provides a searchable interface for CT logs. To efficiently extract subdomains using `crt.sh` within your terminal, you can use a command like this:

```bash
curl -s "https://crt.sh/?q=%25.example.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u
```

This command fetches JSON-formatted data from `crt.sh` for `example.com` (the `%` is a wildcard), extracts domain names using `jq`, removes any wildcard prefixes (`*.`) with `sed`, and finally sorts and deduplicates the results.

## Web Crawling

Web crawling is the automated exploration of a website's structure. A web crawler, or spider, systematically navigates through web pages by following links, mimicking a user's browsing behavior. This process maps out the site's architecture and gathers valuable information embedded within the pages.

A crucial file that guides web crawlers is `robots.txt`. This file resides in a website's root directory and dictates which areas are off-limits for crawlers. Analyzing `robots.txt` can reveal hidden directories or sensitive areas that the website owner doesn't want to be indexed by search engines.

`Scrapy` is a powerful and efficient Python framework for large-scale web crawling and scraping projects. It provides a structured approach to defining crawling rules, extracting data, and handling various output formats.

Here's a basic Scrapy spider example to extract links from `example.com`:

```python
import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ['http://example.com/']

    def parse(self, response):
        for link in response.css('a::attr(href)').getall():
            if any(link.endswith(ext) for ext in self.interesting_extensions):
                yield {"file": link}
            elif not link.startswith("#") and not link.startswith("mailto:"):
                yield response.follow(link, callback=self.parse)
```

After running the Scrapy spider, you'll have a file containing scraped data (e.g., `example_data.json`). You can analyze these results using standard command-line tools. For instance, to extract all links:

```bash
jq -r '.[] | select(.file != null) | .file' example_data.json | sort -u
```

This command uses `jq` to extract links, `awk` to isolate file extensions, `sort` to order them, and `uniq -c` to count their occurrences. By scrutinizing the extracted data, you can identify patterns, anomalies, or sensitive files that might be of interest for further investigation.

## Search Engine Discovery

Leveraging search engines for reconnaissance involves utilizing their vast indexes of web content to uncover information about your target. This passive technique, often referred to as Open Source Intelligence (OSINT) gathering, can yield valuable insights without directly interacting with the target's systems.

By employing advanced search operators and specialized queries known as "Google Dorks," you can pinpoint specific information buried within search results. Here's a table of some useful search operators for web reconnaissance:

|Operator|Description|Example|
|---|---|---|
|`site:`|Restricts search results to a specific website.|`site:example.com "password reset"`|
|`inurl:`|Searches for a specific term in the URL of a page.|`inurl:admin login`|
|`filetype:`|Limits results to files of a specific type.|`filetype:pdf "confidential report"`|
|`intitle:`|Searches for a term within the title of a page.|`intitle:"index of" /backup`|
|`cache:`|Shows the cached version of a webpage.|`cache:example.com`|
|`"search term"`|Searches for the exact phrase within quotation marks.|`"internal error" site:example.com`|
|`OR`|Combines multiple search terms.|`inurl:admin OR inurl:login`|
|`-`|Excludes specific terms from search results.|`inurl:admin -intext:wordpress`|

By creatively combining these operators and crafting targeted queries, you can uncover sensitive documents, exposed directories, login pages, and other valuable information that may aid in your reconnaissance efforts.

## Web Archives

Web archives are digital repositories that store snapshots of websites across time, providing a historical record of their evolution. Among these archives, the Wayback Machine is the most comprehensive and accessible resource for web reconnaissance.

The Wayback Machine, a project by the Internet Archive, has been archiving the web for over two decades, capturing billions of web pages from across the globe. This massive historical data collection can be an invaluable resource for security researchers and investigators.

|Feature|Description|Use Case in Reconnaissance|
|---|---|---|
|`Historical Snapshots`|View past versions of websites, including pages, content, and design changes.|Identify past website content or functionality that is no longer available.|
|`Hidden Directories`|Explore directories and files that may have been removed or hidden from the current version of the website.|Discover sensitive information or backups that were inadvertently left accessible in previous versions.|
|`Content Changes`|Track changes in website content, including text, images, and links.|Identify patterns in content updates and assess the evolution of a website's security posture.|

By leveraging the Wayback Machine, you can gain a historical perspective on your target's online presence, potentially revealing vulnerabilities that may have been overlooked in the current version of the website.

# Web Fuzzing Cheatsheet

## What is Web Fuzzing?

`Web fuzzing` is a technique used to discover vulnerabilities, hidden resources, and security issues in web applications by automatically injecting a large set of input data into the application and analyzing its response. The goal is to identify unexpected behaviors or errors that could indicate potential security weaknesses or misconfigurations.

Fuzzing is commonly employed in security testing to find:

- Hidden directories and files
- Insecure APIs and endpoints
- SQL injection points
- Cross-site scripting (XSS) vulnerabilities
- Command injection flaws

## Comparison: Brute-Forcing vs. Fuzzing

|`Criteria`|`Brute-Forcing`|`Fuzzing`|
|---|---|---|
|`Definition`|Systematically trying all possible combinations of input data to guess a specific value.|Injecting unexpected or random data into an application to find vulnerabilities and hidden resources.|
|`Purpose`|Crack passwords, keys, or other access credentials.|Discover application vulnerabilities, hidden files, directories, and input validation issues.|
|`Methodology`|Exhaustive search over all possible input combinations.|Dynamic input injection to provoke unexpected application responses.|
|`Focus`|Specific input or data, such as passwords or API keys.|General application behavior under various input conditions.|
|`Efficiency`|Time-consuming due to exhaustive nature; less efficient for large input spaces.|More efficient in identifying unexpected behaviors and vulnerabilities with varied input.|
|`Tools Used`|Password crackers, key recovery tools.|Web fuzzers, vulnerability scanners.|
|`Output`|Successful match of the correct input value.|Discovery of vulnerabilities, misconfigurations, and hidden resources.|

## Miscellaneous Commands

Below are some useful commands that can aid in various tasks related to web fuzzing and testing.

|`Command`|`Description`|
|---|---|
|`sudo sh -c 'echo "SERVER_IP academy.htb" >> /etc/hosts'`|Add a DNS entry for a specific IP address to the `/etc/hosts` file. This helps resolve domain names locally.|
|`for i in $(seq 1 1000); do echo $i >> ids.txt; done`|Create a sequence wordlist from 1 to 1000. Useful for brute-forcing numerical IDs or similar patterns.|
|`curl http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'id=key' -H 'Content-Type: application/x-www-form-urlencoded'`|Use `curl` to send a POST request with specific data and headers, simulating form submissions or API calls.|

## Commonly Used SecLists Wordlists

[SecLists](https://github.com/danielmiessler/SecLists) is a collection of multiple types of wordlists used by security researchers and penetration testers. Below is a table of some commonly used wordlists from SecLists, which can be incredibly valuable during web fuzzing.

|`Wordlist`|`Description`|
|---|---|
|`/usr/share/seclists/Discovery/Web-Content/common.txt`|`General-Purpose Wordlist`: Contains a broad range of common directory and file names on web servers. It's an excellent starting point for fuzzing and often yields valuable results.|
|`/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt`|`Directory-Focused Wordlist`: A more extensive wordlist specifically focused on directory names. It's a good choice when you need a deeper dive into potential directories.|
|`/usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt`|`Large Directory Wordlist`: Boasts a massive collection of directory names compiled from various sources. It's a valuable resource for thorough fuzzing campaigns.|
|`/usr/share/seclists/Discovery/Web-Content/big.txt`|`Comprehensive Wordlist`: A massive wordlist containing both directory and file names. Useful when you want to cast a wide net and explore all possibilities.|

### Tips for Using Wordlists Effectively

|`Tip`|`Explanation`|
|---|---|
|`Choose the Right Wordlist`|Select wordlists relevant to the target environment and technology stack for better results.|
|`Combine Wordlists`|Use multiple wordlists together to increase the breadth of your fuzzing efforts.|
|`Customize Wordlists`|Modify existing wordlists or create your own based on specific knowledge about the target.|
|`Monitor Performance`|Large wordlists can be resource-intensive; monitor performance and adjust as needed.|
|`Leverage Community Resources`|Utilize community-maintained wordlists for the latest and most effective fuzzing strategies.|

## Tools for Web Fuzzing

### ffuf (Fuzz Faster U Fool)

`ffuf` is a fast web fuzzer written in Go that allows you to discover directories and files on web servers.

|`Command`|`Description`|
|---|---|
|`ffuf -u http://example.com/FUZZ`|Basic fuzzing of a URL path.|
|`ffuf -u http://example.com/FUZZ -w wordlist.txt`|Fuzz with a specific wordlist.|
|`ffuf -u http://example.com/FUZZ -w wordlist.txt -ic`|Fuzz with a specific wordlist, automatically ignoring any comments in the wordlist.|
|`ffuf -u http://example.com/FUZZ -w wordlist.txt -c`|Colorize the output for better readability.|
|`ffuf -u http://example.com/FUZZ -w wordlist.txt -mc 200`|Filter results by status code (e.g., 200).|
|`ffuf -u http://example.com/FUZZ -w wordlist.txt -mr "Welcome"`|Filter results by matching a regex pattern.|
|`ffuf -u http://example.com/FUZZ -w wordlist.txt -e .php,.html`|Add extensions to each wordlist entry.|
|`ffuf -u http://example.com/FUZZ -w wordlist.txt -t 50`|Set the number of threads (e.g., 50) for faster fuzzing.|
|`ffuf -u http://example.com/FUZZ -w wordlist.txt -x http://127.0.0.1:8080`|Use a proxy for requests.|

### gobuster

`gobuster` is a tool used to brute-force URIs (directories and files) in web sites and DNS subdomains.

|`Command`|`Description`|
|---|---|
|`gobuster dir -u http://example.com -w wordlist.txt`|Directory fuzzing using a wordlist.|
|`gobuster dir -u http://example.com -w wordlist.txt -x .php,.html`|Fuzz with specific extensions.|
|`gobuster dir -u http://example.com -w wordlist.txt -s 200`|Filter results by status code (e.g., 200).|
|`gobuster dir -u http://example.com -w wordlist.txt -t 50`|Set the number of concurrent threads (e.g., 50).|
|`gobuster dir -u http://example.com -w wordlist.txt -o results.txt`|Output results to a file.|
|`gobuster dns -d example.com -w subdomains.txt`|Fuzz DNS subdomains using a wordlist.|
|`gobuster dns -d example.com -w subdomains.txt -i`|Show IP addresses of discovered subdomains.|
|`gobuster dns -d example.com -w subdomains.txt -z`|Silent mode; suppress output except for results.|

### wenum (Wfuzz Fork)

`wenum` is a fork of `wfuzz`, a versatile web application fuzzer for testing web security.

|`Command`|`Description`|
|---|---|
|`wenum -c -w wordlist.txt --hc 404 -u http://example.com/FUZZ`|Basic fuzzing excluding 404 responses.|
|`wenum -c -w wordlist.txt -d 'username=FUZZ&password=secret' -u http://example.com/login`|Fuzz POST data in a form.|
|`wenum -c -w wordlist.txt -b 'session=12345' -u http://example.com/FUZZ`|Use a specific cookie for requests.|
|`wenum -c -w wordlist.txt -H 'User-Agent: Wenum' -u http://example.com/FUZZ`|Add a custom header to requests.|
|`wenum -c -w wordlist.txt -t 50 -u http://example.com/FUZZ`|Set the number of threads (e.g., 50) for faster fuzzing.|
|`wenum -c -w wordlist.txt -X PUT -u http://example.com/FUZZ`|Fuzz using a specific HTTP method (e.g., PUT).|
|`wenum -c -w wordlist.txt --hs 50 -u http://example.com/FUZZ`|Filter responses by content length (e.g., 50 bytes).|

### feroxbuster

`feroxbuster` is a tool designed for recursive content discovery and web fuzzing.

|`Command`|`Description`|
|---|---|
|`feroxbuster -u http://example.com -w wordlist.txt`|Basic URL fuzzing with a wordlist.|
|`feroxbuster -u http://example.com -w wordlist.txt -x`|Include specified file extensions in fuzzing.|
|`feroxbuster -u http://example.com -w wordlist.txt -C 404`|Exclude responses with status code 404.|
|`feroxbuster -u http://example.com -w wordlist.txt -t 50`|Set the number of concurrent threads (e.g., 50).|
|`feroxbuster -u http://example.com -w wordlist.txt --depth 3`|Set maximum recursion depth (e.g., 3 levels deep).|
|`feroxbuster -u http://example.com -w wordlist.txt -o results.txt`|Save output to a file.|
|`feroxbuster -u http://example.com -w wordlist.txt --no-recursion`|Disable recursion into discovered directories.|
|`feroxbuster -u http://example.com -w wordlist.txt --redirect`|Follow redirects automatically.|

## Tips for Effective Web Fuzzing

|`Tip`|`Explanation`|
|---|---|
|`Use Comprehensive Wordlists`|The quality of your wordlist can significantly impact results; choose or create wordlists relevant to the target.|
|`Filter Unwanted Responses`|Use status codes or response size filtering to focus on meaningful results and reduce noise.|
|`Adjust Thread Count`|Increase thread count for faster fuzzing, but be mindful of server capabilities to avoid overloading.|
|`Monitor Server Responses`|Pay attention to anomalies or unexpected behavior in server responses, indicating potential vulnerabilities.|
|`Fuzz with Various HTTP Methods`|Test different HTTP methods (GET, POST, PUT, DELETE) to uncover potential vulnerabilities in all endpoints.|

## Web APIs: REST, SOAP, and GraphQL

### What is a Web API?

A `Web API` (Application Programming Interface) is a set of rules and protocols for building and interacting with software applications. APIs allow different applications to communicate with each other over the internet, enabling the integration of various services and data exchange.

Web APIs can be categorized into three main types:

1. `REST (Representational State Transfer)`
2. `SOAP (Simple Object Access Protocol)`
3. `GraphQL`

Each type has its own unique characteristics, advantages, and use cases.

### REST (Representational State Transfer)

`REST` is an architectural style that uses standard HTTP methods to access and manipulate resources on a server. It is known for its simplicity, scalability, and statelessness.

|`Feature`|`Description`|
|---|---|
|`Protocol`|Uses HTTP/HTTPS.|
|`Data Format`|Typically JSON, but can also use XML, HTML, or plain text.|
|`Stateless`|Each request from a client to a server must contain all the information needed.|
|`CRUD Operations`|Uses HTTP methods: GET, POST, PUT, DELETE.|
|`Scalability`|Highly scalable due to its stateless nature.|
|`Caching`|Supports caching mechanisms to improve performance.|
|`URL Structure`|Uses endpoints that represent resources, e.g., `/api/users/{id}`.|
|`Advantages`|Simplicity, flexibility, scalability.|
|`Disadvantages`|Can lead to over-fetching or under-fetching data.|

`REST Fuzzing Tips:`

|`Tip`|`Explanation`|
|---|---|
|`Test All HTTP Methods`|Ensure all CRUD operations are tested, as vulnerabilities might exist in any of them.|
|`Validate Input Fields`|Fuzz input fields with unexpected data types and formats to uncover validation issues.|
|`Examine Error Messages`|Analyze error messages for information disclosure or unintended behavior.|
|`Test Authentication Mechanisms`|Check for improper authentication and authorization controls.|
|`Explore API Rate Limits`|Test rate limits and throttling controls to ensure the API handles requests properly.|
|`Use Comprehensive Payloads`|Leverage a variety of payloads (SQLi, XSS) to test for potential security flaws.|
|`Check Resource Representation`|Test different resource representations (JSON, XML) for consistency and security flaws.|

### SOAP (Simple Object Access Protocol)

`SOAP` is a protocol for exchanging structured information in web services. It uses XML as its message format and can operate over various protocols like HTTP, SMTP, or TCP.

|`Feature`|`Description`|
|---|---|
|`Protocol`|Protocol-independent but often used with HTTP/HTTPS.|
|`Data Format`|Exclusively XML.|
|`Stateful/Stateless`|Can be either stateful or stateless.|
|`WS-Security`|Built-in security features for message integrity and confidentiality.|
|`Error Handling`|Uses specific error codes and messages.|
|`Complexity`|More complex due to extensive standards and specifications.|
|`Extensibility`|Highly extensible via WS-* standards.|
|`Advantages`|Strong security, reliability, and extensibility.|
|`Disadvantages`|More complex and less flexible compared to REST.|

`SOAP Fuzzing Tips:`

|`Tip`|`Explanation`|
|---|---|
|`Analyze WSDL Files`|Use WSDL (Web Services Description Language) files to understand the service's operations and inputs.|
|`Validate XML Schema`|Test XML inputs against the schema to identify validation flaws.|
|`Check for XML Injection`|Fuzz XML data to test for injection vulnerabilities.|
|`Test SOAP Headers`|Fuzz SOAP headers to find potential security issues or misconfigurations.|
|`Evaluate WS-Security Implementations`|Ensure security implementations are robust and correctly configured.|
|`Test Transport Security`|Verify that transport-level security (e.g., HTTPS) is enforced and properly implemented.|
|`Examine SOAP Faults`|Analyze SOAP fault messages for potential information leakage.|

### GraphQL

`GraphQL` is a query language and runtime for APIs that allows clients to request specific data and define the structure of the response.

|`Feature`|`Description`|
|---|---|
|`Protocol`|Uses HTTP/HTTPS, typically over POST requests.|
|`Data Format`|JSON-based queries and responses.|
|`Stateful/Stateless`|Stateless architecture.|
|`Query Flexibility`|Clients can request exactly what they need, minimizing over-fetching and under-fetching.|
|`Single Endpoint`|Typically uses a single endpoint for all operations.|
|`Introspection`|Allows clients to query the API schema for available operations and data types.|
|`Advantages`|Efficiency, flexibility, and powerful developer tooling.|
|`Disadvantages`|Potential for complex queries leading to performance issues if not properly managed.|

`GraphQL Fuzzing Tips:`

| `Tip`                                 | `Explanation`                                                                                        |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `Test Query Depth and Complexity`     | Evaluate the server's handling of deeply nested or complex queries to avoid performance bottlenecks. |
| `Validate Input Types and Arguments`  | Fuzz input arguments with unexpected values and data types to uncover validation flaws.              |
| `Examine Query Aliasing and Batching` | Test the server's response to aliased queries and batching for potential information leakage.        |
| `Check for Introspection Misuse`      | Ensure introspection is not exposing sensitive information or internal schema details.               |
| `Assess Authorization Controls`       | Verify that access controls are properly enforced for different queries and operations.              |
| `Evaluate Rate Limiting`              | Test rate limits to ensure the API can handle excessive or malicious requests appropriately.         |
| `Fuzz Mutations`                      | Mutations can alter data; test for security issues and improper input validation.                    |