### Challenge

Okay, we have one thing left for this run of challenges. You've written out a single byte, and now we'll practice writing out multiple bytes. I've stored a 14-character secret string at memory location `1337000`. Can you write it out?

>[!tip]
>The _only_ thing you should have to change compared to your previous solution is the value in `rdx`!

---
### Solution

```asm
.intel_syntax noprefix
.global _start
_start:
mov rdi, 1
mov rsi, 1337000
mov rdx, 14
mov rax, 1
syscall
mov rdi, 42
mov rax, 60
syscall
```

