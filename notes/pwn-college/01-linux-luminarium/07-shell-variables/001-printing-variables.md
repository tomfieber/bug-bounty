Let's start with printing variables out. The `/challenge/run` program will not, and cannot, give you the flag, but that's okay, because the flag has been put into the variable called "FLAG"! Just have your shell print it out!

You can also print out variables with `echo`, by prepending the variable name with a `$`. For example, there is a variable, `PWD`, that always holds the current working directory of the current shell.

```bash
# Run the challenge to get the flag printed into the shell variable
/challenge/run

# Print out the $FLAG variable
echo $FLAG
```

