# This script prints temperature readings from a DS18B20 sensor

# Import platform-specific definitions
from platform_defs import *

from machine import Pin, I2C
from esp8266_i2c_lcd import I2cLcd
from tsl25x1 import tsl25x1_sensor #, TSL2561, Tsl2591, read_tsl25x1
from time import sleep_ms

# -------------------------------------------------------------------------------
# Set up pins for the light sensors; power from either Vbat or p_pwr1 pin (defined in platform_defs)
# -------------------------------------------------------------------------------
class read_light:

    def __init__(self):
        p_pwr1.value(1)

        # Wrapper function to synonymize calls to TSL2561 and TSL2591 light sensors
        self.sensor = tsl25x1_sensor()

    # -------------------------------------------------------------------------------
    # Progression for obtaining light readings from the sensor
    # -------------------------------------------------------------------------------

    def print_light(self):
        i2c = I2C(scl=Pin(p_I2Cscl_lbl),sda=Pin(p_I2Csda_lbl))
        try:
            lcd = I2cLcd(i2c, 0x27,2,16)
            lcdF = 1
        except:
            lcdF = 0
        full, ir, lux = self.sensor.light()
        print('full: ',str(full),' ir: ',str(ir))
        if lcdF == 1:
            lcd.clear()      # Sleep for 1 sec
            lcd.putstr('full: '+str(full)+'\nir: '+str(ir))

    # -------------------------------------------------------------------------------
    # Get continuous light measurements
    # -------------------------------------------------------------------------------
    def print_light_start(self,samp_max=1000,interval=5):
        sleep_microsec=int(1000*interval)
        pause_microsec=1000
        i2c = I2C(scl=Pin(p_I2Cscl_lbl),sda=Pin(p_I2Csda_lbl))
        try:
            lcd = I2cLcd(i2c, 0x27,2,16)
            lcdF = 1
        except:
            lcdF = 0
        sample_num=1            # Start sample number at 0 so we can count the number of samples we take
        while sample_num <= samp_max:            # This will repeat in a loop, until we terminate with a ctrl-c
            full, ir, lux  = self.sensor.light()   # Obtain a distance reading
            sleep_ms(pause_microsec)      # Sleep for 1 sec
            print("Sample: ",sample_num, ', full: ',str(full),' ir: ',str(ir)) # print the sample number and distance
            print("\n")         # Print a line of space between temp readings so it is easier to read
            if lcdF ==1:
                lcd.clear()      # Sleep for 1 sec
                lcd.putstr("# "+str(sample_num)+' full,ir=\n'+str(full)+','+str(ir))
            sleep_ms(max(sleep_microsec-pause_microsec,0))      # Wait 5 sec, before repeating the loop and taking another reading
            sample_num+=1       # Increment the sample number for each reading
        if lcdF == 1:
            lcd.clear()
            lcd.putstr("Done!")
            sleep_ms(2000)
            lcd.clear()
