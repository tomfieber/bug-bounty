# API Testing

## Recon

### Passive API recon

Perform recon without touching the target.

### Google dorking

```
# Basic

$target api
$target docs
$target developers
$target graphql

# intitle
intitle:"api" site:target.com

# inurl
inurl:"/api/v1" site:target.com
inurl:"/api/v2/" site:target.com
```

### GitHub

Check github for leaked secrets

### Finding API Documentation

- [ ] Check for common documentation paths:

```
/api
/api/docs
/api/swagger
/api/swagger-ui.html
/api/v1/docs
/swagger.json
/openapi.json
/api-docs
/graphql
/graphiql
/altair
/playground
```

- [ ] Check Wayback Machine for old/removed API docs
- [ ] Look for Postman collections shared publicly

## Active Testing

### Authentication & Authorization

- [ ] Test endpoints with no auth token
- [ ] Test with expired tokens
- [ ] Test with tokens from a different user (horizontal privilege escalation)
- [ ] Test with a low-privilege token on admin endpoints (vertical privilege escalation)
- [ ] Check if API keys are in the URL (leaked via logs/Referer)

### HTTP Method Testing

- [ ] Try all methods on each endpoint (GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD)
- [ ] Check if `PUT`/`DELETE` are allowed where they shouldn't be

### Input Validation

- [ ] Test with unexpected data types (strings where ints expected, arrays where strings expected)
- [ ] Send oversized payloads
- [ ] Test with special characters and encoding
- [ ] Check for mass assignment — send additional properties in POST/PUT requests

```json
{ "username": "user", "role": "admin" }
```

### Rate Limiting

- [ ] Check if rate limiting exists on sensitive endpoints (login, password reset, OTP)
- [ ] Try bypassing with `X-Forwarded-For` header rotation

### Information Disclosure

- [ ] Check verbose error messages
- [ ] Check for stack traces in responses
- [ ] Look for internal IPs, paths, or debug info in responses
- [ ] Test `Accept` header variations (`application/xml`, `text/html`)

### GraphQL-Specific

- [ ] Test for introspection:

```json
{ "query": "{__schema{types{name,fields{name}}}}" }
```

- [ ] Check for disabled introspection bypass with newline:

```json
{ "query": "\n{__schema{types{name,fields{name}}}}" }
```

- [ ] Look for query batching for brute force
- [ ] Test for excessive depth/complexity (DoS)

---

## References

- [OWASP API Security Top 10](https://owasp.org/API-Security/)
- [PortSwigger - API Testing](https://portswigger.net/web-security/api-testing)
