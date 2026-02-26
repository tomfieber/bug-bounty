Note that there are no spaces around the `=`! If you put spaces (e.g., `VAR = 1337`), the shell won't recognize a variable assignment and will, instead, try to run the `VAR` command (which does not exist).

Also note that this uses `VAR` and _not_ `$VAR`: the `$` is only prepended to _access_ variables. In shell terms, this prepending of `$` triggers what is called _variable expansion_, and is, surprisingly, the source of many potential vulnerabilities (if you're interested in that, check out the Art of the Shell dojo when you get comfortable with the command line!).

To solve this level, you must set the `PWN` variable to the value `COLLEGE`. Be careful: both the names and values of variables are case-sensitive! `PWN` is not the same as `pwn` and `COLLEGE` is not the same as `College`.

```bash
PWN=COLLEGE
```

