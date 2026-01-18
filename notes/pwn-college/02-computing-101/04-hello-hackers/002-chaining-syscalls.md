### Challenge

Okay, our previous solution wrote output but then crashed. In this level, you will write output, and then _not_crash!

We'll do this by invoking the `write` system call, and then invoking the `exit` system call to cleanly exit the program. How do we invoke two system calls? Just like you invoke two instructions! First, you set up the necessary registers and invoke `write`, then you set up the necessary registers and invoke `exit`!

Your previous solution had 5 instructions (setting `rdi`, setting `rsi`, setting `rdx`, setting `rax`, and `syscall`). This one should have those 5, plus three more for `exit` (setting `rdi` to the exit code, setting `rax` to syscall index `60`, and `syscall`). For this level, let's exit with exit code `42`!

---
### Solution

hh2.s

```asm
.intel_syntax noprefix
.global _start
_start:
mov rdi, 1
mov rsi, 1337000
mov rdx, 1
mov rax, 1
syscall
mov rdi, 42
mov rax, 60
syscall
```

