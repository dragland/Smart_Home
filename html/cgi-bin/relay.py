#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 3.0 | 2017

#************************************SETUP**************************************
import smartHomeCGI

#*****************************Raspberry Pi Pinout*******************************
RELAY_PIN = 5

#*************************************MAIN**************************************
smartHomeCGI.header("BLANK")
smartHomeCGI.set_mode(RELAY_PIN)
if smartHomeCGI.read_state(RELAY_PIN) == "0":
	smartHomeCGI.relay_on(RELAY_PIN)
else:
	smartHomeCGI.relay_off(RELAY_PIN)
