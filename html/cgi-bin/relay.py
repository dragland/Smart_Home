#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 3.0 | 2017

#************************************SETUP**************************************
import smartHomeCGI

#*************************************MAIN**************************************
smartHomeCGI.header("BLANK")
PIN_NUMBER = 5
smartHomeCGI.set_mode(PIN_NUMBER)
if smartHomeCGI.read_state(PIN_NUMBER) == "0":
	smartHomeCGI.relay_on(PIN_NUMBER)
else:
	smartHomeCGI.relay_off(PIN_NUMBER)
