#!/usr/bin/env python
import time
import subprocess
import pushbullet
import keys

time.sleep(3)
ip = subprocess.check_output(["hostname -I"], shell=True)
try:
	pb = pushbullet.Pushbullet(keys.PUSH)
	push = pb.push_sms(pb.devices[0], keys.PHONE, "EVE is online at http://" + ip)
	print("sending...")
except Exception, e:
	print("send failled...")
	print(e)