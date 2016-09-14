#Python app to run a K-30 Sensor
import serial
import time
ser = serial.Serial("/dev/ttyAMA0")
print "Serial Connected!"
ser.flushInput()
time.sleep(1)

while True:
    ser.write("\xFE\x44\x00\x08\x02\x9F\x25")
    time.sleep(.01)
    resp = ser.read(7)
    high = ord(resp[3])
    low = ord(resp[4])
    co2 = (high*256) + low
    print ""
    print ""
    print "Co2 = " + str(co2)
    time.sleep(1)

