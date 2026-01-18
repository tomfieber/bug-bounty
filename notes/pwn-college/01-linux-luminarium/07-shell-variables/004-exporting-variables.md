By default, variables that you set in a shell session are local to that shell process. That is, other commands you run won't inherit them. You can experiment with this by simply invoking another shell process in your own shell, like so:

```console
hacker@dojo:~$ VAR=1337
hacker@dojo:~$ echo "VAR is: $VAR"
VAR is: 1337
hacker@dojo:~$ sh
$ echo "VAR is: $VAR"
VAR is: 
```

In the output above, the `$` prompt is the prompt of `sh`, a minimal shell implementation that is invoked as a _child_ of the main shell process. And it does not receive the `VAR` variable!

This makes sense, of course. Your shell variables might have sensitive or weird data, and you don't want it leaking to other programs you run unless it explicitly should. How do you mark that it should? You _export_ your variables. When you export your variables, they are passed into the _environment variables_ of child processes. You'll encounter the concept of environment variables in other challenges, but you'll observe their effects here. Here is an example:

```console
hacker@dojo:~$ VAR=1337
hacker@dojo:~$ export VAR
hacker@dojo:~$ sh
$ echo "VAR is: $VAR"
VAR is: 1337
```

Here, the child shell received the value of VAR and was able to print it out! You can also combine those first two lines.

```console
hacker@dojo:~$ export VAR=1337
hacker@dojo:~$ sh
$ echo "VAR is: $VAR"
VAR is: 1337
```

In this challenge, you must invoke `/challenge/run`with the `PWN` variable exported and set to the value `COLLEGE`, and the `COLLEGE` variable set to the value `PWN` but _not_ exported (e.g., not inherited by `/challenge/run`).

```bash
# export the PWN variable
export PWN=COLLEGE

# Set the COLLEGE variable, but do not export
COLLEGE=PWN
```

Then run the challenge

```bash
/challenge/run
```

