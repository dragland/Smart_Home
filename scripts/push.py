#!/usr/bin/env python
import subprocess
import pushbullet
import keys

ip = subprocess.check_output(["hostname -I"], shell=True)
try:
	pb = pushbullet.Pushbullet(keys.PUSH)
	push = pb.push_note("EVE is online at", "http://" + ip)
	push = pb.push_sms(pb.devices[0], keys.PHONE, "EVE is online at http://" + ip)
except:
	print(keys.PUSH + " is incorrect...")