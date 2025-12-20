#!/bin/bash

ps -u root -o user,pid,vsz,rss,cmd | grep -v " 0 0"
