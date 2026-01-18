You can specify the `MODE` in two ways: as a modification of the existing permissions mode, or as a completely new mode to overwrite the old one.

In this level, we will cover the former: modifying an existing mode. `chmod` allows you to tweak permissions with the mode format of `WHO`+/-`WHAT`, where `WHO` is user/group/other and `WHAT` is read/write/execute. For example, to add _read_access for the owning _user_, you would specify a mode of `u+r`. `w`rite and e`x`ecute access for the `g`roup and the `o`ther (or `a`ll the modes) are specified the same way.

In this challenge, you must change the permissions of the `/flag` file to read it! Typically, you need to have write access to the file in order to change its permissions, but I have made the `chmod` command all-powerful for this level, and you can `chmod` anything you want even though you are the `hacker` user. This is an ultimate power. The `/flag` file is owned by `root`, and you can't change that, but you can make it readable.

```bash
chmod go+r /flag
```

