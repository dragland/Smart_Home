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
smartHomeCGI.header("HTML")
QUERY = smartHomeCGI.get_value("QUERY")
print QUERY