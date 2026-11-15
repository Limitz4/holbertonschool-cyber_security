# Burp Suite Fundamentals - Web Security Lab

## Overview

This directory records hands-on exercises with Burp Suite's core tools for intercepting, inspecting, and testing HTTP(S) traffic in an authorized web-security lab.

## Exercise Map

| Artifact | Related Exercise |
| --- | --- |
| `0-flag.txt` | Initial Burp Suite setup, browser proxy configuration, and HTTPS interception. |
| `1-flag.txt` | Client-side TLS certificate configuration. |
| `2-flag.txt` | Intercepting and modifying a server response. |
| `3-flag.txt` | Inspecting and replaying requests with **Repeater**. |
| `4-flag.txt` | Exploring parameterized requests with **Intruder**. |
| `5-flag.txt` | Examining tokens and their randomness with **Sequencer**. |
| `6-flag.txt` | Working with encoded values using **Decoder**. |

These files contain lab verification outputs, not screenshots, captured requests, or a standalone Burp extension.

## Concepts Practiced

- Configuring an intercepting proxy between a browser and a test application.
- Understanding HTTPS interception and the role of certificates.
- Comparing HTTP requests and responses.
- Replaying requests while examining server behavior.
- Using Burp tools to investigate input handling and session tokens.

## Typical Authorized Workflow

1. Configure Burp's proxy listener and a browser for a lab target.
2. Inspect captured requests and responses.
3. Use the relevant Burp tool to investigate the lab question.
4. Document supported observations and defensive implications.

## Skills Demonstrated

- Familiarity with Burp Proxy, Repeater, Intruder, Sequencer, and Decoder.
- Manual analysis of web application behavior.
- Understanding how requests, responses, sessions, and certificates interact.

## Responsible Use

Use these techniques only on applications that you own or have explicit permission to assess. The presence of challenge result files does not, by itself, establish a reproducible vulnerability finding or production security impact.

