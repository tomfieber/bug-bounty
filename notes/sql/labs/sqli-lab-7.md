# SQL injection UNION attack, determining the number of columns returned by the query

1. Send a single quote and observe the error
2. Use `ORDER BY` to find the number of columns

![[attachments/sqli-lab-7/file-20260204105624252.png]]

![[attachments/sqli-lab-7/file-20260204105640354.png]]

3. Note that 4 fails while 3 succeeds. The original query returns 3 columns. 
4. 