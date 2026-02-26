Sometimes, you want to grab specific columns of data, such as the first column, the third column, or the 42nd column. For this, there's the `cut` command.

The `-d` argument specifies the column _delimiter_ (how columns are separated). In this case, it's a space character. Of course, it has to be in quotes here so that the shell knows that the space is an argument rather than a space separating other arguments! The `-f` argument specifies the _field_ number (which column to extract).

In this challenge, the `/challenge/run` program will give you a bunch of lines with random numbers and single characters (characters of the flag) as columns. Use `cut` to extract the flag characters, then pipe them to `tr -d "\n"` (like the previous level!) to join them together into a single line. Your solution will look something like `/challenge/run | cut ??? | tr ???`, with the `???` filled out.

```bash
/challenge/run | cut -d " " -f 2 | tr -d "\n"
```

