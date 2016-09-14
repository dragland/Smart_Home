#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#*********************************************************************
#                           SETUP
#*********************************************************************
import time 
import threading
import smartHome

#*********************************************************************
#                            MAIN
#*********************************************************************
print("Executing program:")
smartHome.init_archive()
t1 = threading.Thread(target = smartHome.read_rh_temp, args = (4,))
t2 = threading.Thread(target = smartHome.read_door, args = (18,))
t3 = threading.Thread(target = smartHome.read_lights_red, args = (0,))
t4 = threading.Thread(target = smartHome.read_lights_green, args = (2,))
t5 = threading.Thread(target = smartHome.read_lights_blue, args = (3,))
t6 = threading.Thread(target = smartHome.read_fan, args = (4,))
t7 = threading.Thread(target = smartHome.read_co2)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
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
		t3 = threading.Thread(target = smartHome.read_lights_red, args = (0,))
		t3.start()
	if t4.is_alive()is False:
		del t4
		t4 = threading.Thread(target = smartHome.read_lights_green, args = (2,))
		t4.start()
	if t5.is_alive()is False:
		del t5
		t5 = threading.Thread(target = smartHome.read_lights_blue, args = (3,))
		t5.start()
	if t6.is_alive()is False:
		del t6
		t6 = threading.Thread(target = smartHome.read_fan, args = (4,))
		t6.start()
	if t7.is_alive()is False:
		del t7
		t7 = threading.Thread(target = smartHome.read_co2)
		t7.start()
	smartHome.automate(4)
	smartHome.write_state()
	smartHome.write_archive()
	time.sleep(1)