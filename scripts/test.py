#!/usr/bin/env python

import serial
from xbee import xbee

ser = serial.Serial('/dev/ttyUSB0', 9600)
while True:
    packet = xbee.find_packet(ser)
    if packet:
        xb = xbee(packet)
        print xb