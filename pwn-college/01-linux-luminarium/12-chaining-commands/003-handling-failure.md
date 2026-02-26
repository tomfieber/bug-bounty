  
You just learned about the `&&` operator, which runs the second command only if the first succeeds. Now let's learn about its opposite: the `||` operator allows you to run a second command only if the first command fails (exits with a non-zero code). This is called the "OR" operator because either the first command succeeds OR the second command will run.

The `||` operator is super useful for providing fallback commands or error handling!

In this challenge, you need to chain `/challenge/first-failure` and `/challenge/second` using the `||` operator. Go for it!

```bash
/challenge/first-failure || /challenge/second
```

