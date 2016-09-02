#!/usr/bin/env bash
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

sudo git fetch --all
sudo git reset --hard origin/master
until scripts/main.py; do
	echo "main.py has failed with exit code $?. Restarting child process..." >&2
	sleep 1
done