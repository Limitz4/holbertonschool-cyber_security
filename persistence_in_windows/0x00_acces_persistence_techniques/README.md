# Windows Persistence Mechanisms - Investigation Labs

## Overview

This directory covers how legitimate Windows autorun and task-management features can be misused for persistence. The exercises focus on recognizing these mechanisms, examining their configuration, and understanding how administrators can detect and remove unauthorized entries.

## Guided Exercises

| Exercise | Windows component | Investigation focus |
| --- | --- | --- |
| `0-flag.txt` | Startup folders | Identifying programs or scripts configured to run at user sign-in |
| `1-flag.txt` | Registry autorun keys | Reviewing Run-key entries and interpreting encoded information in referenced scripts |
| `2-flag.txt` | Windows Services | Inspecting automatically started services and metadata such as descriptions |
| `3-flag.txt` | Task Scheduler | Finding scheduled tasks and examining triggers, descriptions, and execution context |

The broader exercise brief also introduces Background Intelligent Transfer Service (BITS) jobs as a persistence technique. **No BITS demonstration script or report is currently committed in this folder.**

## Security Concepts

- User-specific versus machine-wide autorun locations.
- Registry-based startup behavior and why unauthorized entries should be audited.
- Windows service configuration and automatic execution after startup.
- Scheduled-task triggers, account privileges, and task metadata.
- BITS job monitoring as part of Windows endpoint security.

## Detection and Hardening

1. Review autorun entries and startup directories with trusted administrative tools.
2. Alert on unexpected changes to service startup settings and task registrations.
3. Apply least privilege to registry keys, executable locations, and service configuration.
4. Correlate suspicious autorun changes with Windows event logs and endpoint telemetry.
5. Remove unauthorized persistence mechanisms and verify the system returns to a trusted state.

## Repository Contents and Scope

The four `*-flag.txt` files record challenge verification results. They are **not** persistence payloads or scripts that install autorun mechanisms. All investigation topics are presented in the context of a controlled, authorized Windows laboratory.
