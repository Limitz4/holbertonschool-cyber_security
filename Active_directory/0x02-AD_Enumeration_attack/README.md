# Active Directory Enumeration and Credential Abuse - Security Labs

## Overview

This project explores how misconfigurations in enterprise identity systems can expose credentials or privilege relationships. The guided lab covers Kerberos-related risks, user attributes, graph-based directory analysis, and the security implications of highly privileged replication permissions.

## Exercise Topics

| Topic | Security Concept |
| --- | --- |
| AS-REP roasting | Risk associated with Kerberos accounts that do not require preauthentication. |
| Kerberoasting | Why service-account password strength and SPN exposure matter. |
| LDAP and BloodHound enumeration | How directory information and privilege relationships can be reviewed. |
| User-attribute inspection | The danger of placing sensitive data in readable directory fields. |
| DCSync permissions | Why replication privileges require strict monitoring and least privilege. |

## Files

`0-flag.txt` through `4-flag.txt` record guided lab results. These are verification artifacts, not scripts or complete security reports; challenge values are omitted from this documentation.

## Defensive Lessons

- Require appropriate Kerberos preauthentication and strong service-account passwords.
- Minimize and audit sensitive delegation and replication rights.
- Restrict privileged group membership and review access-control changes.
- Avoid storing secrets in directory attributes.
- Monitor Kerberos and directory-service events for suspicious patterns.

## Scope and Ethics

These exercises concern a controlled AD training environment. Studying identity attack techniques helps assess and improve defenses; it does not authorize testing external directories or accounts.

