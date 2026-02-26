Previously, you `read` user input into a variable. You've also previously redirected files into command input! Put them together, and you can read files with the shell.

```console
hacker@dojo:~$ echo "test" > some_file
hacker@dojo:~$ read VAR < some_file
hacker@dojo:~$ echo $VAR
test
```

What happened there? The example redirects `some_file` into the _standard input_ of `read`, and so when `read` reads into `VAR`, it reads from the file! Now, use that to read `/challenge/read_me` into the `PWN` environment variable, and we'll give you the flag! The `/challenge/read_me` will keep changing, so you'll need to read it right into the `PWN` variable with one command!

```bash
read PWN < /challenge/read_me
```

