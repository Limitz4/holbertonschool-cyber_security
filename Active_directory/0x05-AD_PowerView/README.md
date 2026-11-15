# Active Directory Enumeration with PowerView

## Overview

This directory documents guided PowerView exercises in a Windows Active Directory lab. The tasks focus on reviewing domain metadata, user and group attributes, directory permissions, and administrative exposure using PowerShell-based enumeration concepts.

## Exercise Topics

| Area | Learning Objective |
| --- | --- |
| Domain reconnaissance | Examine domain properties and basic identity information. |
| User attributes | Understand the security relevance of account metadata. |
| Groups and shares | Investigate group membership and access relationships. |
| ACLs and delegated permissions | Recognize overly broad access rights. |
| SYSVOL review | Understand how shared domain files can expose sensitive information. |
| SPNs and service accounts | Review service identities and Kerberos-related exposure. |

## Files

`0-flag.txt` through `5-flag.txt` contain results from guided exercises. There are no custom PowerView modules or full PowerShell transcripts committed in this directory.

## Skills Practiced

- Understanding PowerShell-based directory inspection.
- Recognizing common AD object types and access-control concepts.
- Interpreting user/group configuration from a defensive perspective.
- Documenting lab findings without overstating the available evidence.

## Defensive Takeaways

Apply least privilege, review delegation and group membership, protect service accounts, monitor directory changes, and restrict access to sensitive shared files.

## Scope and Safety

PowerView is a dual-use security administration and assessment tool. The exercises are intended for authorized lab environments; the presence of lab flags does not demonstrate unauthorized access to an external domain.

