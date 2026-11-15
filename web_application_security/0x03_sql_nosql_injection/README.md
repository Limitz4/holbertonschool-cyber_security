# SQL and NoSQL Injection - Web Security Labs

## Overview

This directory contains answer artifacts from guided SQL and NoSQL injection exercises in an isolated training application. The tasks investigate how unsafe handling of user-controlled data can affect database queries, authentication, and access to application information.

The focus is on understanding vulnerability classes and their defensive implications. The repository contains **lab findings and verification files**, not an automated exploitation toolkit.

## Exercise Topics

| Topic | Learning Goal |
| --- | --- |
| SQL injection discovery | Recognize evidence of unsafe SQL query construction. |
| Database and table exposure | Understand potential consequences of injection vulnerabilities. |
| Time-based blind SQL injection | Recognize how application behavior can indirectly reveal information. |
| Second-order injection | Understand how stored input can become dangerous during later processing. |
| NoSQL injection discovery | Identify risks caused by unsafe handling of structured query input. |
| Authentication bypass risks | Understand how injection can affect authorization decisions. |
| NoSQL data exposure | Consider how query manipulation can expose application data. |

## Repository Files

- `0-vuln.txt` and `5-vuln.txt`: Short findings from vulnerability-identification exercises.
- `1-flag.txt` - `4-flag.txt` and `6-flag.txt` - `7-flag.txt`: Validation artifacts for the guided labs.

Challenge values are intentionally not repeated in this README.

## Defensive Takeaways

- Use parameterized SQL queries and properly configured database access layers.
- Validate and constrain input types, especially when interpreting JSON or query operators.
- Apply least-privilege database access to reduce impact.
- Keep authentication and authorization checks separate from user-controlled query data.
- Record reproducible findings with the affected endpoint, expected behavior, observed behavior, and recommended fix.

## Scope and Ethics

These exercises were designed for a controlled lab. No public-facing system should be tested without explicit authorization. The submitted text files are evidence of exercise responses, not a complete penetration-test report or proof that a production system is vulnerable.

