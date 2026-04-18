#!/bin/bash
tail -n 1000  auth.log| cut -d " " -f12 |tail -n 1
