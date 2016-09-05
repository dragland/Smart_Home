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
import subprocess
import Adafruit_DHT
import RPi.GPIO
import config

#*********************************************************************
#                          FUNCTIONS
#*********************************************************************
#Function: read_rh_temp
#This function reads the data from DHT22 AM2302 humidity and temperature sensor.
def read_rh_temp(PIN_NUMBER):
	r_h, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, PIN_NUMBER, 5, 3)
	if r_h and temp is not None:
		config.rh = r_h
		config.temp_f = temp * 1.8 + 32.0
	time.sleep(2)

#Function: read_door
#This function reads the data from a magnetic door sensor.
def read_door(PIN_NUMBER):
	RPi.GPIO.setmode(RPi.GPIO.BCM)
	RPi.GPIO.setup(PIN_NUMBER, RPi.GPIO.IN, pull_up_down = RPi.GPIO.PUD_UP)
	if RPi.GPIO.input(PIN_NUMBER):
		config.door = 1
	else:
		config.door = 0
	time.sleep(0.1)

#Function: read_lights
#This function reads the data from a relay.
def read_lights(PIN_NUMBER):
	if read_state(int(PIN_NUMBER)) == "1":
		config.lights = 0
	else:
		config.lights = 1
	time.sleep(0.1)

#Function: read_fan
#This function reads the data from a relay.
def read_fan(PIN_NUMBER):
	if read_state(int(PIN_NUMBER)) == "1":
		config.fan = 0
	else:
		config.fan = 1
	time.sleep(0.1)

#Function: read_event
#This function reads the data from a relay.
def read_event(PIN_NUMBER):
	if read_state(int(PIN_NUMBER)) == "1":
		config.event = 0
	else:
		config.event = 1
	time.sleep(0.1)

#Function: write_state
#This function prints and writes the current data from each sensor module to a state CSV.
def write_state():
	data = str("%s,%3.1f,%3.1f,%d,%d,%d,%d" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), config.temp_f, config.rh, config.door, config.lights, config.fan, config.event))
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