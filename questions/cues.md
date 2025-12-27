# Login page

- [ ] Does the app allow self-registration
	- [ ] Two accounts with the same name
	- [ ] Unicode normalization issues?
- [ ] Check for weak credentials
- [ ] Check for default credentials
- [ ] Check for rate limiting
- [ ] Check for account lockout
- [ ] Test for [SQLi](../notes/SQLi.md)
- [ ] Check for username enumeration
	- [ ] Error messages
	- [ ] Timing disparity
	- [ ] Content-length
	- [ ] Try with a very long password
- [ ] Is there MFA
	- [ ] Can it be bypassed?
	- [ ] Brute forced if no rate limiting?
	- [ ] How are MFA tokens handled?
		- [ ] Do they expire?
		- [ ] Can they be used more than once?
	- [ ] Navigate directly to authenticated functionality
- [ ] Forgot password functionality?
	- [ ] How is it handled?
	- [ ] Current password required?
	- [ ] Can we change where email goes?
- [ ] Is it using SAML/OAUTH?
- [ ] Check for issues in client-side JS
- [ ] Can we bypass auth with IP spoofing?

# Registration

- [ ] Can anyone register? 
- [ ] What is required for registration?
- [ ] Check for mass assignment
- [ ] Check for unicode normalization issues
- [ ] Registration via API endpoints

# User input

- [ ] Is the input reflected anywhere on the page?
	- [ ] What is the context?
- [ ] Check for XSS
- [ ] Check for SQLi
- [ ] Check for SSTI
- [ ] What is the content-type of the request?
	- [ ] Check for XXE
	- [ ] Try converting JSON to XML


