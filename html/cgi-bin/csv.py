#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 3.0 | 2017

#************************************SETUP**************************************
import smartHomeCGI

#*************************************MAIN**************************************
smartHomeCGI.header("HTML")
RANGE = smartHomeCGI.get_value("RANGE")
VALUE = smartHomeCGI.get_value("VALUE")
rows = smartHomeCGI.queryData("../archive.db", RANGE, VALUE)
smartHomeCGI.formatData(rows)
