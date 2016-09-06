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
os.system("gpio mode 0 out")
if relayCGI.read_state(int(0)) == "1":
	relayCGI.relay_on(int(0))
else:
	relayCGI.relay_off(int(0))
relayCGI.header()
