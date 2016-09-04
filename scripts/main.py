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
#Function: read_rh_temp
#This function reads the data from DHT22 AM2302 humidity and temperature sensor.
def read_rh_temp(PIN_NUMBER):
	global rh
	global temp_f
	r_h, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, PIN_NUMBER, 5, 3)
	if r_h and temp is not None:
		rh = r_h
		temp_f = temp * 1.8 + 32.0
	time.sleep(2)

#Function: read_door
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

#Function: read_lights
#This function reads the data from a relay.
def read_lights(PIN_NUMBER):
	global lights
	if read_state(int(PIN_NUMBER)) == "1":
		lights = 0
	else:
		lights = 1
	time.sleep(0.1)

#Function: read_fan
#This function reads the data from a relay.
def read_fan(PIN_NUMBER):
	global fan
	if read_state(int(PIN_NUMBER)) == "1":
		fan = 0
	else:
		fan = 1
	time.sleep(0.1)

#Function: write_state
#This function prints and writes the current data from each sensor module to a state CSV.
def write_state():
	data = str("%s,%3.1f,%3.1f,%d,%d,%d" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), temp_f, rh, door, lights, fan))
	state = open("html/state.txt", "w")
	state.write(data + "\n")
	state.close()
	print ">> System Status:",
	print data,
	sys.stdout.flush()
	print "\r",

#*********************************************************************
#                          HELPERS
#*********************************************************************
#Function to return if state is true
def read_state(PIN_NUMBER):
	output = subprocess.check_output(["gpio read %i" % (PIN_NUMBER)], shell=True)
	return str(output)[:1]

#*********************************************************************
#                            MAIN
#*********************************************************************
print("Executing program:")
temp_f = 70
rh = 50
door = 0
t1 = threading.Thread(target = read_rh_temp, args = (4,))
t2 = threading.Thread(target = read_door, args = (17,))
t3 = threading.Thread(target = read_lights, args = (2,))
t4 = threading.Thread(target = read_fan, args = (3,))
t1.start()
t2.start()
t3.start()
t4.start()
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
		t3 = threading.Thread(target = read_lights, args = (2,))
		t3.start()
	if t4.is_alive()is False:
		del t4
		t4 = threading.Thread(target = read_fan, args = (3,))
		t4.start()
	write_state()
	time.sleep(1)