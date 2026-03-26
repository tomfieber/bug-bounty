# OAuth / OpenID Connect

## Checks

- [ ] Check `redirect_uri` for flawed validation
  - Try path traversal: `https://allowed.com/../attacker.com`
  - Try subdomain: `https://evil.allowed.com`
  - Try appending: `https://allowed.com.evil.com`
  - Try parameter pollution: `redirect_uri=https://allowed.com&redirect_uri=https://evil.com`
  - Try localhost variations: `redirect_uri=http://127.0.0.1`
  - Try different schemes: `redirect_uri=javascript://allowed.com%0aalert(1)`
- [ ] Check if there is a `state` parameter (CSRF protection)
  - If missing, try forging authorization requests
  - If present, check if it's validated server-side
  - Check if the state is predictable or reusable
- [ ] Check if authorization codes are single-use
  - Try replaying an authorization code
- [ ] Check if tokens are leaked in the Referer header
  - Look at where the redirect goes — any external resources loaded?
- [ ] Check the token type — `response_type=code` vs `response_type=token`
  - Implicit flow (`token`) is more dangerous; token exposed in URL fragment
- [ ] Check scope escalation - can we request additional scopes?
- [ ] Check if the `client_secret` is exposed in client-side code
- [ ] Look for open redirects to chain with OAuth redirect_uri
- [ ] Try changing `response_type` from `code` to `token` (force implicit flow)
- [ ] Check if tokens/codes are bound to the correct client_id

## Authorization Code Flow

```
1. User -> App: Click "Login with OAuth"
2. App -> Auth Server: GET /authorize?client_id=X&redirect_uri=Y&response_type=code&scope=Z&state=S
3. User authenticates with Auth Server
4. Auth Server -> App: Redirect to Y?code=AUTH_CODE&state=S
5. App -> Auth Server: POST /token (code + client_secret)
6. Auth Server -> App: Access Token
```

## Common Attack Scenarios

### Stealing Authorization Code via [Open Redirect](open-redirects.md)

If you find an open redirect on the allowed domain, chain it:

```
/authorize?client_id=X&redirect_uri=https://allowed.com/redirect?url=https://evil.com&response_type=code
```

### Missing State Parameter ([CSRF](csrf.md))

Force a victim to link their account with the attacker's OAuth account:

```html
<img src="https://target.com/oauth/callback?code=ATTACKER_AUTH_CODE" />
```

### Token Leakage via Referer

If the callback page loads external resources (images, scripts), the token in the URL fragment or query string may leak via the `Referer` header.

---

## References

- [PortSwigger - OAuth](https://portswigger.net/web-security/oauth)
- [PayloadsAllTheThings - OAuth](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/OAuth%20Misconfiguration)
