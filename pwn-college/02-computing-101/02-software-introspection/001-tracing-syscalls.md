The first one is pretty simple: the **s**yscall **trace**r, `strace`.

Given a program to run, `strace` will use functionality of the Linux operating system to introspect and record every system call that the program invokes, and its result. For example, let's look at our program from the previous challenge:

```console
hacker@dojo:~$ strace /tmp/your-program
execve("/tmp/your-program", ["/tmp/your-program"], 0x7ffd48ae28b0 /* 53 vars */) = 0
exit(42)                                 = ?
+++ exited with 42 +++
hacker@dojo:~$
```

As you can see, `strace` reports what system calls are triggered, what parameters were passed to them, and what data they returned. The syntax used here for output is `system_call(parameter, parameter, parameter, ...)`. This syntax is borrowed from a programming language called C, but we don't have to worry about that yet. Just keep in mind how to read this specific syntax.

In this example, `strace` reports two system calls: the second is the `exit` system call that your program uses to request its own termination, and you can see the parameter you passed to it (42). The first is an `execve` system call. We'll learn about this system call later, but it's somewhat of a yin to `exit`'s yang: it starts a new program (in this case, `your-program`). It's not actually invoked by `your-program` in this case: its detection by `strace` is a weird artifact of how `strace` works, that we'll investigate later.

In the final line, you can see the result of `exit(42)`, which is that the program exits with an exit code of `42`!

Now, the `exit` syscall is easy to introspect without using `strace` --- after all, part of the point of `exit` is to give you an exit code that you can access. But other system calls are less visible. For example, the `alarm` system call (syscall number 37!) will set a timer in the operating system, and when that many seconds pass, Linux will terminate the program. The point of `alarm` is to, e.g., kill the program when it's frozen, but in this case, we'll use `alarm` to practice our `strace` snooping!

In this challenge, you must `strace` the `/challenge/trace-me` program to figure out what value it passes as a parameter to the `alarm` system call, then call `/challenge/submit-number` with the number you've retrieved as the argument. Good luck!

---
![](../../../attachments/pwn-college/02-computing-101/02-software-introspection/001-tracing-syscalls.md/Pasted%20image%2020250924135831.png)

This one is simple. Just follow the instructions. 