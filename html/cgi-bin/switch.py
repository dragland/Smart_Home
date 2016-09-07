#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#*********************************************************************
#                           SETUP
#*********************************************************************
import cgi
import relayCGI

#*********************************************************************
#                            MAIN
#*********************************************************************
PIN_NUMBER = relayCGI.get_value("PIN_NUMBER")
relayCGI.set_mode(PIN_NUMBER)
if relayCGI.read_state(PIN_NUMBER) == "1":
	relayCGI.relay_on(PIN_NUMBER)
else:
	relayCGI.relay_off(PIN_NUMBER)
relayCGI.print_blank_header()
