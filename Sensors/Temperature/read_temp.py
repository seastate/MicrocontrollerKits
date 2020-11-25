# This script prints temperature readings from a DS18B20 sensor

# Import platform-specific definitions
from platform_defs import *

from machine import Pin, I2C
from esp8266_i2c_lcd import I2cLcd
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep_ms


# -------------------------------------------------------------------------------
# Set up pins for the DS18B20
# -------------------------------------------------------------------------------
class read_temp:

    def __init__(self):
        p_pwr1.value(1)

        ow = OneWire(p_DS18B20)   # Pin 13 is the data pin for the DS18B20
        self.ds = DS18X20(ow)        # Initialize a ds18b20 object
        self.roms = self.ds.scan()   # Find all the DS18B20 sensors that are attached (we only have one)

    # -------------------------------------------------------------------------------
    # Progression for obtaining temperature readings from the sensor
    # -------------------------------------------------------------------------------

    def print_temp(self):
        i2c = I2C(scl=Pin(p_I2Cscl_lbl),sda=Pin(p_I2Csda_lbl))
        try:
            lcd = I2cLcd(i2c, 0x27,2,16)
            lcdF = 1
        except:
            lcdF = 0
        self.ds.convert_temp()       # Obtain temp readings from each of those sensors
        sleep_ms(750)           # Sleep for 750 ms, to give the sensors enough time to report their temperature readings
        print(self.ds.read_temp(self.roms[0]), ' C')
        if lcdF == 1:
            lcd.clear()      # Sleep for 1 sec
            lcd.putstr("Temp: "+str(round(self.ds.read_temp(self.roms[0]),2))+" C")

    # -------------------------------------------------------------------------------
    # Get continuous temperature measurements
    # -------------------------------------------------------------------------------
    def print_temps_start(self,samp_max=1000,interval=5):
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
            self.ds.convert_temp()   # Obtain a temperature reading
            sleep_ms(pause_microsec)      # Sleep for 1 sec
            print("Sample: ",sample_num, ',', self.ds.read_temp(self.roms[0]), ' C') # print the sample number and temperature
            print("\n")         # Print a line of space between temp readings so it is easier to read
            if lcdF ==1:
                lcd.clear()      # Sleep for 1 sec
                lcd.putstr("Sample: "+str(sample_num)+"\nTemp: "+str(round(self.ds.read_temp(self.roms[0]),2))+" C")
            sleep_ms(max(sleep_microsec-pause_microsec,0))      # Wait 5 sec, before repeating the loop and taking another reading
            sample_num+=1       # Increment the sample number for each reading
        if lcdF == 1:
            lcd.clear()
            lcd.putstr("Done!")
            sleep_ms(2000)
            lcd.clear()



            
