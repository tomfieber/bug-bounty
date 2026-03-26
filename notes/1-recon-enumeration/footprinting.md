# Footprinting

> See also: [Attacking Common Services](attacking-common-services.md) for offensive techniques against these services.

## Infrastructure-based Enumeration

Certificate transparency.

```
curl -s https://crt.sh/\?q\=<target-domain>\&output\=json | jq .
```

Scan each IP address in a list using Shodan.

```
for i in $(cat ip-addresses.txt);do shodan host $i;done
```

---

## Host-based Enumeration

##### FTP

Interact with the FTP service on the target.

```
ftp <FQDN/IP>
```

Interact with the FTP service on the target.

```
nc -nv <FQDN/IP> 21
```

Interact with the FTP service on the target.

```
telnet <FQDN/IP> 21
```

Interact with the FTP service on the target using encrypted connection.

```
openssl s_client -connect <FQDN/IP>:21 -starttls ftp
```

Download all available files on the target FTP server.

```
wget -m --no-passive ftp://anonymous:anonymous@<target>
```

##### SMB

Null session authentication on SMB.

```
smbclient -N -L //<FQDN/IP>
```

Connect to a specific SMB share.

```
smbclient //<FQDN/IP>/<share>
```

Interaction with the target using RPC.

```
rpcclient -U "" <FQDN/IP>
```

Username enumeration using Impacket scripts.

```
samrdump.py <FQDN/IP>
```

Enumerating SMB shares.

```
smbmap -H <FQDN/IP>
```

Enumerating SMB shares using null session authentication.

```
crackmapexec smb <FQDN/IP> --shares -u '' -p ''
```

SMB enumeration using enum4linux.

```
enum4linux-ng.py <FQDN/IP> -A
```

##### NFS

Show available NFS shares.

```
showmount -e <FQDN/IP>
```

Mount the specific NFS share to ./target-NFS

```
mount -t nfs <FQDN/IP>:/<share> ./target-NFS/ -o nolock
```

Unmount the specific NFS share.

```
umount ./target-NFS
```

##### DNS

NS request to the specific nameserver.

```
dig ns <domain.tld> @<nameserver>
```

ANY request to the specific nameserver.

```
dig any <domain.tld> @<nameserver>
```

AXFR request to the specific nameserver.

```
dig axfr <domain.tld> @<nameserver>
```

Subdomain brute forcing.

```
dnsenum --dnsserver <nameserver> --enum -p 0 -s 0 -o found_subdomains.txt -f ~/subdomains.list <domain.tld>
```

##### SMTP

Connect to the SMTP service on the target.

```
telnet <FQDN/IP> 25
```

##### IMAP/POP3

Log in to the IMAPS service using cURL.

```
curl -k 'imaps://<FQDN/IP>' --user <user>:<password>
```

Connect to the IMAPS service.

```
openssl s_client -connect <FQDN/IP>:imaps
```

Connect to the POP3s service.

```
openssl s_client -connect <FQDN/IP>:pop3s
```

##### SNMP

Querying OIDs using snmpwalk.

```
snmpwalk -v2c -c <community string> <FQDN/IP>
```

Bruteforcing community strings of the SNMP service.

```
onesixtyone -c community-strings.list <FQDN/IP>
```

Bruteforcing SNMP service OIDs.

```
braa <community string>@<FQDN/IP>:.1.*
```

##### MySQL

Login to the MySQL server.

```
mysql -u <user> -p<password> -h <FQDN/IP>
```

##### MSSQL

Log in to the MSSQL server using Windows authentication.

```
mssqlclient.py <user>@<FQDN/IP> -windows-auth
```

##### IPMI

IPMI version detection.

```
msf6 auxiliary(scanner/ipmi/ipmi_version)
```

Dump IPMI hashes.

```
msf6 auxiliary(scanner/ipmi/ipmi_dumphashes)
```

##### Linux Remote Management

Remote security audit against the target SSH service.

```
ssh-audit.py <FQDN/IP>
```

Log in to the SSH server using the SSH client.

```
ssh <user>@<FQDN/IP>
```

Log in to the SSH server using private key.

```
ssh -i private.key <user>@<FQDN/IP>
```

Enforce password-based authentication.

```
ssh <user>@<FQDN/IP> -o PreferredAuthentications=password
```

##### Windows Remote Management

Check the security settings of the RDP service.

```
rdp-sec-check.pl <FQDN/IP>
```

Log in to the RDP server from Linux.

```
xfreerdp /u:<user> /p:"<password>" /v:<FQDN/IP>
```

Log in to the WinRM server.

```
evil-winrm -i <FQDN/IP> -u <user> -p <password>
```

Execute command using the WMI service.

```
wmiexec.py <user>:"<password>"@<FQDN/IP> "<system command>"
```

##### Oracle TNS

Perform a variety of scans to gather information about the Oracle database services and its components.

```
./odat.py all -s <FQDN/IP>
```

Log in to the Oracle database.

```
sqlplus <user>/<pass>@<FQDN/IP>/<db>
```

Upload a file with Oracle RDBMS.

```
./odat.py utlfile -s <FQDN/IP> -d <db> -U <user> -P <pass> --sysdba --putFile C:\\insert\\path file.txt ./file.txt
```
