What happens when there are multiple potential matches? What happens varies based on the specific shell and its options. By default `bash` will auto-expand until the first point when there are multiple options (in this case, `fl`). When you hit tab a _second_ time, it'll print out those options. Other shells and configurations, instead, will cycle through the options.

This challenge has a `/challenge/files` directory with a bunch of files starting with `pwncollege`. Tab-complete from `/challenge/files/p` or so, and make your way to the flag!

![](../../../attachments/pwn-college/01-linux-luminarium/05-file-globbing/009-multiple-options-for-tab-completion.md/Pasted%20image%2020250917105021.png)
Just tab through until you get pwncollege-flag.

