Armed with your knowledge, you can now carry out some shenanigans. This challenge is almost the same as the first challenge in this module. Again, this challenge will delete the flag using the `rm` command. But unlike before, it will _not_ print anything out for you.

How can you solve this? You know that `rm` is searched for in the directories listed in the `PATH` variable. You have experience creating the `win` command when the previous challenge needed it. What else can you create?

Create a "malicious" `rm` command

```bash
#!/bin/bash
cat /flag
```

Then set the path

```bash
PATH="$(pwd):$PATH" /challenge/run
```

![](../../../attachments/pwn-college/01-linux-luminarium/14-pondering-path/005-hijacking-commands.md/Pasted%20image%2020250924065042.png)

