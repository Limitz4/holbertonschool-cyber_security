# Ruby Scripting for Cybersecurity and Automation

## Overview

This project contains a sequence of Ruby exercises progressing from basic language concepts to file operations, HTTP requests, simple cryptography demonstrations, dictionary-based hash matching, and command-line automation.

## Files

| File | Focus |
| --- | --- |
| `0-hello_world_function.rb` | Functions and basic program output. |
| `1-hello_world_class.rb` | Classes and methods. |
| `2-prime.rb` | Number checking and conditional logic. |
| `3-read_file.rb` | Reading local files. |
| `4-write_file.rb` | Writing local files. |
| `5-cipher.rb` | A Caesar cipher class for reversible text transformation. |
| `6-get.rb` | Sending an HTTP GET request and parsing JSON. |
| `7-args.rb` | Working with command-line arguments. |
| `8-post.rb` | Sending an HTTP POST request with JSON content. |
| `9-download_file.rb` | Downloading a file from a URL. |
| `10-password_cracked.rb` | Comparing a SHA-256 hash with hashes of words from a provided dictionary. |
| `11-cli.rb` | A small command-line task manager with add, list, and remove options. |

## Key Technologies

- Ruby standard library (`net/http`, `json`, `uri`, `digest`, `optparse`).
- Object-oriented programming and file handling.
- HTTP clients and JSON processing.
- Basic cryptographic concepts and security-oriented scripting.
- Command-line interface design.

## Example

The task-manager exercise supports creating and viewing a simple list of tasks:

```bash
ruby 11-cli.rb --help
ruby 11-cli.rb --add "Review access logs"
ruby 11-cli.rb --list
```

The script reads and writes `tasks.txt` in the current working directory.

## Skills Demonstrated

Writing reusable Ruby functions and classes, interacting with files and APIs, parsing arguments, and building small automation utilities.

## Security Notes

The Caesar cipher is educational and does not provide modern cryptographic protection. The hash-matching exercise is intended for authorized demonstrations using test data; it should not be used against other people's credentials or data. Network operations depend on the availability and trustworthiness of their target services.

