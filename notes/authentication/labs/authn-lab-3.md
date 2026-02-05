---
tags:
  - authn
  - timing
---
# Username enumeration via response timing

1. Log in with our own credentials and note the response time (~567ms)
2. Send a valid username (wiener) with a very long, incorrect password and observe the response time (~5359ms)
3. Note that we get an error about making too many requests. "You have made too many incorrect login attempts. Please try again in 30 minute(s)."
4. Set an `X-Forwarded-For` header and set a placeholder at the last octet
5. Run the attack again with the usernames and a long password. 

![[attachments/authn-lab-3/file-20260204183114322.png]]

6. Run the same attack with a placeholder on the password field and look for the 302 response

![[attachments/authn-lab-3/file-20260204183517332.png]]

7. Log in as the discovered user to solve the lab



