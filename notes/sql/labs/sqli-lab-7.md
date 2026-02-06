# SQL injection UNION attack, determining the number of columns returned by the query

1. Send a single quote and observe the error
2. Use `ORDER BY` to find the number of columns

![[attachments/sqli-lab-7/file-20260206135416506.png]]

![[attachments/sqli-lab-7/file-20260206135416510.png]]

3. Note that 4 fails while 3 succeeds. The original query returns 3 columns. 
4. 