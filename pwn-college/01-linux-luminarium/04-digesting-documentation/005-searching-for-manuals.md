  
This level is tricky: it hides the manpage for the challenge by randomizing its name. Luckily, all of the manpages are gathered in a searchable database, so you'll be able to search the man page database to find the hidden challenge man page! To figure out how to search for the right manpage, read the `man` page manpage by doing: `man man`!

**HINT 1:** `man man` teaches you advanced usage of the `man` command itself, and you must use this knowledge to figure out how to search for the hidden manpage that will tell you how to use `/challenge/challenge`

**HINT 2:** though the manpage is randomly named, you still actually use `/challenge/challenge` to get the flag!

```bash
# Check for manuals using regex
man -k challenge
```

![](../../../attachments/pwn-college/01-linux-luminarium/04-digesting-documentation/005-searching-for-manuals.md/Pasted%20image%2020250916163318.png)

![](../../../attachments/pwn-college/01-linux-luminarium/04-digesting-documentation/005-searching-for-manuals.md/Pasted%20image%2020250916163353.png)

```bash
/challenge/challenge --iwjonh 449
```

