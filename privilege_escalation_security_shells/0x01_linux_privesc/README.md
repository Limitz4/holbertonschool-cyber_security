# Linux Privilege Escalation - Guided Security Labs

## Overview

This directory documents Linux privilege-escalation exercises conducted in isolated training systems. The focus is on identifying configuration weaknesses, understanding why they grant unintended access, and recognizing the defensive controls that would prevent them.

## Lab Scenarios

| Exercise | Security focus | Result artifact |
| --- | --- | --- |
| Restricted-file access | Reviewing permitted `sudo` commands and the security implications of privileged utilities, including `choom` | `0-flag.txt` |
| Misconfigured scheduled job | Examining a root-owned cron workflow whose executed script is writable by a lower-privileged account | `1-flag.txt` |
| SUID binary assessment | Enumerating SUID executables and reviewing how an unsafe binary or configuration can cross a privilege boundary | `2-flag.txt` |

## Concepts Explored

- Linux users, groups, effective user IDs, and the principle of least privilege.
- `sudo` rules and the risks of granting powerful command access.
- Cron-job ownership, script permissions, and trusted execution paths.
- SUID permissions and the difference between legitimate elevated execution and privilege abuse.
- System enumeration as a foundation for privilege-escalation risk assessment.

## Repository Contents

The three `*-flag.txt` files are verification artifacts from guided challenges. They are **not** privilege-escalation scripts, automated scanners, or full technical reports. The challenge values are intentionally omitted from this README.

## Defensive Takeaways

1. Review `sudoers` rules and avoid unnecessary privileged command exceptions.
2. Protect scripts executed by root-owned scheduled jobs from untrusted modification.
3. Audit SUID files regularly and remove elevated privileges where they are not needed.
4. Monitor permission changes and unexpected execution in privileged contexts.

## Scope

All scenarios refer to explicitly authorized laboratory environments. No production system or third-party target is assessed in this repository.
