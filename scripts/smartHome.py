#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#*********************************************************************
#                           SETUP
#*********************************************************************
import os
import sys
import time
import serial
import datetime
import subprocess
import sqlite3
import Adafruit_DHT
import RPi.GPIO
import notsmb
import xbee
import config

#*********************************************************************
#                          FUNCTIONS
#*********************************************************************
#Function: read_rh_temp
#This function reads the data from a DHT22 AM2302 humidity and temperature sensor.
def read_rh_temp(PIN_NUMBER):
	r_h, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, PIN_NUMBER, 5, 3)
	if r_h and temp is not None:
		config.rh = r_h
		config.temp_f = temp * 1.8 + 32.0
	time.sleep(2)

#Function: read_co2
#This function reads the data from a K-30 CO2 sensor.
def read_co2():
	READ = 0x22
	readBytes = [0x00, 0x08, 0x2A]
	while True:
		try:
			resp = notsmb.notSMB(1).i2c(0x68,[0x22,0x00,0x08,0x2A],4)
			time.sleep(0.1)
			co2Value = (resp[1]*256) + resp[2]
			if co2Value < 2000:
				config.co2 = co2Value
				break
		except:
			blank =0;

#Function: read_energy
#This function reads the data from a Kill-A-Watt P3 sensor.
def read_energy():
	xb = xbee.XBee(serial.Serial("/dev/ttyUSB0", 9600))
	while True:
	    packet = xb.wait_read_frame()
	    voltagedata = [-1] * (len(packet["samples"]) - 1)
		ampdata = [-1] * (len(packet["samples"]) - 1)
		for i in range(len(voltagedata)):
			voltagedata[i] = packet["samples"][i + 1]["adc-0"]
			ampdata[i] = packet["samples"][i + 1]["adc-0"] 
		min_v = 1024
		max_v = 0
		for i in range(len(voltagedata)):
		    if (min_v > voltagedata[i]):
		        min_v = voltagedata[i]
		    if (max_v < voltagedata[i]):
		        max_v = voltagedata[i]
		avgv = (max_v + min_v) / 2
		vpp =  max_v - min_v
		for i in range(len(voltagedata)):
		    voltagedata[i] -= avgv
		    voltagedata[i] = (voltagedata[i] * 340) / vpp
		for i in range(len(ampdata)):
		    ampdata[i] -= 470
		    ampdata[i] /= 15.5 
		wattdata = [0] * len(voltagedata)
		for i in range(len(wattdata)):
		    wattdata[i] = voltagedata[i] * ampdata[i]
		avgamp = 0
		for i in range(17):
		    avgamp += abs(ampdata[i])
		avgamp /= 17.0
		avgwatt = 0
		for i in range(17):         
		    avgwatt += abs(wattdata[i])
		avgwatt /= 17.0
		config.energy = avgwatt
		    
#Function: read_cpu
#This function reads the percent memory used by the CPU.
def read_cpu():
	output = subprocess.check_output(["grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'"], shell=True)
	config.cpu = str(output)[:2]

#Function: read_memory
#This function reads the percent memory available on the raspberry pi.
def read_memory():
	output = subprocess.check_output(["df -h | grep /dev/root | cut -d ' ' -f 14-"], shell=True)
	config.memory = str(output)[:2]

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
	data = str("%s,%3.1f,%3.1f,%4.0f,%4.2f,%s,%s,%d,%d,%d,%d,%d" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), config.temp_f, config.rh, config.co2, config.energy, config.cpu, config.memory, config.door, config.fan, config.lights_red, config.lights_green, config.lights_blue))
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
	conn = sqlite3.connect("html/archive.db")
	curs = conn.cursor()
	curs.execute("INSERT INTO data values((?), (?), (?), (?), (?), (?), (?), (?), (?), (?), (?), (?))", (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "{0:.2f}".format(config.temp_f), "{0:.2f}".format(config.rh), "{0:.2f}".format(config.co2), "{0:.2f}".format(config.energy), config.cpu, config.memory, config.door, config.fan, config.lights_red, config.lights_green, config.lights_blue))
	conn.commit()
	conn.close()

#Function: automate
#This function automates the relay control based on setpoint values.
def automate(PIN_NUMBER):
	if config.temp_f > 80:
		relay_on(int(PIN_NUMBER))
	if config.temp_f < 40:
		relay_off(int(PIN_NUMBER))

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

#Function: init_archive
#This function initializes the SQL database.
def init_archive():
	conn = sqlite3.connect("html/archive.db")
	curs = conn.cursor()
	curs.execute("CREATE TABLE IF NOT EXISTS data (timestamp DATETIME, temp_f NUMERIC, rh NUMERIC, co2 NUMERIC, energy NUMERIC, cpu NUMERIC, memory NUMERIC, door INTEGER, fan INTEGER, lights_red INTEGER, lights_green INTEGER, lights_blue INTEGER)")
	conn.commit()
	conn.close()