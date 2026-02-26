In this challenge, `/challenge/run` will refuse to run while `/challenge/dont_run` is running! You must find the `dont_run` process and `kill` it. If you fail, `pwn.college` will disavow all knowledge of your mission.

```bash
ps -efww

# After you find the target process, use kill
kill $PID
```

