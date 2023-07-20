Title: How to Check If Your Network Behind CGNAT
Date: 2023-07-21
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

*On Mac OS*
```bash
brew install traceroute
```

*On Debian based Linux*
```bash
apt install traceroute
```

One the installation was done use traceroute to get the list of gate the network pass.

```bash
traceroute <public ip address>
```

If there's not private IP like gate used to reach the destination public IP then most likely the IP have direct connection to the internet and not behind any public IP pool CGNAT.
