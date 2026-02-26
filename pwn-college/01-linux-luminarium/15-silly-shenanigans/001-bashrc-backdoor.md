When your shell starts up, it looks for `.bashrc` file in your home directory and executes it as a _startup script_. You can customize your `/home/hacker/.bashrc` with useful things, such as setting environment variables, tweaking your shell configuration, and so on.

You can _also_ use it for _evil_! An unwitting victim's `.bashrc` is a common target for shenanigans. Imagine sneaking onto your friend's computer and adding a `echo "Hackers were here!"` at the end of their `.bashrc`. That's funny, but the same capability can be used for much more nefarious purposes. Malicious software, for example, often targets startup scripts such as `.bashrc` to maintain persistence into the future!

In this challenge, we'll pretend that you've broken into a victim user's machine! That user is named `zardus`, with a home directory of `/home/zardus`. You, as the `hacker` user, have write access to his `.bashrc`, and `zardus` has read-access to `/flag`. The victim is simulated by the script `/challenge/victim`, and you can launch this script at any time to observe the victim logging into the computer. Can you get the flag?

Add the following line to zardus' .bashrc file:

```bash
cat /flag > /tmp/flag
```

Then simulate the victim logging in with `/challenge/victim`

![](../../../attachments/pwn-college/01-linux-luminarium/15-silly-shenanigans/001-bashrc-backdoor.md/Pasted%20image%2020250924065503.png)
