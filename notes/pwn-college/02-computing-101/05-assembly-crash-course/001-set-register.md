### Challenge

  
In this level, you will be working with registers. You will be asked to modify or read from registers.

In this level, you will work with registers! Please set the following:

`rdi = 0x1337`

---
### Solution

asm1.s

```bash
.intel_syntax noprefix
.global _start
_start:
mov rdi, 0x1337
```

