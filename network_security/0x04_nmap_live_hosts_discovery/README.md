# Nmap Live Host Discovery

## Overview

This directory contains Bash scripts demonstrating different host-discovery probes with Nmap. The exercises compare ARP, ICMP, TCP, and UDP discovery techniques and help explain why a single probing method does not always identify every live host.

## Files

| Script | Discovery Method |
| --- | --- |
| `0-arp_scan.sh` | ARP-based host discovery (`-PR`). |
| `1-icmp_echo_scan.sh` | ICMP echo discovery (`-PE`). |
| `2-icmp_timestamp_scan.sh` | ICMP timestamp probes (`-PP`). |
| `3-icmp_address_mask_scan.sh` | ICMP address-mask probes (`-PM`). |
| `4-tcp_syn_ping.sh` | TCP SYN discovery on ports 22, 80, and 443 (`-PS`). |
| `5-tcp_ack_ping.sh` | TCP ACK discovery on ports 22, 80, and 443 (`-PA`). |
| `6-udp_ping_scan.sh` | UDP discovery on ports 53, 161, and 162 (`-PU`). |
| `100-flag.txt` | Lab verification artifact. |

All scripts accept a target address or range as their first argument. They use `sudo` and Nmap's `-sn` option for host discovery without a regular port scan.

## Example

On a lab network that you own or have explicit authorization to test:

```bash
chmod u+x 1-icmp_echo_scan.sh
./1-icmp_echo_scan.sh 192.0.2.10
```

`192.0.2.10` is a documentation-only example address; replace it with a permitted lab target.

## Technical Takeaways

- ARP discovery works primarily within a local broadcast domain.
- ICMP requests may be blocked or filtered.
- TCP and UDP probes offer alternative discovery signals.
- A negative response to one technique does not always prove a host is offline.

## Responsible Use

Run network probes only against authorized hosts and ranges. Results depend on routing, access controls, and network configuration. These scripts are learning exercises and should not be represented as a complete asset-discovery platform.

