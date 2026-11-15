# Nmap Advanced Port Scanning

## Overview

This project explores how different TCP scan techniques work in Nmap. The Bash scripts demonstrate NULL, FIN, Xmas, Maimon, ACK, Window, and custom-flag scanning options against an explicitly authorized lab target.

## Files

| File | Technique |
| --- | --- |
| `0-null_scan.sh` | TCP NULL scan using `-sN`. |
| `1-fin_scan.sh` | FIN scan using `-sF`, with packet fragmentation and a timing setting. |
| `2-xmas_scan.sh` | Xmas scan using `-sX`, packet tracing, and reason output. |
| `3-maimon_scan.sh` | Maimon scan using `-sM` against selected common services. |
| `4-ask_scan.sh` | ACK scan for examining response and filtering behavior. |
| `5-window_scan.sh` | ACK/Window scan options with excluded ports. |
| `6-custom_scan.sh` | Experiment with custom scan flags and file output. |

## Concepts Practiced

- Understanding TCP flag combinations and how a scanner interprets responses.
- Comparing scan behavior under different host and firewall conditions.
- Using Nmap output controls such as `--reason`, `--packet-trace`, and `-oN`.
- Recognizing why `open`, `closed`, `filtered`, and `open|filtered` are context-dependent scan states.

## Usage

Inspect each script and its arguments before running it. In a disposable, authorized network lab, an example is:

```bash
chmod u+x 0-null_scan.sh
./0-null_scan.sh 192.0.2.10
```

`192.0.2.10` is a documentation-only address; supply an authorized test target. Several techniques require elevated privileges, and their behavior varies by Nmap version and operating system.

## Scope and Limitations

These scripts are small scanning exercises, not a complete vulnerability assessment. Some commands use exercise-specific port selections or scan options; review and validate them in your lab before relying on their results. Scan only hosts for which you have explicit permission.

