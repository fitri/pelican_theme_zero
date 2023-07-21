Title: How to Check if Your Network Behind CGNAT
Date: 2023-06-30
Category: Network
Tags: ip, ipv4, networking
Slug: how-to-check-if-your-network-behind-cgnat
Authors: Fitri Rahim


### check the public ip address

Open up the terminal and sent a quick request to the ipify.

```bash
curl "https://api.ipify.org?format=json"
```

The services will sent a json reply with the public ip address.

```json
{"ip":"161.142.159.51"}
```

### trace the ip address route
Using terminal and command traceroute we can check the route it took for the network to reach this ip address.

Install traceroute if not available

**On Mac OS**
```bash
brew install traceroute
```

**On Debian based Linux**
```bash
apt install traceroute
```

Once the installation was done use traceroute to get the list of gate the network pass.

```bash
traceroute <public ip address>
```

If there's not private IP like gate used to reach the destination public IP then most likely the IP have direct connection to the internet and not behind any public IP pool CGNAT.

```bash
traceroute to 161.142.157.51 (161.142.157.51), 64 hops max, 52 byte packets
 1  192.168.1.1 (192.168.1.1)  4.506 ms  3.485 ms  3.281 ms
 2  10.35.208.1 (10.35.208.1)  5.459 ms  7.461 ms  9.485 ms
 3  * * *
 4  * * *
 5  * * *
 6  * * *
 7  * * *
 8  * * *
 9  * * *
10  * * *
```
Example above this IP most likely assigned thru CGNAT.
