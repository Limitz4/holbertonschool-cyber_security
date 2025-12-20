#!/bin/bash

user=$1

ps -u "$user" -o user,vsz,rss | grep -v " VSZ RSS" | grep -v " 0 0 "
