#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 3.0 | 2017

#************************************SETUP**************************************
import smartHomeCGI

#*************************************MAIN**************************************
smartHomeCGI.header("BLANK")
RED_VAL   = smartHomeCGI.get_value("R")
GREEN_VAL = smartHomeCGI.get_value("G")
BLUE_VAL  = smartHomeCGI.get_value("B")
PARTY_VAL = smartHomeCGI.get_value("P")
if PARTY_VAL == "1":
    smartHomeCGI.set_leds_party()
else:
    smartHomeCGI.set_leds(RED_VAL,GREEN_VAL,BLUE_VAL)
