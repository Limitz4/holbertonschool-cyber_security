# Linux Security Basics - System and Network Inspection

## Overview

This project contains Bash exercises using common Linux administration and security tools. The scripts inspect login activity, active connections, listening services, firewall rules, system configuration, packet traffic, and target hosts within an authorized lab.

## Files

| File | Command or Task | Purpose |
| --- | --- | --- |
| `0-login.sh` | `last` | Review recent system logins with timestamps. |
| `1-active-connections.sh` | `ss` | List active TCP connections and associated processes. |
| `2-incoming_connections.sh` | `ufw` | Add a firewall rule allowing inbound TCP traffic on port 80. |
| `3-firewall_rules.sh` | `iptables` | Inspect rules in the security table. |
| `4-network_services.sh` | `netstat` | Display listening network services and owning processes. |
| `5-audit_system.sh` | `lynis` | Run a local system security audit. |
| `6-capture_analyze.sh` | `tcpdump` | Capture a small sample of network packets. |
| `7-scan.sh` | `nmap` | Perform a basic scan of a user-supplied target. |

## Concepts Practiced

- Login auditing and process visibility.
- TCP sessions, listening sockets, and network services.
- Host-based firewall configuration and rule inspection.
- Security auditing with Lynis.
- Basic packet capture with tcpdump.
- Authorized host scanning with Nmap.

## Example Usage

Inspect active connections in a Linux VM:

```bash
chmod u+x 1-active-connections.sh 4-network_services.sh
./1-active-connections.sh
./4-network_services.sh
```

The scripts rely on commands such as `ss`, `ufw`, `iptables`, `netstat`, `lynis`, `tcpdump`, and `nmap`. Some may need to be installed separately; several commands invoke `sudo` and therefore require appropriate permissions.

## Important Safety Notes

- `2-incoming_connections.sh` **changes the system firewall configuration**. Review the command before running it and use a disposable VM or sandbox.
- Packet capture and port scanning should be performed only on systems and networks you own or are authorized to test.
- Audit and scan results depend on the environment; this repository contains exercise scripts rather than proof that a particular host has been secured.

