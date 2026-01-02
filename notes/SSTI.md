# SSTI Testing Methodology

## Universal polyglot

```
${{\<\%\[%'"}}%\\
```

## Testing Methodology

- [ ] **Detect SSTI** Use basic mathematical expressions (`{{7*7}}`, `${7*7}`, `@(7*7)`) to confirm template processing.
- [ ] **Fingerprint Engine** Apply type coercion tests (`{{7*'7'}}`) to identify the specific engine and underlying language.
- [ ] **Craft Engine-Specific Exploit** Use the appropriate RCE payload for the identified engine.
- [ ] **Handle Blind Scenarios** If output isn't visible, employ time-based or OOB techniques.
- [ ] **Bypass Filters** When basic payloads are blocked, use character encoding, alternative syntax, or creative exploitation techniques.

## Where to look for SSTI

If user input is shown in any of the following, test for SSTI

- [ ] PDF and document generators
- [ ] Email templates
- [ ] Error messages
- [ ] API response formatting
- [ ] Admin interfaces
	- [ ] Dashboard widget configs
	- [ ] Report builders
	- [ ] Notification template editors
	- [ ] Custom email/SMS template systems
- [ ] Logging systems that format log messages
- [ ] Chat or message systems
- [ ] Calendar event description
- [ ] Ticket or issue tracking system
- [ ] CRM custom field rendering



