# ----------------------
# I2C with MCP4725
# Firmware Ref Link: https://raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2
# ----------------------

# Install SMBus: sudo apt-get install python-smBus
'''
    Connections
    -----------
    VCC -> RPi Pin 1 (3.3V)
    GND -> RPi Pin 6 (GND)
    SDA -> RPi Pin 3 (I2C1 SDA)
    SCL -> RPi Pin 5 (I2C1 SCL)
'''

#import smbus
#from smbus2 import SMBus

''' 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)'''
# I2Cbus = smbus.SMBus(1)
# I2Cbus = SMBus(1)


#from smbus2 import SMBusWrapper

I2C_ADDR_RD = 0xA3
I2C_ADDR_WRT = 0xA2

Minute_Reg = 0x03
Hour_Reg = 0x04
Date_Reg = 0x05

minutes = 18
hours = 3
date = 19

rtc_minutes = 0
rtc_hours = 0
rtc_date = 0

#while(1):
from smbus2 import SMBus

with SMBus(1) as I2Cbus:
#With SMBusWrapper(1) as I2Cbus: # I2C1 bus
    print( "Sending I2C data...", end=" " )
    I2Cbus.write_byte_data(0xA2,Minute_Reg,18 )
    I2Cbus.write_byte_data(0xA2,Hour_Reg,5 )
    I2Cbus.write_byte_data(0xA2,Date_Reg,19 )
    print( "DONE" )
    sleep(.2)
    
'''	
while True:
    rtc_minutes = I2Cbus.read_byte_data(I2C_ADDR_RD, Minute_Reg )
    print(rtc_minutes)
    rtc_hours = I2Cbus.read_byte_data(I2C_ADDR_RD, Hour_Reg)
    print(rtc_hours)
    rtc_date = I2Cbus.read_byte_data(I2C_ADDR_RD, Date_Reg)
    print(rtc_date)
'''		

''' Write an array of registers '''
#ledout_values = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff]
#I2Cbus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, ledout_values)
