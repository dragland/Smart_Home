#!/usr/bin/env python

import serial
from xbee import XBee

ser = serial.Serial('/dev/ttyUSB0', 9600)
xbee = XBee(ser)

while True:
    try:
        print xbee.wait_read_frame()
    except KeyboardInterrupt:
        break

serial_port.close()