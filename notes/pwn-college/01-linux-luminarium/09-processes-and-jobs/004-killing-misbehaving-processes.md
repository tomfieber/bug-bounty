In this challenge, there's a decoy process that's hogging a critical resource - a named pipe (FIFO) at `/tmp/flag_fifo`into which (like in the [Practicing Piping](https://pwn.college/linux-luminarium/piping) FIFO challenge) `/challenge/run` wants to write your flag. You need to `kill`this process.

Your general workflow should be:

1. Check what processes are running.
2. Find `/challenge/decoy` in the list and figure out its process ID.
3. `kill` it.
4. Run `/challenge/run` to get the flag without being overwhelmed by decoys (you don't need to redirect its output; it'll write to the FIFO on its own).

![](../../../attachments/pwn-college/01-linux-luminarium/09-processes-and-jobs/004-killing-misbehaving-processes.md/Pasted%20image%2020250918152426.png)

```bash
# Kill the process
kill 142

# Check the named pipe
cat /tmp/flag_fifo
```

