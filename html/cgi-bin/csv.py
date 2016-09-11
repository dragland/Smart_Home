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
RANGE = smartHomeCGI.get_value("RANGE")
VALUE = smartHomeCGI.get_value("VALUE")
rows = smartHomeCGI.querryData("../archive.db", RANGE, VALUE)
smartHomeCGI.formatData(rows)