# File Upload Vulnerabilities - Validation and Security Controls

## Overview

This project explores risks in file upload functionality through guided web-security exercises. The tasks focus on the difference between client-side checks and trusted server-side validation, filename handling, file signatures, and upload-size restrictions.

## Exercise Map

| File | Related Topic |
| --- | --- |
| `0-target.txt` | Identification of an upload-related target in the lab. |
| `1-flag.txt` | Testing assumptions about client-side file restrictions. |
| `2-flag.txt` | Exploring the handling of special characters in uploaded filenames. |
| `3-flag.txt` | Investigating file signatures and magic-byte validation. |
| `4-flag.txt` | Investigating file-size restrictions and their enforcement. |

The text files contain lab answers or validation artifacts; they do not contain a complete upload service or a production exploit.

## Security Concepts

- **Client-side checks are insufficient:** Browser-side restrictions can support usability but should not be trusted as the only security boundary.
- **Filename validation:** Uploaded names should be normalized and safely generated to prevent unexpected file-path behavior.
- **Content verification:** File extensions and declared MIME types should not be the only factors in deciding whether a file is safe.
- **Upload limits:** Size, count, and resource-consumption restrictions should be enforced on the server.
- **Storage isolation:** Uploaded content should be stored outside executable application paths and served with appropriate response headers.

## Defensive Checklist

1. Define a strict allowlist of permitted file types and business use cases.
2. Enforce validation and size limits on the server.
3. Generate safe storage filenames instead of trusting user-provided paths.
4. Isolate uploaded content from application execution.
5. Log relevant failures and evaluate scanning or content transformation where appropriate.

## Scope

This directory documents educational lab observations. It does not demonstrate that a real service has been compromised. Testing upload controls should be limited to applications that you own or are expressly authorized to assess.

