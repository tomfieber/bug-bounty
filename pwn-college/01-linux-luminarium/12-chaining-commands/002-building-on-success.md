The `&&` operator allows you to run a second command only if the first command succeeds (in Linux convention, this means it exited with code 0). This is called the "AND" operator because both conditions must be true: the first command must succeed AND then the second command will run. That's super useful for complex commandline workflows where certain actions depend on the success of other actions.

In this challenge, you need to chain the programs `/challenge/first-success` and `/challenge/second` using the `&&`operator. Try running each command separately first to see what happens (which is that you will _not_ get the flag). But if you chain them with `&&`, the flag will appear!

```bash
/challenge/first-success && /challenge/second
```

