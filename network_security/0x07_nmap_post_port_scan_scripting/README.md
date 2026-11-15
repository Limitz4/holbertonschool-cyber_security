# Nmap Post-Scan Enumeration and NSE Scripting

## Overview

This directory contains Bash wrappers around Nmap's scripting engine (NSE). The exercises extend basic port discovery with service identification, default scripts, selected vulnerability checks, banner inspection, and TLS-related enumeration.

## Files

| File | Main Focus |
| --- | --- |
| `0-nmap_default.sh` | Run Nmap's default script category (`-sC`). |
| `1-nmap_vulners.sh` | Use the `vulners` NSE script against selected web ports. |
| `2-vuln_scan.sh` | Run a check related to the Apache Struts CVE-2017-5638 issue. |
| `3-comprehensive_scan.sh` | Combine service detection and selected HTTP, TLS, and FTP scripts. |
| `4-vulnerability_scan.sh` | Run selected vulnerability-oriented NSE script families. |
| `5-service_enumeration.sh` | Collect service, banner, TLS, and SMB-domain information. |

The scripts use common options such as `-sV`, `-sC`, `--script`, and `-oN`; some save output to local text files when executed.

## Skills Demonstrated

- Moving from port discovery to service enumeration.
- Selecting NSE scripts for a defined assessment question.
- Recording scan output and interpreting service information.
- Distinguishing an automated vulnerability indication from a confirmed finding.

## Example

After reviewing the script, it can be run against a target within your own isolated test network:

```bash
chmod u+x 0-nmap_default.sh
./0-nmap_default.sh 192.0.2.10
```

Replace the documentation address with an explicitly authorized lab system. The availability of individual scripts, such as `vulners`, depends on the installed Nmap/NSE environment and script data.

## Defensive Relevance

Service and version inventory can help identify unexpectedly exposed ports, weak configurations, and patching priorities. Scan outputs require validation, context, and authorization before being used in a security report.

