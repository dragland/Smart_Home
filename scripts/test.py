#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#*********************************************************************
#                           SETUP
#*********************************************************************
from xbee import xbee
import serial

ser = serial.Serial("/dev/ttyUSB0", 9600)
ser.open()
 
while True:
    # grab one packet from the xbee, or timeout
    packet = xbee.find_packet(ser)
    if packet:
        xb = xbee(packet)
 
        print xb