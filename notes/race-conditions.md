# Race Conditions

Race conditions occur when an application processes concurrent requests in a way that leads to unintended behavior. These are sometimes called "time-of-check to time-of-use" (TOCTOU) vulnerabilities. Exploitable when operations that should be atomic (e.g., checking a balance and deducting it) can be interleaved by parallel requests.

## Checks

- [ ] Identify state-changing operations that should be atomic (balance transfers, coupon redemption, voting, etc.)
- [ ] Check for limit bypasses — can you exceed a limit by sending parallel requests?
- [ ] Test single-use tokens/codes — can they be reused if submitted simultaneously?
- [ ] Test for duplicate actions (double-spending, double-registration, etc.)
- [ ] Check multi-step processes — can you skip or repeat steps by racing?
- [ ] Look for operations that read-then-write without locking

## Burp Suite (Turbo Intruder / Single-Packet Attack)

PortSwigger's "single-packet attack" sends multiple requests in a single TCP packet to minimize network jitter and maximize timing precision.

> [!tip] In Burp Suite, use the **Send group in parallel (single-packet attack)** option in Repeater by selecting multiple tabs and sending them together.

## Command-Line Testing

### PowerShell

```powershell
1..50 | ForEach-Object -Parallel { try { $resp = (Invoke-WebRequest -Method POST `-Uri "<your lab>"` -Headers @{ "Content-Type" = "application/json"; "Authorization" = "Bearer <your token" } ` -Body '{"from_currency":"USD","to_currency":"EUR","amount":50}' ).Content | ConvertFrom-Json if ($resp.flag) { "FLAG FOUND: $($resp.flag)" } } catch {} } -ThrottleLimit 50
```

### Bash

```shell
seq 50 | xargs -I{} -P 50 curl -k -x http://127.0.0.1:8080 -X POST \
    -H 'Content-Type:application/json' \
    -H 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwidXNlcm5hbWUiOiJ0ZXN0ZXIxIiwicm9sZSI6InVzZXIiLCJpYXQiOjE3NzE1OTYzNTN9.-pvatNd0QsCWiABxW6b52FTiSlkUDS7G0Jf_vcYROrU' \
    -H 'X-PwnFox-Color:magenta' \
    -H 'Priority:u=0' \
    -d '{
  "from_currency": "USD",
  "to_currency": "EUR",
  "amount": 10
}' \
    'https://lab-1771596331957-t6ucr7.labs-app.bugforge.io/api/convert-currency'
```

## Common Targets

| Scenario                  | What to Test                                                       |
| ------------------------- | ------------------------------------------------------------------ |
| Coupon/promo code         | Apply the same code in parallel — does it get applied twice?       |
| Balance transfer          | Send multiple transfer requests simultaneously                     |
| Vote/like system          | Can you vote multiple times with concurrent requests?              |
| Invite/registration limit | Can you exceed the invite limit by racing?                         |
| File upload + processing  | Upload and access the file before server-side validation completes |
| MFA/OTP verification      | Brute force OTP with parallel requests if no rate limit            |

---

## References

- [PortSwigger - Race Conditions](https://portswigger.net/web-security/race-conditions)
- [PortSwigger Research - Smashing the State Machine](https://portswigger.net/research/smashing-the-state-machine)
- [HackTricks - Race Conditions](https://book.hacktricks.wiki/en/pentesting-web/race-condition.html)
