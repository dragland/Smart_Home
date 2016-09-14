import time
from notsmb import notSMB
I2CBUS = 1
CO2_ADDR = 0x68
READ = 0x22
readBytes = [0x00, 0x08, 0x2A]
bus = notSMB(I2CBUS)
while True:
 try:
 resp = bus.i2c(CO2_ADDR,[0x22,0x00,0x08,0x2A],4)
 time.sleep(0.1)
 #resp = bus.i2c(CO2_ADDR,[],4)
 co2Val = (resp[1]*256) + resp[2]
 print(resp)
 print(co2Val);
 break
 except:
 blank =0;