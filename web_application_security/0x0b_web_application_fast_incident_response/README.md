# Web Application Fast Incident Response - Log Triage

## Overview

This project contains Bash one-liners for quickly extracting useful indicators from web-server log data. The exercises focus on identifying the most frequent source IP, the most requested endpoint, the number of requests from the leading source, and a common client-library indicator.

## Files

| File | Analysis |
| --- | --- |
| `0-attack_ip.sh` | Counts requests by source IP and outputs the most frequent address. |
| `1-endpoint.sh` | Finds the most frequently requested endpoint in the supplied log. |
| `2-count_attack.sh` | Reports the request count for the highest-volume source IP. |
| `3-library.sh` | Extracts and counts a client/user-agent-related field from quoted log content. |

## Tools and Techniques

- `awk` for selecting log fields.
- `sort`, `uniq -c`, and `head` for frequency analysis.
- Simple command pipelines for rapid incident triage.
- Distinguishing suspicious patterns from confirmed malicious activity.

## Usage

These scripts expect a local file named **`logs.txt`** in the working directory. That log file is **not included** in the repository; use an approved sample or sanitized lab data matching the expected format.

```bash
chmod u+x 0-attack_ip.sh
./0-attack_ip.sh
```

## Operational Limitations

- The scripts assume a particular space-delimited/quoted log layout and may not work as intended with a different logging format.
- A high request volume does not prove that an IP address is an attacker.
- Additional context, timestamps, response codes, and corroborating telemetry are needed before drawing incident conclusions.

## Skills Demonstrated

Fast shell-based log triage, basic indicator extraction, and evidence-aware security analysis.

