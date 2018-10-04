#!/usr/bin/env bash
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 4.0 | 2018

#*********************************** SETUP *************************************
cd /var/www
sudo git fetch --all
sudo git reset --hard origin/master
clear

#************************************ MAIN *************************************
hostname -I
until scripts/main.py; do
	echo "main.py has failed with exit code $?. Restarting child process..." >&2
	sleep 1
done
