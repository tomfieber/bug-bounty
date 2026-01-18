Bash supports the expansion of multiple globs in a single word.

We put a few happy, but diversely-named files in `/challenge/files`. Go `cd` there and run `/challenge/run`, providing a single argument: a short (3 characters or less) globbed word with two `*` globs in it that covers every word that contains the letter `p`.

```bash
# Get into the right directory
cd /challenge/files

# Run the challenge program
/challenge/run *p*
```

