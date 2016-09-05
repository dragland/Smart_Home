#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#*********************************************************************
#                           SETUP
#*********************************************************************
import time
import threading
import smartHome
import config

#*********************************************************************
#                            MAIN
#*********************************************************************
print("Executing program:")
t1 = threading.Thread(target = smartHome.read_rh_temp, args = (4,))
t2 = threading.Thread(target = smartHome.read_door, args = (18,))
t3 = threading.Thread(target = smartHome.read_lights, args = (2,))
t4 = threading.Thread(target = smartHome.read_fan, args = (3,))
t4 = threading.Thread(target = smartHome.read_event, args = (0,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
while True:	
	if t1.is_alive()is False:
		del t1
		t1 = threading.Thread(target = smartHome.read_rh_temp, args = (4,))
		t1.start()
	if t2.is_alive()is False:
		del t2
		t2 = threading.Thread(target = smartHome.read_door, args = (18,))
		t2.start()
	if t3.is_alive()is False:
		del t3
		t3 = threading.Thread(target = smartHome.read_lights, args = (2,))
		t3.start()
	if t4.is_alive()is False:
		del t4
		t4 = threading.Thread(target = smartHome.read_fan, args = (3,))
		t4.start()
	if t5.is_alive()is False:
		del t5
		t5 = threading.Thread(target = smartHome.read_event, args = (0,))
		t5.start()
	smartHome.write_state()
	time.sleep(1)