# OWASP Top 10 - Web Application Security Exercises

## Overview

This directory contains guided web-security exercises based on selected OWASP Top 10 risk categories. The recorded tasks explore cryptographic failures and injection-related weaknesses, including stored cross-site scripting (XSS), in an isolated learning environment.

## Repository Contents

| File | Purpose |
| --- | --- |
| `0-flag.txt` | Verification artifact from an introductory lab exercise. |
| `1-xor_decoder.sh` | Decodes a lab-specific XOR-obfuscated, Base64-encoded value. |
| `4-vuln.txt` | Records the relevant application field identified during a vulnerability exercise. |

The file list contains the submitted artifacts for the exercises; it is not a comprehensive implementation of all ten OWASP categories.

## Security Concepts

- Identifying common categories of web application risks.
- Understanding why weak encoding or obfuscation is not equivalent to secure encryption.
- Recognizing how untrusted input can become a stored XSS issue when output is not safely handled.
- Distinguishing vulnerability identification from remediation.

## Script Example

`1-xor_decoder.sh` demonstrates how a reversible transformation can be decoded in the context of a lab task. Inspect the script before running it:

```bash
chmod u+x 1-xor_decoder.sh
./1-xor_decoder.sh '{xor}LAB_VALUE'
```

The placeholder above is not a valid exercise result; a correctly formatted lab input is required.

## Defensive Takeaways

- Use cryptographic primitives suitable for the security requirement instead of custom reversible transformations.
- Validate input and perform context-aware output encoding to reduce XSS exposure.
- Apply security controls based on threat models and tested behavior.

## Scope

This project documents selected educational labs. It should not be taken as evidence of a complete OWASP Top 10 audit or a production penetration test.

