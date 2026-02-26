When you pipe data from one command to another, you of course no longer see it on your screen. This is not always desired: for example, you might want to see the data as it flows through between your commands to debug unintended outcomes (e.g., "why did that second command not work???").

This process' `/challenge/pwn` must be piped into `/challenge/college`, but you'll need to intercept the data to see what `pwn` needs from you!

```bash
/challenge/pwn | tee pwn-output
```

Read the secret code and include the subsequent command piping to `/challenge/college`

```bash
/challenge/pwn --secret $CODE | /challenge/college
```

 

