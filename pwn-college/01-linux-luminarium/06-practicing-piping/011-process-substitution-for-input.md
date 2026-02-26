Sometimes you need to compare the output of two commands rather than two files.

Linux follows the philosophy that ["everything is a file"](https://en.wikipedia.org/wiki/Everything_is_a_file). That is, the system strives to provide file-like access to most resources, including the input and output of running programs! The shell follows this philosophy, allowing you to, for example, use any utility that takes file arguments on the command line and hook it up to the output of programs, as you learned in the previous few levels.

Interestingly, we can go further, and hook input and output of programs to _arguments_ of commands. This is done using [Process Substitution](https://www.gnu.org/software/bash/manual/html_node/Process-Substitution.html). For reading from a command (input process substitution), use `<(command)`. When you write `<(command)`, bash will run the command and hook up its output to a temporary file that it will create.

Now for your challenge! Recall what you learned in the `diff` challenge from [Comprehending Commands](https://pwn.college/linux-luminarium/commands). In that challenge, you diffed two files. Now, you'll diff two sets of command outputs: `/challenge/print_decoys`, which will print a bunch of decoy flags, and `/challenge/print_decoys_and_flag` which will print those same decoys plus the real flag.

Use process substitution with `diff` to compare the outputs of these two programs and find your flag!

```bash
diff <(/
challenge/print_decoys) <(/challenge/print_decoys_and_flag)
```


