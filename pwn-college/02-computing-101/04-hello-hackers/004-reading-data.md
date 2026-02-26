### Challenge

You now know how to output data to stdout using `write`. But how does your program receive input data? It `read`s it from stdin!

Like `write`, `read` is a system call that shunts data around between file descriptors and memory, and its syscall number is `0`. In `read`'s case, it reads some amount of bytes from the provided file descriptor and stores them in memory. The C-style syntax is the same as `write`:

```c
read(0, 1337000, 5);
```

This will read `5` bytes from file descriptor `0` (stdin) into memory starting from `1337000`. So, if you type in (or pipe in) `HELLO HACKERS` into stdin, the above `read` call would result in the following memory configuration:

```text
  Address │ Contents
+────────────────────+
│ 1337000 │ 48       │
│ 1337001 │ 45       │
│ 1337002 │ 4c       │
│ 1337003 │ 4c       │
│ 1337004 │ 4f       │
+────────────────────+
```

What are those numbers?? They are _hexadecimal_ representations of _ASCII_-encoded letters. If those words don't make sense, please run through the first half or so of the [Dealing with Data](https://pwn.college/fundamentals/data-dealings) module and then come back here!

In this level, we will combine `read` with our previous `write` abilities. Your program should:

1. first `read` 8 bytes from stdin to address `1337000`
2. then `write` those 8 bytes from address `1337000` to stdout
3. finally, exit with the exit code `42`.

Remember: you've already written steps 2 and 3. All you have to do is add step 1!

>[!tip]
>**NOTE:** Keep in mind that, in this challenge, you'll be writing 8 characters, whereas in the previous challenge, you wrote 14. Don't forget to update your `write()` size (in `rdx`)!
>
>**DEBUGGING:** Having trouble? Build your program and run it with `strace` to see what's happening at the system call level!

---
### Solution

hh4.s

```asm
.intel_syntax noprefix
.global _start
_start:
mov rdi, 0
mov rsi, 1337000
mov rdx, 8
mov rax, 0
syscall
mov rdi, 1
mov rsi, 1337000
mov rdx, 8
mov rax, 1
syscall
mov rdi, 42
mov rax, 60
syscall
```