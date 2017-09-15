#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 3.0 | 2017

#************************************SETUP**************************************
import os
import sys
import time
import serial
import datetime
import subprocess
import sqlite3
import RPi.GPIO
import xbee
import state

#**********************************FUNCTIONS************************************
#Function: read_rh_temp
#This function reads the data from a HIH6130 humidity and temperature sensor.
def read_rh_temp():
	# TODO
	r_h = 45.1
	temp = 32
	if r_h and temp is not None:
		state.rh = r_h
		state.temp_f = temp * 1.8 + 32.0
	time.sleep(2)

#Function: read_co2
#This function reads the data from a SenseAir S8 CO2 sensor.
def read_co2():
	while True:
		ser = serial.Serial("/dev/ttyS0",baudrate =9600,timeout = .5)
		ser.flushInput()
		ser.write("\xFE\x44\x00\x08\x02\x9F\x25")
		time.sleep(0.1)
		try:
			resp = ser.read(7)
			high = ord(resp[3])
			low = ord(resp[4])
			co2Value = (high*256) + low
			state.co2 = co2Value
			break
		except:
			blank =0;

#Function: read_energy
#This function reads the data from a Kill-A-Watt P3 sensor.
def read_energy():
	xb = xbee.XBee(serial.Serial("/dev/ttyUSB0", 9600))
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
	state.energy = avgwatt

#Function: read_cpu
#This function reads the percent memory used by the CPU.
def read_cpu():
	output = subprocess.check_output(["grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'"], shell=True)
	state.cpu = str(output)[:2]

#Function: read_memory
#This function reads the percent memory available on the raspberry pi.
def read_memory():
	output = subprocess.check_output(["df -h | grep /dev/root | cut -d ' ' -f 14-"], shell=True)
	state.memory = str(output)[:2]

#Function: read_wifi
#This function reads the wifi signal quality on the raspberry pi.
def read_wifi():
	output = subprocess.check_output(["df -h | grep /dev/root | cut -d ' ' -f 14-"], shell=True)
	state.wifi = str(output)[:2]
	# output = subprocess.check_output(["iwconfig wlan0 | grep Quality | cut -d '=' -f 2 | cut -f 1 -d '/'"], shell=True)
	# # state.wifi = str(output)

#Function: read_door
#This function reads the data from a magnetic door sensor.
def read_door(PIN_NUMBER):
	RPi.GPIO.setmode(RPi.GPIO.BCM)
	RPi.GPIO.setup(PIN_NUMBER, RPi.GPIO.IN, pull_up_down = RPi.GPIO.PUD_UP)
	if RPi.GPIO.input(PIN_NUMBER):
		state.door = 1
	else:
		state.door = 0
	time.sleep(0.1)

#Function: write_state
#This function prints and writes the current data from each sensor module to a state CSV.
def write_state():
	data = str("%s,%3.1f,%3.1f,%4.0f,%4.2f,%s,%s,%s,%d,%d" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), state.temp_f, state.rh, state.co2, state.energy, state.cpu, state.memory, state.wifi, state.door, state.fan))
	stateFile = open("html/state", "w")
	stateFile.write(data + "\n")
	stateFile.close()
	print ">> System Status:",
	print data,
	sys.stdout.flush()
	print "\r",

#Function: write_archive
#This function writes the current data from each sensor module to a SQL database.
def write_archive():
	conn = sqlite3.connect("html/db/archive.db")
	curs = conn.cursor()
	curs.execute("INSERT INTO data values((?), (?), (?), (?), (?), (?), (?), (?), (?), (?))", (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "{0:.2f}".format(state.temp_f), "{0:.2f}".format(state.rh), "{0:.2f}".format(state.co2), "{0:.2f}".format(state.energy), state.cpu, state.memory, state.wifi, state.door, state.fan))
	conn.commit()
	conn.close()

#***********************************HELPERS*************************************
#Function: read_fan
#This function reads the data from a relay.
def read_fan(PIN_NUMBER):
	if read_state(int(PIN_NUMBER)) == "1":
		state.fan = 1
	else:
		state.fan = 0
	time.sleep(0.1)

#Function: read_state
#This function reads the state of a relay.
def read_state(PIN_NUMBER):
	output = subprocess.check_output(["gpio read %i" % (PIN_NUMBER)], shell=True)
	return str(output)[:1]

#Function: relay_on
#This function turns on a relay.
def relay_on(PIN_NUMBER):
	os.system("gpio mode %i out" % (PIN_NUMBER))
	os.system("gpio write %i 1" % (PIN_NUMBER))

#Function: relay_off
#This function turns off a relay.
def relay_off(PIN_NUMBER):
	os.system("gpio mode %i out" % (PIN_NUMBER))
	os.system("gpio write %i 0" % (PIN_NUMBER))

#Function: init_lights
#This function initializes the lights to the default configuration.
def init_lights():
	relay_off(5)
	print("TODO")

#Function: init_archive
#This function initializes the SQL database.
def init_archive():
	conn = sqlite3.connect("html/db/archive.db")
	curs = conn.cursor()
	curs.execute("CREATE TABLE IF NOT EXISTS data (timestamp DATETIME, temp_f NUMERIC, rh NUMERIC, co2 NUMERIC, energy NUMERIC, cpu NUMERIC, memory NUMERIC, wifi NUMERIC, door INTEGER, fan INTEGER)")
	conn.commit()
	conn.close()
