## Broken Access Control/IDOR

- [ ] Understand the context of the app
- [ ] Read all client-side JS; check for:
	- [ ] Passwords, credentials, secrets
	- [ ] API keys
	- [ ] Paths, URIs, API structure
	- [ ] Object identifiers
- [ ] Find the JSON/API endpoints (not the rendered HTML)
- [ ] Create a list of interesting object IDs
	- [ ] Request params
	- [ ] Response params
	- [ ] URI path params
	- [ ] Headers
- [ ] Try quiet tweaks first: trailing slash, double slash, subpaths, query params.
- [ ] Test version downgrades - old APIs are gold.
- [ ] Try type/format tricks: strings, leading zeros, hex.
- [ ] Try encoding tricks: `%00`, `%20`, control chars.
- [ ] Combine tricks when single tests fail.
	- [ ] Downgrade + encoded char + path tweak
	- [ ] Try something like `/api/v2/users/5%20/`
- [ ] Log request + response (status + body snippet) - that becomes your PoC.
- [ ] If UUIDs are used, check if they're leaked in other parts of the app or online (e.g., GitHub, etc.)

### Trailing slashes

```
/api/v3/users/5/
```

### Double slashes

```
/api/v3//users//5
```

### Version downgrade

If the original request is using `v3` try downgrading to `v2`

```
/api/v3/users/5
/api/v2/users/5
```

### Subpath/Endpoint variations

Try adding other endpoints like `/profile` `/account`, `/details`, etc.

### Try adding additional users

```
/api/v3/users?id=5,6
```

### Query vs. Param

```
/api/v3/users/5
/api/v3/users?id=5
```

### Type confusion

Check if there are differences in the parsing engine

```
/api/v3/users/5
/api/v3/users/"5"
/api/v3/users/abc5
```

### Leading zeros / Hex / other formats

Check if different numeric formats bypass the 403

```
/api/v3/users/025
/api/v3/users/0x19
```

### NULL / termination / control characters

Check to see if control characters can bypass checks

```
/api/v3/users/5%00
```

### Header / proxy-based bypass

```
GET /api/v3/users/5
Host: target 
X-Original-URL: /api/v3/users/4
```

### Unicode  / encoded space

```
/api/v3/users/5
/api/v3/users/5%20
```

