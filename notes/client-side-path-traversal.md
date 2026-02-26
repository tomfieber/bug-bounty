# Client-Side Path Traversal (CSPT)

## Checks

- [ ] Check the network tab for requests to API endpoints
- [ ] Carefully review the client-side code and AJAX requests to identify other endpoints that may be useful
- [ ] Check to see what other methods are being used with endpoints
- [ ] Check for chains with other vulns --
  - [ ] Is anything reflected on other endpoints? Try [xss](xss.md)
  - [ ] Combine with CSRF — if a path-traversed request performs a state change
  - [ ] Combine with SSRF — if the client sends the traversed path to the server
- [ ] Try dot-dot-slash (`../`) in path segments of AJAX/fetch URLs
- [ ] Check if client-side routing uses URL path segments directly in API calls
- [ ] Look for patterns like `fetch('/api/resource/' + userInput)` where userInput isn't sanitized

## Example

If the frontend makes a request like:

```javascript
fetch("/api/users/" + userId + "/profile");
```

And `userId` is controllable (e.g., from the URL), try:

```
../../admin/settings
```

Resulting in:

```
/api/users/../../admin/settings/profile → /admin/settings/profile
```

---

## References

- [Client-Side Path Traversal - Maxence Schmitt](https://blog.doyensec.com/2024/10/02/cspt-practical-attacks.html)
- [PortSwigger Research - Path Traversal in Client-Side Contexts](https://portswigger.net/research/client-side-path-traversal)
