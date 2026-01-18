In preparation for more complex levels, we want you to:

1. Redirect the output of `/challenge/run` to `/tmp/data.txt`.
2. This will result in a hundred thousand lines of text, with one of them being the flag, in `/tmp/data.txt`.
3. `grep` that for the flag!

```bash
# Redirect the challenge output to /tmp/data.txt
/challenge/run > /tmp/data.txt

# grep for the flag
grep pwn.college /tmp/data.txt
```

