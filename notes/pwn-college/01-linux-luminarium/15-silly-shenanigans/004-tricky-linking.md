Okay, Zardus has wised up! No more sharing the home directory: despite the reduced convenience, Zardus has moved to sharing `/tmp/collab`. He's made that directory world-readable and has started a list of evil commands to remember!

```console
zardus@dojo:~$ mkdir /tmp/collab
zardus@dojo:~$ chmod a+w /tmp/collab
zardus@dojo:~$ echo "rm -rf /" > /tmp/collab/evil-commands.txt
```

In this challenge, when you run `/challenge/victim`, Zardus will add `cat /flag` to that list of commands:

```console
hacker@dojo:~$ /challenge/victim

Username: zardus
Password: **********
zardus@dojo:~$ echo "cat /flag" >> /tmp/collab/evil-commands.txt
zardus@dojo:~$ exit
logout

hacker@dojo:~$
```

Recall from the previous level that, having write access to `/tmp/collab`, the `hacker` user can replace that `evil-commands.txt` file. Also remember from [Comprehending Commands](https://pwn.college/linux-luminarium/commands) that files can _link_ to other files. What happens if `hacker` replaces `evil-commands.txt` with a symbolic link to some sensitive file that `zardus` can write to? Chaos and shenanigans!

You _know_ the file to link to. Pull off the attack, and get `/flag` (which, for this level, Zardus can read again!).

---
Link to zardus' .bashrc file

Be sure to remove the existing file first or the link will fail. 

![](../../../attachments/pwn-college/01-linux-luminarium/15-silly-shenanigans/004-tricky-linking.md/Pasted%20image%2020250924075044.png)

