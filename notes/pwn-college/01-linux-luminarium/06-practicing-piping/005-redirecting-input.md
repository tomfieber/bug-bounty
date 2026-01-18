Just like you can redirect _output_ from programs, you can redirect input _to_ programs! This is done using `<`.

In this level, we will practice using `/challenge/run`, which will require you to redirect the `PWN` file to it and have the `PWN` file contain the value `COLLEGE`! To write that value to the `PWN` file, recall the prior challenge on output redirection from `echo`!

```bash
# Create the file with the correct content
echo COLLEGE > PWN

# Redirect the input from PWN to the challenge program
/challenge/run < PWN
```

