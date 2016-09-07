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
import sqlite3
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

#Function: write_state
#This function prints and writes the current data from each sensor module to a state CSV.
def write_state():
	data = str("%s,%3.1f,%3.1f,%d,%d,%d,%d,%d" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), config.temp_f, config.rh, config.door, config.lights_red, config.lights_green, config.lights_blue, config.fan))
	state = open("html/state.txt", "w")
	state.write(data + "\n")
	state.close()
	print ">> System Status:",
	print data,
	sys.stdout.flush()
	print "\r",

#Function: write_archive
#This function writes the current data from each sensor module to a SQL database.
def write_archive():
	conn = sqlite3.connect("/home/pi/archive.db")
	curs = conn.cursor()
	curs.execute("INSERT INTO data values(date('now'), time('now'), (?), (?), (?), (?), (?), (?), (?))", (config.temp_f, config.rh, config.door, config.lights_red, config.lights_green, config.lights_blue, config.fan))
	conn.commit()
	conn.close()

#*********************************************************************
#                          HELPERS
#*********************************************************************
#Function: read_lights_red
#This function reads the data from a relay.
def read_lights_red(PIN_NUMBER):
	if read_state(int(PIN_NUMBER)) == "1":
		config.lights_red = 0
	else:
		config.lights_red = 1
	time.sleep(0.1)

#Function: read_lights_green
#This function reads the data from a relay.
def read_lights_green(PIN_NUMBER):
	if read_state(int(PIN_NUMBER)) == "1":
		config.lights_green = 0
	else:
		config.lights_green = 1
	time.sleep(0.1)

#Function: read_lights_blue
#This function reads the data from a relay.
def read_lights_blue(PIN_NUMBER):
	if read_state(int(PIN_NUMBER)) == "1":
		config.lights_blue = 0
	else:
		config.lights_blue = 1
	time.sleep(0.1)

#Function: read_fan
#This function reads the data from a relay.
def read_fan(PIN_NUMBER):
	if read_state(int(PIN_NUMBER)) == "1":
		config.fan = 0
	else:
		config.fan = 1
	time.sleep(0.1)

#Function: read_state
#This function reads the state of a relay control pin.
def read_state(PIN_NUMBER):
	output = subprocess.check_output(["gpio read %i" % (PIN_NUMBER)], shell=True)
	return str(output)[:1]