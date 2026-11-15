# Wireshark Basics - Packet Analysis Filters

## Overview

This project provides Wireshark display-filter expressions for investigating traffic patterns associated with common network discovery and scanning techniques. The exercises focus on reading packet fields and narrowing traffic views, including TCP flags, ICMP messages, UDP packets, and ARP activity.

## Files

| File | Traffic Pattern |
| --- | --- |
| `0-ip_scan.txt` | ICMP traffic selected by IP protocol number. |
| `1-tcp_syn.txt` | TCP SYN packets matching an exercise-specific window-size condition. |
| `2-tcp_connect_scan.txt` | TCP SYN packets matching a different window-size condition. |
| `3-tcp_fin.txt` | TCP FIN packets. |
| `4-tcp_ping_sweep.txt` | TCP packets on port 80 matching selected SYN/ACK and payload conditions. |
| `5-udp_port_scan.txt` | ICMP destination-unreachable / port-unreachable responses. |
| `6-udp_ping_sweep.txt` | UDP traffic matching the lab's destination port and length. |
| `7-icmp_ping_sweep.txt` | ICMP echo requests and replies. |
| `8-arp_scanning.txt` | ARP traffic matching an exercise-specific destination hardware address. |

## How to Use

1. Open a packet capture in Wireshark, or capture traffic on an authorized interface.
2. Open the relevant `.txt` file.
3. Copy its expression into the **Display Filter** field.
4. Apply the filter and inspect matching packets, conversations, and timestamps.

Example filter from `7-icmp_ping_sweep.txt`:

```text
icmp.type == 8 or icmp.type == 0
```

This selects ICMP echo requests and echo replies.

## Skills Demonstrated

- Using Wireshark display filters.
- Interpreting TCP flag fields and packet metadata.
- Recognizing ICMP and UDP discovery patterns.
- Distinguishing filtering evidence from definitive attribution.

## Limitations

The repository contains **filter expressions**, not packet-capture files or a full network-forensics report. Some expressions include values chosen for a particular lab and are not reliable signatures of an attack on their own. Packet patterns should be interpreted in context.

