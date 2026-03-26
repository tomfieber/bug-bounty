# Open Redirects

Lack of server-side validation to ensure that redirect URLs are legitimate

## Checks

- [ ] Try to add a domain we control in any redirect parameter, url=, redirect=, redirect_url=, etc.
- [ ] Check for misconfigured filtering.
  - google.com.demo instead of [google.com](http://google.com/)
- [ ] Try // instead of https://

## SSO

If there is an open redirect somewhere on the site, we might be able to abuse that in the context of an SSO login.

Example:

```
https://auth.barite.ctfio.com/auth?client_id=1&redirect_url=https://barite.ctfio.com/redirect?url=https://tomfieber.github.io&response_type=token
```

Note that the open redirect occurs within one functionality on the site:

`https://barite.ctfio.com/redirect?url=https://www.google.com`

But if we plug that into the `redirect_url` parameter of the SSO auth request, then we can control where the user is redirected after logging in.

## Bypasses

- [ ] Check misconfigured regex
  - `target.net/x//hacker.com`
- [ ] Try using an `@` symbol in the domain name
  - `https://auth.bismuth.ctfio.com/auth?client_id=1&redirect_url=https://bismuth.ctfio.com@tomfieber.github.io/&response_type=token`

---

## References

- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Open%20Redirect)
- [HackTricks](https://angelica.gitbook.io/hacktricks/pentesting-web/open-redirect)
- [AppSecExplained](https://appsecexplained.gitbook.io/appsecexplained/common-vulns/open-redirect)
- [PortSwigger URL Validation Bypass Cheatsheet](https://portswigger.net/web-security/ssrf/url-validation-bypass-cheat-sheet)
