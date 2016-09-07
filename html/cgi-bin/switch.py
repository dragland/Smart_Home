#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#*********************************************************************
#                           SETUP
#*********************************************************************
import os
import relayCGI

#*********************************************************************
#                            MAIN
#*********************************************************************
form = cgi.FieldStorage()
PIN_NUMBER = form["PIN_NUMBER"].value

os.system("gpio mode %d out" % PIN_NUMBER)

if relayCGI.read_state(int(PIN_NUMBER)) == "1":
	relayCGI.relay_on(int(PIN_NUMBER))
else:
	relayCGI.relay_off(int(PIN_NUMBER))
relayCGI.header()
