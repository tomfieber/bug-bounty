Every shell command, including every program and every builtin, exits with an _exit code_ when it finishes running and terminates. This can be used by the shell, or the user of the shell (that's you!) to check if the process succeeded in its functionality (this determination, of course, depends on what the process is supposed to do in the first place).

You can access the exit code of the most recently-terminated command using the special `?` variable (don't forget to prepend it with `$` to read its value!)

In this challenge, you must retrieve the exit code returned by `/challenge/get-code` and then run `/challenge/submit-code` with that error code as an argument. Good luck!

```bash
# Get the code
/challenge/get-code

# Get the response code
echo $?

# Submit the code
/challenge/submit-code $CODE
```

![](../../../attachments/pwn-college/01-linux-luminarium/09-processes-and-jobs/010-process-exit-codes.md/Pasted%20image%2020250919084918.png)

