# Active Reconnaissance - Lab Findings

## Overview

This directory records results from guided active-reconnaissance exercises in a controlled training environment. The activities investigate exposed services, web-server technology, application endpoints, database information, and hidden paths.

The repository primarily contains **text answers and lab findings**, not an automated scanning framework.

## Files

| File | Recorded Finding |
| --- | --- |
| `0-ports.txt` | Identified open service port. |
| `1-webserver.txt` | Identified web-server product/version. |
| `2-injectable.txt` | Endpoint identified during a controlled injection test. |
| `3-database.txt` | Database identifier collected in the lab. |
| `4-tables.txt` | Number of discovered database tables. |
| `5-hidden_dir.txt` | Hidden web directory identified during enumeration. |
| `100-flag.txt` - `102-flag.txt` | Additional lab verification artifacts. |

## Skills Practiced

- Discovering reachable services and open ports.
- Identifying server software and web technologies.
- Mapping web paths and endpoints.
- Recording findings in a repeatable, reviewable format.
- Understanding the difference between service discovery and vulnerability validation.

## Typical Assessment Workflow

1. Confirm the allowed target and testing scope.
2. Identify exposed network services in the lab.
3. Inspect the application and enumerate relevant paths.
4. Validate observations using the approved lab methodology.
5. Record only supported findings and avoid overstating their impact.

## Scope and Limitations

These files are outputs from exercises. They do not include the complete commands, packet captures, or reports necessary to independently reproduce every finding. Any vulnerability assessment must be performed only in an explicitly authorized environment.

