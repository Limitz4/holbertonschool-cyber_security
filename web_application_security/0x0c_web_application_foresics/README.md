# Web Application Forensics - Linux Log Investigation

## Overview

This directory contains small Bash exercises for investigating operating-system and authentication artifacts that can support a web application incident review. The scripts work with text logs and demonstrate simple filtering, counting, and summarization techniques.

## Files

| File | Purpose |
| --- | --- |
| `0-service.sh` | Groups values from a selected field of `auth.log` for review. |
| `1-operating.sh` | Extracts Linux-version-related lines from `dmesg` text. |
| `2-accounts.sh` | Extracts a field from recent authentication log entries. |
| `3-ips.sh` | Counts distinct source-field values in accepted root-password login records. |
| `4-firewall.sh` | Counts lines mentioning `iptables` and `INPUT` in the authentication log. |
| `5-users.sh` | Prints a fixed list of user names from the exercise, rather than enumerating live accounts. |

## Required Inputs

The scripts expect example files such as `auth.log` and `dmesg` in the current working directory. These supporting logs are not checked into this repository.

## Skills Practiced

- Reading Linux authentication and system logs.
- Extracting and counting events with `grep`, `cut`, `sed`, `sort`, and `wc`.
- Identifying information that may help scope a security incident.
- Recognizing the limits of field-based parsing and incomplete evidence.

## Example Usage

With sanitized laboratory log files in place:

```bash
chmod u+x 1-operating.sh 4-firewall.sh
./1-operating.sh
./4-firewall.sh
```

## Forensic Considerations

Preserve original logs, document collection time and source, and avoid treating a single parsed field as conclusive proof. These scripts are introductory analysis exercises, not a full forensic collection or chain-of-custody workflow.

