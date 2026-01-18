Here, the flag file is owned by the `root` user and the `root` group, and the `hacker` user is neither the `root` user nor a member of the `root` group, so the file cannot be accessed. Luckily, group ownership can be changed with the `chgrp` (**ch**ange **gr**ou**p**) command!

In this level, I have made the flag readable by whatever group owns it, but this group is currently `root`. Luckily, I have also made it possible for you to invoke `chgrp` as the `hacker` user! Change the group ownership of the flag file, and read the flag!

```bash
chgrp hacker /flag
```

