#!/usr/bin/env python
import subprocess
import pushbullet
import keys

import os
import datetime
filename = '/var/www/html/log.txt'
if os.path.exists(filename):
    append_write = 'a'
else:
    append_write = 'w'
f = file = open(filename,append_write)
f.write(str(datetime.datetime.now()))

ip = subprocess.check_output(["hostname -I"], shell=True)
f.write(ip)
try:
	pb = pushbullet.Pushbullet(keys.PUSH)
	push = pb.push_sms(pb.devices[0], keys.PHONE, "EVE is online at http://" + ip)
	print("sending...")
	f.write("sending...\n")
except:
	print(keys.PUSH + " is incorrect...")
	f.write("send failled...\n")
f.write("done...\n")
f.close()