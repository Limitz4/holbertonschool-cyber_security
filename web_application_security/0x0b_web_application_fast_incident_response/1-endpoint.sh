#!/bin/bash
cat dos.logs | cut -d " " -f7  | uniq -c |sort -nr|head -1| awk '{print $2}'
