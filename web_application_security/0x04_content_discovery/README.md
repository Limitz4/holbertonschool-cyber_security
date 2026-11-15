# Content Discovery - Web Attack Surface Enumeration

## Overview

This directory documents controlled content-discovery exercises involving hidden routes, directory enumeration, DNS subdomain discovery, and request fuzzing. The learning objective is to identify web resources that may not be linked in an application's normal navigation and evaluate why exposure matters to defenders.

## Tools and Techniques

| Technique | Purpose |
| --- | --- |
| Manual inspection | Review response headers and application behavior for useful context. |
| Directory enumeration | Identify accessible paths using an approved wordlist in a lab. |
| DNS subdomain discovery | Find hostnames associated with an authorized domain. |
| HTTP request fuzzing | Explore how a test application handles selected paths or inputs. |
| Findings review | Distinguish valid resources from redirects, error pages, and false positives. |

The guided exercises refer to tools such as **Gobuster** and **ffuf**, as well as manual inspection of HTTP responses.

## Repository Contents

- `0-flag.txt`, `1-flag.txt`, and `4-flag.txt` - `8-flag.txt`: Guided lab verification artifacts.
- `2-vendor.txt` and `3-senior.txt`: Short observations recorded during content-discovery tasks.

The source files store answers rather than a custom discovery program or full scan logs. Verification values are not repeated in this documentation.

## Skills Practiced

- Exploring web endpoints and understanding the relationship between URL paths and application resources.
- Using directory and subdomain discovery tools in a permitted environment.
- Choosing appropriate wordlists and interpreting HTTP responses.
- Recording discovered resources for security review.

## Defensive Takeaways

- Do not rely on a hidden or unlinked route for access control.
- Remove unused endpoints and restrict administrative resources.
- Apply authorization checks regardless of whether a URL is publicly advertised.
- Review exposed staging assets, backups, and accidentally published files.

## Responsible Use

Enumeration and fuzzing can generate substantial traffic. Use them only against authorized lab targets, with reasonable rate limits and clear scope. A discovered route is not automatically a vulnerability; security impact requires separate validation.

