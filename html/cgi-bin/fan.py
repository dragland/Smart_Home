#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#Import Libraries
import os
import relayCGI

#Actual program
os.system("gpio mode 3 out")
if relayCGI.read_state(int(1)) == "1":
	relayCGI.relay_on(int(1))
else:
	relayCGI.relay_off(int(1))
relayCGI.header()
