### Challenge

  
In this level, you will be working with registers. You will be asked to modify or read from registers.

In this level, you will work with multiple registers. Please set the following:

- `rax = 0x1337`
- `r12 = 0xCAFED00D1337BEEF`
- `rsp = 0x31337`

---
### Solution

asm2.s

```asm
.intel_syntax noprefix
.global _start
_start:
mov rax, 0x1337
mov r12, 0xCAFED00D1337BEEF
mov rsp, 0x31337
```

