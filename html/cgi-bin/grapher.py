#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#*********************************************************************
#                           SETUP
#*********************************************************************
import relayCGI
import cgi

#*********************************************************************
#                            MAIN
#*********************************************************************
print "Content-Type: text/html"
print ""

form = cgi.FieldStorage()
print form["PIN_NUMBER"].value