#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 3.0 | 2017

#************************************SETUP**************************************
import smartHomeCGI

#*************************************MAIN**************************************
smartHomeCGI.header("HTML")
QUERY = smartHomeCGI.get_value("QUERY")
smartHomeCGI.queryBot(QUERY)
