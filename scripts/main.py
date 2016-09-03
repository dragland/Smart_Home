#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#*********************************************************************
#                           SETUP
#*********************************************************************
import os
import sys
import time
import datetime
import threading
import Adafruit_DHT
import RPi.GPIO

#*********************************************************************
#                          FUNCTIONS
#*********************************************************************
#function: read_rh_temp
#This function reads the data from DHT22 AM2302 humidity and temperature sensor.
def read_rh_temp(PIN_NUMBER):
	global rh
	global temp_f
	r_h, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, PIN_NUMBER, 5, 3)
	if r_h and temp is not None:
		rh = r_h
		temp_f = temp * 1.8 + 32.0
	time.sleep(2)

#function: read_door
#This function reads the data from a magnetic door sensor.
def read_door(PIN_NUMBER):
	global door
	RPi.GPIO.setmode(RPi.GPIO.BCM)
	RPi.GPIO.setup(PIN_NUMBER, RPi.GPIO.IN, pull_up_down = RPi.GPIO.PUD_UP)
	if RPi.GPIO.input(PIN_NUMBER):
		door = 1
	else:
		door = 0
	time.sleep(0.1)

#function: read_lumin
#This function reads the data from an analog photoresistor.
def read_lumin(PIN_NUMBER):
	global lumin
	value = 0
	RPi.GPIO.setup(PIN_NUMBER, RPi.GPIO.OUT)
	RPi.GPIO.output(PIN_NUMBER, RPi.GPIO.LOW)
	value.sleep(0.1)
	RPi.GPIO.setup(PIN_NUMBER, RPi.GPIO.IN)
	while (RPi.GPIO.input(PIN_NUMBER) == RPi.GPIO.LOW):
		value += 1
	lumin = value

#function: write_state
#This function prints and writes the current data from each sensor module to a state CSV.
def write_state():
	data = str("%s,%3.1f,%3.1f,%d, %d" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), temp_f, rh, door, lumin))
	state = open("html/state.txt", "w")
	state.write(data + "\n")
	state.close()
	print ">> System Status:",
	print data,
	sys.stdout.flush()
	print "\r",

#*********************************************************************
#                            MAIN
#*********************************************************************
print("Executing program:")
temp_f = 70
rh = 50
door = 0
lumin = 0
t1 = threading.Thread(target = read_rh_temp, args = (4,))
t2 = threading.Thread(target = read_door, args = (17,))
t3 = threading.Thread(target = read_lumin, args = (21,))
t1.start()
t2.start()
t3.start()
while True:	
	if t1.is_alive()is False:
		del t1
		t1 = threading.Thread(target = read_rh_temp, args = (4,))
		t1.start()
	if t2.is_alive()is False:
		del t2
		t2 = threading.Thread(target = read_door, args = (17,))
		t2.start()
	if t3.is_alive()is False:
		del t3
		t3 = threading.Thread(target = read_lumin, args = (21,))
		t3.start()
	write_state()
	time.sleep(1)