#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 4.0 | 2018

#*********************************** SETUP *************************************
import time
import threading
import smartHome

#**************************** Raspberry Pi Pinout ******************************
DOOR_PIN = 23
RELAY_PIN = 5

#************************************ MAIN *************************************
print("Executing program:")
smartHome.push_alert(smartHome.read_ip)
smartHome.init_archive()
t1  = threading.Thread(target = smartHome.read_rh_temp)
t2  = threading.Thread(target = smartHome.read_co2)
t3  = threading.Thread(target = smartHome.read_energy)
t4  = threading.Thread(target = smartHome.read_cpu)
t5  = threading.Thread(target = smartHome.read_memory)
t6  = threading.Thread(target = smartHome.read_wifi)
t7  = threading.Thread(target = smartHome.read_door, args = (DOOR_PIN,))
t8  = threading.Thread(target = smartHome.read_relay, args = (RELAY_PIN,))
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
		t7 = threading.Thread(target = smartHome.read_door, args = (DOOR_PIN,))
		t7.start()
	if t8.is_alive() is False:
		del t8
		t8 = threading.Thread(target = smartHome.read_relay, args = (RELAY_PIN,))
		t8.start()
	smartHome.write_state()
	smartHome.write_archive()
	time.sleep(1)
