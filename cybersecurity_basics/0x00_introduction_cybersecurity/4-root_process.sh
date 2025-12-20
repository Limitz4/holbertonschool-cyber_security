#!/bin/bash

ps -o user,vsz,rss | grep -v "VSZ RSS" | grep -v " 0 0"
