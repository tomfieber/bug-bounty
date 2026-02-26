I've hidden the flag in a random directory on the filesystem. It's still called `flag`. Go find it!

Several notes. First, there are other files named `flag` on the filesystem. Don't panic if the first one you try doesn't have the actual flag in it. Second, there're plenty of places in the filesystem that are not accessible to a normal user. These will cause `find` to generate errors, but you can ignore those; we won't hide the flag there! Finally, `find`can take a while; be patient!

```bash
find / -type f -name "flag" 2>/dev/null
```

