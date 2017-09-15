#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 3.0 | 2017

#************************************SETUP**************************************
import time
import threading
import smartHome

#TODO
#DOOR SENSOR IS PIN 23
#RELAY IS PIN 24 (5 for WiringPi)

#*************************************MAIN**************************************
print("Executing program:")
smartHome.init_archive()
t1  = threading.Thread(target = smartHome.read_rh_temp)
t2  = threading.Thread(target = smartHome.read_co2)
t3  = threading.Thread(target = smartHome.read_energy)
t4  = threading.Thread(target = smartHome.read_cpu)
t5  = threading.Thread(target = smartHome.read_memory)
t6  = threading.Thread(target = smartHome.read_wifi)
t7  = threading.Thread(target = smartHome.read_door, args = (23,))
t8  = threading.Thread(target = smartHome.read_relay, args = (5,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
smartHome.init_relay(5)
smartHome.init_lights()
while True:
	if t1.is_alive() is False:
		del t1
		t1 = threading.Thread(target = smartHome.read_rh_temp)
		t1.start()
	if t2.is_alive() is False:
		del t2
		t2 = threading.Thread(target = smartHome.read_co2)
		t2.start()
	if t3.is_alive() is False:
		del t3
		t3 = threading.Thread(target = smartHome.read_energy)
		t3.start()
	if t4.is_alive() is False:
		del t4
		t4 = threading.Thread(target = smartHome.read_cpu)
		t4.start()
	if t5.is_alive() is False:
		del t5
		t5 = threading.Thread(target = smartHome.read_memory)
		t5.start()
	if t6.is_alive() is False:
		del t6
		t6 = threading.Thread(target = smartHome.read_wifi)
		t6.start()
	if t7.is_alive() is False:
		del t7
		t7 = threading.Thread(target = smartHome.read_door, args = (23,))
		t7.start()
	if t8.is_alive() is False:
		del t8
		t8 = threading.Thread(target = smartHome.read_relay, args = (5,))
		t8.start()
	smartHome.write_state()
	smartHome.write_archive()
	time.sleep(1)
