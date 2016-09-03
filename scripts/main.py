#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#Import libraries 
import os
import sys
import time
import datetime
import threading
import Adafruit_DHT

#Function to read data from AM2302 humidity and temperature sensor
def read_rh_temp():
	global rh
	global temp_f
	r_h, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4, 5, 3)
	if r_h and temp is not None:
		rh = r_h
		temp_f = temp * 1.8 + 32.0
	time.sleep(2)

#Function to print and write current data from each sensor module to state CSV
def write_state():
	data = str("%s,%3.1f,%3.1f" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), temp_f, rh))
	state = open("html/state.txt", "w")
	state.write(data + "\n")
	state.close()
	print ">> System Status:",
	print data,
	sys.stdout.flush()
	print "\r",

#Actual Program
print("Executing program:")
temp_f = 70
rh = 50
t1 = threading.Thread(target=read_rh_temp)
t1.start()
while True:	
	if t1.is_alive()is False:
		del t1
		t1 = threading.Thread(target=read_rh_temp)
		t1.start()
	write_state()
	time.sleep(1)