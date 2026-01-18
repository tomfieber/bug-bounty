You can also use process substitution for _writing_ to commands!

You can duplicate data to two files with `tee`.

But wait! You just learned that bash can make commands look like files using process substitution! For writing to a command (output process substitution), use `>(command)`. If you write an argument of `>(rev)`, bash will run the `rev`command (this command reads data from standard input, reverses its order, and writes it to standard output!), but hook up its input to a temporary named pipe file. When commands write to this file, the data goes to the standard input of the command. 

In this challenge, we have `/challenge/hack`, `/challenge/the`, and `/challenge/planet`. Run the `/challenge/hack` command, and duplicate its output as input to both the `/challenge/the` and the `/challenge/planet` commands! Scroll back through the previous challenges "Duplicating piped data with tee" and "Process substitution for input" if you need a refresher on this method.

```bash
/challenge/hack | tee >(/challenge/the) >(/challenge/planet)
```





