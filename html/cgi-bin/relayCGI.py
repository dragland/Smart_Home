#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#*********************************************************************
#                           SETUP
#*********************************************************************
import os
import cgi
import subprocess

#*********************************************************************
#                          FUNCTIONS
#*********************************************************************
#Function: get_value
#This function gets the value from an HTTP GET call.
def get_value(KEY):
	form = cgi.FieldStorage()
	return form[KEY].value

#Function: set_mode
#This function sets the mode of a relay.
def set_mode(PIN_NUMBER):
	os.system("gpio mode %i out" % PIN_NUMBER)

#Function: read_state
#This function reads the state of a relay.
def read_state(PIN_NUMBER):
	output = subprocess.check_output(["gpio read %i" % (PIN_NUMBER)], shell=True)
	return str(output)[:1]

#Function: relay_on
#This function turns on a relay.
def relay_on(PIN_NUMBER):
	os.system("gpio write %i 0" % (PIN_NUMBER))

#Function: relay_off
#This function turns off a relay.
def relay_off(PIN_NUMBER):
	os.system("gpio write %i 1" % (PIN_NUMBER))

#Function: blank_header
#This function returns a blank HTTP packet.
def blank_header():
	print "Status: 204 No Content"
	print "Content-type: text/plain"
	print ""

#Function: html_header
#This function returns an HTML header.
def html_header():
	print "Content-Type: text/html"
	print ""