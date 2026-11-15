# Process Heap Memory - Security Research Exercise

## Overview

This project contains a Python exercise for examining the heap memory region of a Linux process through the `/proc` filesystem. It illustrates process-memory boundaries, byte searches, and the risks associated with modifying memory in a running process.

The source file is an educational memory-manipulation example. It is **not** a standalone proof of a buffer-overflow vulnerability, and it does not automatically detect or exploit a buffer overflow.

## File

| File | Description |
| --- | --- |
| `read_write_heap.py` | Locates a process heap region through `/proc/<pid>/maps`, searches its memory through `/proc/<pid>/mem`, and attempts to replace a matching byte sequence. |

## Concepts Practiced

- Virtual memory layout and heap address ranges.
- Process IDs and Linux `/proc` process metadata.
- Reading and searching byte sequences in process memory.
- Understanding why memory access requires appropriate permissions.
- Considering how unsafe memory operations can affect process integrity and availability.

## Defensive Lessons

- Memory corruption and unsafe writes can destabilize applications.
- Process isolation and access-control boundaries matter.
- Bounds checking, memory-safe languages, and compiler/runtime mitigations reduce classes of memory-safety bugs.
- A memory read/write demonstration should not be confused with a completed vulnerability assessment.

## Safety and Scope

The script can modify another process's live memory. Run it **only** against a disposable process created specifically for an authorized lab, with appropriate permissions. Do not use it against production processes or systems that you do not own or administer.

