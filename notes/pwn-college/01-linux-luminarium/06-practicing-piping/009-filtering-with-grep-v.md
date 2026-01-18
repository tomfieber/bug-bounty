The `grep` command has a very useful option: `-v`(invert match). While normal `grep` shows lines that MATCH a pattern, `grep -v` shows lines that do NOT match a pattern.

In this challenge, `/challenge/run` will output the flag to stdout, but it will also output over 1000 decoy flags (containing the word `DECOY`somewhere in the flag) mixed in with the real flag. You'll need to filter _out_ the decoys while keeping the real flag!

```bash
/challenge/run | grep -v DECOY
```

