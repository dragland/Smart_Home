#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#*********************************************************************
#                           SETUP
#*********************************************************************
import time
import subprocess
import os

#*********************************************************************
#                          FUNCTIONS
#*********************************************************************
#Function: read_state
#This function reads the state of a relay.
def read_state(pin):
	output = subprocess.check_output(["gpio read %i" % (pin)], shell=True)
	return str(output)[:1]

#Function: relay_on
#This function turns on a relay.
def relay_on(pin):
	os.system("gpio write %i 0" % (pin))

#Function: relay_off
#This function turns off a relay.
def relay_off(pin):
	os.system("gpio write %i 1" % (pin))

#Function: header
#This function returns a blank HTTP packet.
def header():
	print "Status: 204 No Content"
	print "Content-type: text/plain"
	print ""