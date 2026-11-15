# Windows Privilege Escalation - Configuration and Credential Exposure Labs

## Overview

These guided Windows exercises examine how sensitive installation files, local credential material, weak service permissions, and PowerShell activity records can contribute to security incidents. The objective is to recognize risky configurations and understand their defensive implications.

## Exercise Areas

| Lab | Topic | Repository evidence |
| --- | --- | --- |
| 0 | Locating unattended installation configuration files and checking for administrator-password fields | `0-flag.txt`, `extract_password.py` |
| 1 | Investigating exposed SAM/SYSTEM backup material and the risks of recoverable local credentials | `1-flag.txt` |
| 2 | Reviewing service permissions and potential DLL-loading weaknesses | Task covered in the exercise brief; no `2-flag.txt` is currently committed here |
| 3 | Searching PowerShell transcription records for commands, contextual evidence, and concealed exercise data | `3-flag.txt` |

## Python Utility: `extract_password.py`

The included Python script checks several common Windows locations for unattended setup files, including Panther and Sysprep paths. It uses a regular expression to **detect whether an `AdministratorPassword` element is present**, reports the result, and handles unreadable files.

**Important distinction:** despite its filename, the currently committed script does **not** print or decode administrator passwords, create an elevated session, or automate the full lab. It is a configuration-presence check.

## Skills and Security Concepts

- Windows configuration and local-privilege boundaries.
- Risks of credentials stored in unattended deployment artifacts.
- Security impact of readable backup files and weak service-directory permissions.
- The role of PowerShell transcripts in investigation and accountability.
- Safe file inspection and pattern matching with Python.

## Defensive Recommendations

- Remove deployment secrets from accessible setup files after installation.
- Restrict permissions on credential stores, backup material, service binaries, and DLL search locations.
- Monitor high-privilege service changes and suspicious credential access.
- Protect PowerShell transcription records against unauthorized access or tampering.

## Repository Notes

The `*-flag.txt` files are lab verification artifacts, not exploit code or independent forensic reports. Exercise targets and credentials are not reproduced here. Work is limited to authorized Windows lab environments.
