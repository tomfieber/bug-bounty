# Host header checks

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