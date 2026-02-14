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
