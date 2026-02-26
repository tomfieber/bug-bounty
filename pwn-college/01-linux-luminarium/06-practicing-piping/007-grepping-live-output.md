It turns out that you can "cut out the middleman" and avoid the need to store results to a file, like you did in the last level. You can do this by using the `|` (pipe) operator. Standard output from the command to the left of the pipe will be connected to (_piped into_) the standard input of the command to the right of the pipe.

```bash
/challenge/run | grep pwn.college
```

