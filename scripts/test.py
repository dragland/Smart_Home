#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#*********************************************************************
#                           SETUP
#*********************************************************************
from xbee import xbee
import serial

ser = serial.Serial("/dev/ttyUSB0", 9600)
ser.isOpen()
while True:
	packet = xbee.find_packet(ser)
	if packet:
		xb = xbee(packet)
		print xb