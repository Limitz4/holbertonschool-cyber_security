#!/bin/bash
cut -d " " -f7 auth.log | sort | uniq -c  | sort -nr
