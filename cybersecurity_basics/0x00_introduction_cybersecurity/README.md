# Introduction to Cybersecurity - Practical Linux Exercises

## Overview

This directory introduces foundational cybersecurity operations through five small Bash scripts. The exercises cover login history, password generation, file integrity verification, SSH key generation, and process inspection.

## Files

| File | Description |
| --- | --- |
| `0-login.sh` | Displays the five most recent login records using `last`. |
| `1-gen_password.sh` | Generates a random alphanumeric password of a requested length using `/dev/urandom`. |
| `2-sha256_validator.sh` | Checks a file against a supplied SHA-256 checksum. |
| `3-gen_key.sh` | Generates a 4096-bit RSA SSH key pair at a supplied path. |
| `4-root_process.sh` | Lists processes for a specified user. |

## Key Concepts

- **Account activity:** Reviewing login history can help establish who accessed a system and when.
- **Strong credentials:** Randomly generated passwords reduce predictable patterns.
- **Integrity checking:** A SHA-256 digest can help detect file changes, provided the expected digest comes from a trusted source.
- **SSH authentication:** Public/private key pairs enable key-based remote authentication.
- **Process visibility:** Reviewing processes helps identify running user applications and services.

## Example Usage

Run these examples from the project directory in a Linux practice environment:

```bash
chmod u+x 0-login.sh 1-gen_password.sh 2-sha256_validator.sh 3-gen_key.sh 4-root_process.sh
./0-login.sh
./1-gen_password.sh 20
./4-root_process.sh root
```

For the integrity exercise, provide a file path and its expected SHA-256 checksum:

```bash
./2-sha256_validator.sh sample.txt EXPECTED_SHA256_HASH
```

## Skills Demonstrated

- Basic Linux security monitoring and shell usage.
- Password and key generation concepts.
- File integrity verification.
- Inspecting process ownership.

## Security Notes

The SSH key-generation exercise creates an unencrypted private key for demonstration purposes. Protect private keys and use an appropriate passphrase and key-management policy for real systems. The scripts are educational examples, not a complete security monitoring solution.

