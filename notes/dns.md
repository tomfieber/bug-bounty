# DNS

The Domain Name System (DNS) functions as the internet's GPS, translating user-friendly domain names into the numerical IP addresses computers use to communicate.

## Checks

- [ ] Run `whois` lookup on the target domain
- [ ] Query all record types: A, AAAA, CNAME, MX, NS, TXT, SOA
- [ ] Attempt a zone transfer (`dig axfr @nameserver target.com`)
- [ ] Check for subdomain enumeration via DNS brute force
- [ ] Look for interesting TXT records (SPF, DKIM, verification tokens, internal info)
- [ ] Check for dangling CNAME records (subdomain takeover)
- [ ] Look up reverse DNS for discovered IP addresses

## Quick Reference

The `dig` command allows you to query DNS servers directly, retrieving specific information about domain names. For instance, if you want to find the IP address associated with `example.com`, you can execute the following command:

```bash
dig example.com A
```

## DNS Record Types

| Record Type | Description                                                           |
| ----------- | --------------------------------------------------------------------- |
| A           | Maps a hostname to an IPv4 address.                                   |
| AAAA        | Maps a hostname to an IPv6 address.                                   |
| CNAME       | Creates an alias for a hostname, pointing it to another hostname.     |
| MX          | Specifies mail servers responsible for handling email for the domain. |
| NS          | Delegates a DNS zone to a specific authoritative name server.         |
| TXT         | Stores arbitrary text information.                                    |
| SOA         | Contains administrative information about a DNS zone.                 |

## Useful Commands

```bash
# Standard lookup
dig example.com A
dig example.com ANY

# Query specific nameserver
dig @ns1.example.com example.com

# Zone transfer attempt
dig axfr @ns1.example.com example.com

# Reverse DNS
dig -x 93.184.216.34

# Short output
dig +short example.com

# Trace the full resolution path
dig +trace example.com
```

---

## References

- [HackTricks - DNS Enumeration](https://book.hacktricks.wiki/en/network-services-pentesting/pentesting-dns.html)
