# Active Directory Attack Path Analysis with BloodHound

## Overview

This project explores graph-based analysis of Active Directory relationships using BloodHound in a controlled lab. The exercises examine how accounts, group memberships, service principals, and access-control relationships can combine to create risky privilege paths.

## Topics Explored

- Collecting and exploring domain relationship data in BloodHound.
- Interpreting group, user, and host relationships.
- Understanding why excessive ACL permissions such as `GenericAll` are significant.
- Reviewing service-account and SPN exposure.
- Considering overlooked or disabled accounts in a security review.
- Understanding why exposed SYSVOL content and unsafe group policies deserve attention.

## Repository Contents

The directory contains `0-flag.txt` through `6-flag.txt`, which are lab verification artifacts. They document completion results, not exported BloodHound graphs, collection archives, or an independently reproducible assessment.

## Skills Demonstrated

- Understanding graph-based identity-security assessment concepts.
- Recognizing privilege paths and permission-related risk.
- Relating account hygiene to Active Directory attack-surface reduction.
- Interpreting lab outcomes with appropriate evidentiary limitations.

## Defensive Takeaways

- Regularly review sensitive ACLs and administrative group memberships.
- Reduce unnecessary privilege relationships and delegation.
- Audit service accounts, SPNs, and unused accounts.
- Protect SYSVOL content and monitor changes to authentication infrastructure.

## Responsible Use

Collect and analyze domain data only with explicit authorization. This directory contains training results and should not be described as a completed enterprise penetration test.

