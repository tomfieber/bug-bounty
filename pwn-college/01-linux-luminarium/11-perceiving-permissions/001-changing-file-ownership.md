`college_file`'s owner has been changed to the `hacker` user, and now `hacker` can do with it whatever `root` had been able to do with it! If this was the `/flag` file, that means that the `hacker` user would be able to read it!

In this level, we will practice changing the owner of the `/flag` file to the `hacker` user, and then read the flag. For this challenge only, I made it so that you can use chown to your heart's content as the `hacker` user (again, typically, this requires you to be `root`). Use this power wisely and chown away!

```bash
chown hacker:hacker /flag
```

