#!/bin/bash
ps -u "$1" u | grep -v "VSZ" | grep -v " 0      0 "
