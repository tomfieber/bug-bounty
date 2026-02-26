`tr` can also translate characters to nothing (i.e., _delete_ them). This is done via a `-d` flag and an argument of what characters to delete

Now you give it a try. I'll intersperse some decoy characters (specifically: `^` and `%`) among the flag characters. Use `tr -d` to remove them!

```bash
/challenge/run | tr -d ^%
```

