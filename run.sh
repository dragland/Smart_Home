#!/usr/bin/env bash
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 3.0 | 2017

#*********************************** SETUP *************************************
cd /var/www
sudo git fetch --all
sudo git reset --hard origin/master
clear

#************************************ MAIN *************************************
until scripts/main.py; do
	echo "main.py has failed with exit code $?. Restarting child process..." >&2
	sleep 1
done
