Just like standard output, you can also redirect the error channel of commands. Here, we'll learn about _File Descriptor numbers_. A File Descriptor (FD) is a number that _describes_ a communication channel in Linux. You've already been using them, even though you didn't realize it. We're already familiar with three:

- FD 0: Standard Input
- FD 1: Standard Output
- FD 2: Standard Error

When you redirect process communication, you do it by FD number, though some FD numbers are implicit. For example, a `>` without a number implies `1>`, which redirects FD 1 (Standard Output).

In this challenge, you will need to redirect the output of `/challenge/run`, like before, to `myflag`, and the "errors" (in our case, the instructions) to `instructions`. You'll notice that nothing will be printed to the terminal, because you have redirected everything! You can find the instructions/feedback in `instructions`and the flag in `myflag` when you successfully pull this off!

```bash
/challenge/run > myflag 2> instructions
```

