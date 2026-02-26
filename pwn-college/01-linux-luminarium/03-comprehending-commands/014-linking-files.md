In this level the flag is, as always, in `/flag`, but `/challenge/catflag` will instead read out `/home/hacker/not-the-flag`. Use the symlink, and fool it into giving you the flag!

```bash
# Create the symbolic link
ln -s /flag /home/hacker/not-the-flag

# Run the checker
/challenge/catflag
```


