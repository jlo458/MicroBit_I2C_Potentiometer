from microbit import *
from machine import *

# Initialise Potentiometer
print("i2c init... code ", i2c.init())

# Scan for Devices
print("i2c scan... code ", i2c.scan())

ds3502_addr = 0x28  # Address of the DS3502 on the I2C bus

while True:
    i = 0
    while i <= 8:
        # Only activated when button A is pressed
        if button_a.is_pressed():

            reg_value = 16 * i
            # Since max value 127, cannot go above otherwise it resets to 0
            if reg_value == 128:
                reg_value -= 1
            i2c.write(ds3502_addr, bytes([0x00, reg_value]))
            sleep(1000)
            i2c.write(ds3502_addr, bytes([0]))
            print(" write value to  ", ds3502_addr, "= ", reg_value)
            nValue = i2c.read(ds3502_addr, 1)
            print(" loop read from ", ds3502_addr, "= ", nValue[0])
            i += 1
