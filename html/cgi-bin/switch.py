#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#*********************************************************************
#                           SETUP
#*********************************************************************
import smartHomeCGI

#*********************************************************************
#                            MAIN
#*********************************************************************
smartHomeCGI.header("BLANK")
PIN_NUMBER = int(smartHomeCGI.get_value("PIN_NUMBER"))
smartHomeCGI.set_mode(PIN_NUMBER)
if smartHomeCGI.read_state(PIN_NUMBER) == "1":
	smartHomeCGI.relay_on(PIN_NUMBER)
else:
	smartHomeCGI.relay_off(PIN_NUMBER)