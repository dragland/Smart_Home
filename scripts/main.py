#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#Import libraries 
import os
import sys
import serial
import time
import datetime
import threading
import subprocess

#Function to print and write current data from each sensor module to state CSV
def write_state():
	data = str("%s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
	state = open("../html/state.txt", "w")
	state.write(data + "\n")
	state.close()
	print ">> System Status:",
	print data,
	sys.stdout.flush()
	print "\r",

#Actual Program
print("Executing program:")
while True:	
	write_state()
	time.sleep(1)