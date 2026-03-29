# Scanning with Nmap

## Scanning Options

| **Nmap Option**      | **Description**                                                        |
| -------------------- | ---------------------------------------------------------------------- |
| `10.10.10.0/24`      | Target network range.                                                  |
| `-sn`                | Disables port scanning.                                                |
| `-Pn`                | Disables ICMP Echo Requests                                            |
| `-n`                 | Disables DNS Resolution.                                               |
| `-PE`                | Performs the ping scan by using ICMP Echo Requests against the target. |
| `--packet-trace`     | Shows all packets sent and received.                                   |
| `--reason`           | Displays the reason for a specific result.                             |
| `--disable-arp-ping` | Disables ARP Ping Requests.                                            |
| `--top-ports=<num>`  | Scans the specified top ports that have been defined as most frequent. |
| `-p-`                | Scan all ports.                                                        |
| `-p22-110`           | Scan all ports between 22 and 110.                                     |
| `-p22,25`            | Scans only the specified ports 22 and 25.                              |
| `-F`                 | Scans top 100 ports.                                                   |
| `-sS`                | Performs an TCP SYN-Scan.                                              |
| `-sA`                | Performs an TCP ACK-Scan.                                              |
| `-sU`                | Performs an UDP Scan.                                                  |
| `-sV`                | Scans the discovered services for their versions.                      |
| `-sC`                | Perform a Script Scan with scripts that are categorized as "default".  |
| `--script <script>`  | Performs a Script Scan by using the specified scripts.                 |
| `-O`                 | Performs an OS Detection Scan to determine the OS of the target.       |
| `-A`                 | Performs OS Detection, Service Detection, and traceroute scans.        |
| `-D RND:5`           | Sets the number of random Decoys that will be used to scan the target. |
| `-e`                 | Specifies the network interface that is used for the scan.             |
| `-S 10.10.10.200`    | Specifies the source IP address for the scan.                          |
| `-g`                 | Specifies the source port for the scan.                                |
| `--dns-server <ns>`  | DNS resolution is performed by using a specified name server.          |




## Output Options


| **Nmap Option** | **Description** |
|---|----|
| `-oA filename` | Stores the results in all available formats starting with the name of "filename". |
| `-oN filename` | Stores the results in normal format with the name "filename". |
| `-oG filename` | Stores the results in "grepable" format with the name of "filename". |
| `-oX filename` | Stores the results in XML format with the name of "filename". |



## Performance Options

| **Nmap Option**              | **Description**                                              |
| ---------------------------- | ------------------------------------------------------------ |
| `--max-retries <num>`        | Sets the number of retries for scans of specific ports.      |
| `--stats-every=5s`           | Displays scan's status every 5 seconds.                      |
| `-v/-vv`                     | Displays verbose output during the scan.                     |
| `--initial-rtt-timeout 50ms` | Sets the specified time value as initial RTT timeout.        |
| `--max-rtt-timeout 100ms`    | Sets the specified time value as maximum RTT timeout.        |
| `--min-rate 300`             | Sets the number of packets that will be sent simultaneously. |
| `-T <0-5>`                   | Specifies the specific timing template.                      |

## Specific Scans

### Syn scan

```
sudo nmap 10.129.2.28 -p 21,22,25 -sS -Pn -n --disable-arp-ping --packet-trace
```

### Ack scan

```
sudo nmap 10.129.2.28 -p 21,22,25 -sA -Pn -n --disable-arp-ping --packet-trace
```

### Decoy scan

```
sudo nmap 10.129.2.28 -p 80 -sS -Pn -n --disable-arp-ping --packet-trace -D RND:5
```

### Testing firewall rule

```
sudo nmap 10.129.2.28 -n -Pn -p445 -O
```

### Scan by using a different source IP

```
sudo nmap 10.129.2.28 -n -Pn -p 445 -O -S 10.129.2.200 -e tun0
```

### DNS Proxying

Good for scanning from DMZ

```
sudo nmap 10.129.2.28 -p50000 -sS -Pn -n --disable-arp-ping --packet-trace
```

### SYN scan from DNS port

```
sudo nmap 10.129.2.28 -p50000 -sS -Pn -n --disable-arp-ping --packet-trace --source-port 53
```

### Connect to filtered port

```
ncat -nv --source-port 53 10.129.2.28 50000
```

### Scan filtered ports

```
sudo nmap -g53 --max-retries=1 -Pn -p- --disable-arp-ping 10.129.142.113
```

### Full scan

```bash
sudo nmap --open -p- -A -oA inlanefreight_ept_tcp_all_svc -iL scope
```

## Nmap grep

### Count number of open ports

```
NMAP_FILE=output.grep

egrep -v "^#|Status: Up" $NMAP_FILE | cut -d' ' -f2,4- | \
sed -n -e 's/Ignored.*//p' | \
awk -F, '{split($0,a," "); printf "Host: %-20s Ports Open: %d\n" , a[1], NF}' \
| sort -k 5 -g
```

### Print top 10 ports

```
NMAP_FILE=output.grep

egrep -v "^#|Status: Up" $NMAP_FILE | cut -d' ' -f4- | \
sed -n -e 's/Ignored.*//p' | tr ',' '\n' | sed -e 's/^[ \t]*//' | \
sort -n | uniq -c | sort -k 1 -r | head -n 10
```

### Top service identifiers

```
NMAP_FILE=output.grep

egrep -v "^#|Status: Up" $NMAP_FILE | cut -d ' ' -f4- | tr ',' '\n' | \
sed -e 's/^[ \t]*//' | awk -F '/' '{print $7}' | grep -v "^$" | sort | uniq -c \
| sort -k 1 -nr
```

### Top service names

```
NMAP_FILE=output.grep

egrep -v "^#|Status: Up" $NMAP_FILE | cut -d ' ' -f4- | tr ',' '\n' | \
sed -e 's/^[ \t]*//' | awk -F '/' '{print $5}' | grep -v "^$" | sort | uniq -c \
| sort -k 1 -nr
```

### Hosts and open ports

```
NMAP_FILE=output.grep

egrep -v "^#|Status: Up" $NMAP_FILE | cut -d' ' -f2,4- | \
sed -n -e 's/Ignored.*//p'  | \
awk '{print "Host: " $1 " Ports: " NF-1; $1=""; for(i=2; i<=NF; i++) { a=a" "$i; }; split(a,s,","); for(e in s) { split(s[e],v,"/"); printf "%-8s %s/%-7s %s\n" , v[2], v[3], v[1], v[5]}; a="" }'
```

### Banner grap

```
NMAP_FILE=output.grep

egrep -v "^#|Status: Up" $NMAP_FILE | cut -d' ' -f2,4- | \
awk -F, '{split($1,a," "); split(a[2],b,"/"); print a[1] " " b[1]; for(i=2; i<=NF; i++) { split($i,c,"/"); print a[1] c[1] }}' \
 | xargs -L1 nc -v -w1
```


