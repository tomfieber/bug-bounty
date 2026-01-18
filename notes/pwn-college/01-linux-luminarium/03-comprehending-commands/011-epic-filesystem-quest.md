In this challenge, I have _hidden the flag_! Here, you will use `ls` and `cat` to follow my breadcrumbs and find it! Here's how it'll work:

0. Your first clue is in `/`. Head on over there.
1. Look around with `ls`. There'll be a file named HINT or CLUE or something along those lines!
2. `cat` that file to read the clue!
3. Depending on what the clue says, head on over to the next directory (or don't!).
4. Follow the clues to the flag!

Good luck!

The first clue is in `DISPATCH`

![](../../../attachments/pwn-college/01-linux-luminarium/03-comprehending-commands/011-epic-filesystem-quest.md/Pasted%20image%2020250916134152.png)

Checking the directory shows a `.SPOILER` file

![](../../../attachments/pwn-college/01-linux-luminarium/03-comprehending-commands/011-epic-filesystem-quest.md/Pasted%20image%2020250916134549.png)

Following the instructions in `.SPOILER`

![](../../../attachments/pwn-college/01-linux-luminarium/03-comprehending-commands/011-epic-filesystem-quest.md/Pasted%20image%2020250916134635.png)

There are a lot of files in that directory, but there's one particular one named `.INSIGHT`

![](../../../attachments/pwn-college/01-linux-luminarium/03-comprehending-commands/011-epic-filesystem-quest.md/Pasted%20image%2020250916135053.png)

There's a `HINT` file in /etc/vulkan

![](../../../attachments/pwn-college/01-linux-luminarium/03-comprehending-commands/011-epic-filesystem-quest.md/Pasted%20image%2020250916135223.png)

Following those instructions we get the following:

![](../../../attachments/pwn-college/01-linux-luminarium/03-comprehending-commands/011-epic-filesystem-quest.md/Pasted%20image%2020250916135403.png)

Looking in the prescribed directory, we see a `.README` file that seems interesting:

The next cue is also trapped:

![](../../../attachments/pwn-college/01-linux-luminarium/03-comprehending-commands/011-epic-filesystem-quest.md/Pasted%20image%2020250916135717.png)

![](../../../attachments/pwn-college/01-linux-luminarium/03-comprehending-commands/011-epic-filesystem-quest.md/Pasted%20image%2020250916135837.png)

