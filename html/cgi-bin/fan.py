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
os.system("gpio mode 4 out")
if relayCGI.read_state(int(4)) == "1":
	relayCGI.relay_on(int(4))
else:
	relayCGI.relay_off(int(4))
relayCGI.header()
