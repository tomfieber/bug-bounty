One of the purposes of piping data is to _modify_ it. Many Linux commands will help you modify data in really cool ways. One of these is `tr`, which `tr`anslates characters it receives over standard input and prints them to standard output.

It can also handle multiple characters, with the characters in different positions of the first argument replaced with associated characters in the second argument.

In this level, `/challenge/run` will print the flag but will swap the casing of all characters (e.g., `A` will become `a` and vice-versa). Can you undo it with `tr` and get the flag?

```bash
/challenge/run | tr [:upper:] [:lower:]
```



