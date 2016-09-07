#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#*********************************************************************
#                           SETUP
#*********************************************************************
import relayCGI

#*********************************************************************
#                            MAIN
#*********************************************************************
relayCGI.html_header()
RANGE = relayCGI.get_value("RANGE")
print RANGE
