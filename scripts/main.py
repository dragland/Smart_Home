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
import RPi.GPIO

#Function to read data from AM2302 humidity and temperature sensor
def read_rh_temp(PIN_NUMBER):
	global rh
	global temp_f
	r_h, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, PIN_NUMBER, 5, 3)
	if r_h and temp is not None:
		rh = r_h
		temp_f = temp * 1.8 + 32.0
	time.sleep(2)

#Function to read data from magnetic door sensor
def read_door(PIN_NUMBER):
	global door
	RPi.GPIO.setmode(RPi.GPIO.BCM)
	RPi.GPIO.setup(PIN_NUMBER, RPi.GPIO.IN, pull_up_down = RPi.GPIO.PUD_UP)
	if RPi.GPIO.input(PIN_NUMBER):
		door = 1
	else:
		door = 0
	time.sleep(0.1)

#Function to print and write current data from each sensor module to state CSV
def write_state():
	data = str("%s,%3.1f,%3.1f,%d" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), temp_f, rh, door))
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
door = 0
t1 = threading.Thread(target = read_rh_temp, args = (4))
t2 = threading.Thread(target = read_door, args = (17))
t1.start()
t2.start()
while True:	
	if t1.is_alive()is False:
		del t1
		t1 = threading.Thread(target = read_rh_temp, args = (4,))
		t1.start()
	if t2.is_alive()is False:
		del t2
		t2 = threading.Thread(target = read_door, args = (17,))
		t2.start()
	write_state()
	time.sleep(1)