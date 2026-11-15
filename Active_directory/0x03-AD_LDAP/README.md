# Active Directory LDAP Enumeration

## Overview

This directory contains guided exercises exploring Lightweight Directory Access Protocol (LDAP) queries and directory enumeration in an Active Directory lab. The focus is on understanding what information can be retrieved from domain objects and why access control and data exposure matter.

## Exercise Topics

| Lab Area | Focus |
| --- | --- |
| Basic LDAP enumeration | Discovering directory users and attributes. |
| Directory inspection with a network administration tool | Reviewing exposed AD object information. |
| BloodHound data collection | Mapping directory relationships for security analysis. |
| RPC-based user enumeration | Understanding alternate methods of discovering account metadata. |
| Advanced LDAP filters | Selecting objects by specific attributes and configuration properties. |

## Repository Contents

`0-flag.txt`, `1-flag.txt`, `2-flag.txt`, `3-flag.txt`, and `4-flag.txt` contain lab verification outputs. The repository does not include a reusable LDAP client or exported domain dataset for these exercises.

## Skills Practiced

- Understanding LDAP object attributes and search filters.
- Recognizing the relationship between directory services and authentication.
- Interpreting the security implications of discoverable account information.
- Documenting authorized AD enumeration observations.

## Defensive Relevance

LDAP visibility should be assessed alongside access-control permissions, service-account hygiene, and monitoring. The ability to query an attribute does not automatically imply that the domain has been compromised.

## Scope

All concepts are framed for a simulated or explicitly authorized enterprise lab. No challenge values or sensitive directory data are reproduced here.

