import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

while True:
    incoming = ser.readline().strip()
    print 'Received %s' % incoming
    ser.write('RPi Received: %s\n' % incoming)