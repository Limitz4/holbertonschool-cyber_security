# Passive Reconnaissance and Open-Source Intelligence

## Overview

This project explores reconnaissance using publicly accessible registration, DNS, and internet-facing asset information. It includes scripts for WHOIS queries, DNS record enumeration, subdomain discovery, and a written OSINT assessment of an organization's public digital footprint.

## Files

| File | Purpose |
| --- | --- |
| `0-whois.sh` | Queries registration information with `whois` and exports selected fields to a CSV file. |
| `1-a_record.sh` | Looks up DNS A records. |
| `2-mx_record.sh` | Looks up mail exchanger records. |
| `3-txt_record.sh` | Looks up DNS TXT records. |
| `4-dig_all.sh` | Collects DNS answers using `dig`. |
| `5-subfinder.sh` | Performs subdomain enumeration with `subfinder`. |
| `holbertonschool_report.md` | Documents a passive review of public-facing assets, observed technologies, and defensive considerations. |
| `100-flag.txt` - `102-flag.txt` | Lab completion artifacts. Their values are intentionally not reproduced here. |

## Techniques and Tools

- WHOIS registration queries.
- DNS A, MX, and TXT lookups with `nslookup` and `dig`.
- Subdomain enumeration with `subfinder`.
- Public-data review and written technical reporting.
- Distinguishing observed facts from possible security implications.

## Example Usage

Within an authorized practice environment:

```bash
chmod u+x 1-a_record.sh 2-mx_record.sh 3-txt_record.sh
./1-a_record.sh example.com
./2-mx_record.sh example.com
./3-txt_record.sh example.com
```

WHOIS fields and DNS responses differ by domain, registrar, and resolver. The associated report is a point-in-time assessment, and its observations should be revalidated before being treated as current infrastructure facts.

## Portfolio-Relevant Skills

- Mapping a public attack surface using open-source intelligence.
- Collecting and organizing DNS and registration evidence.
- Writing a concise technical reconnaissance report.

## Responsible Use

Work only within authorized scopes, respect data privacy, and avoid presenting unverified public metadata as proof of a vulnerability. Passive reconnaissance does not by itself demonstrate a successful intrusion or a security flaw.

