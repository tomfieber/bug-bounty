Want to wipe the slate clean and start over? You can!

```console
hacker@dojo:~$ ls /
bin etc blah blah blah
hacker@dojo:~$ rm -rf /
hacker@dojo:~$ ls /
bash: ls: command not found
hacker@dojo:~$
```

What happened here? As you recall, `rm` removes files. The `-r` (recursive) flag removes directories and all files containing them. The `-f` (force) flag ignores any errors the `rm` command runs into or compulsions that it may have. Combined and aimed at `/`, the results are catastrophic: a full wipe of your system. On a modern system, things aren't _that_ simple, but you'll figure that out when you see it.

In this challenge, you will do something that you might never do again: wipe the whole system. We've actually modified things a bit to keep your home directory safe (normally, it would get wiped as well!), but otherwise, all that stands before you and the flag is your willingness to wipe the drive. But before you wipe it all, make sure to start `/challenge/check` so that it can watch the fireworks (and give you the flag)!

>[!warning]
>Don't ever actually do this.

---
![](../../../attachments/pwn-college/01-linux-luminarium/16-daring-destruction/003-rm-rf.md/Pasted%20image%2020250924092221.png)

![](../../../attachments/pwn-college/01-linux-luminarium/16-daring-destruction/003-rm-rf.md/Pasted%20image%2020250924092238.png)

