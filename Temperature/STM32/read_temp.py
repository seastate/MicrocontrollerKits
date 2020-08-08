# This script prints temperature readings from a DS18B20 sensor

from machine import Pin
from pyb import I2C
from pyb_i2c_lcd import I2cLcd
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep_ms

# -------------------------------------------------------------------------------
# Set up pins for the DS18B20
# -------------------------------------------------------------------------------
class read_temp:

    def __init__(self):
        p12 = Pin('D10', Pin.OUT)  # Pin 12 is power supplied to the DS18B20, V+
        p12.value(1)            # set Pin 12 to 3V

        #p14 = Pin(14, Pin.OUT)  # Pin 14 is GND for the DS18B20
        #p14.value(0)            # Set Pin 14 to 0V

        ow = OneWire(Pin('D9'))   # Pin 13 is the data pin for the DS18B20
        self.ds = DS18X20(ow)        # Initialize a ds18b20 object
        self.roms = self.ds.scan()   # Find all the DS18B20 sensors that are attached (we only have one)

    # -------------------------------------------------------------------------------
    # Progression for obtaining temperature readings from the sensor
    # -------------------------------------------------------------------------------

    def print_temp(self):
        i2c = I2C(1, I2C.MASTER)
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
    def print_temps_start(self,samp_max=1000):
        i2c = I2C(1, I2C.MASTER)
        try:
            lcd = I2cLcd(i2c, 0x27,2,16)
            lcdF = 1
        except:
            lcdF = 0
        sample_num=1            # Start sample number at 0 so we can count the number of samples we take
        while sample_num <= samp_max:            # This will repeat in a loop, until we terminate with a ctrl-c
            self.ds.convert_temp()   # Obtain a temperature reading
            sleep_ms(1000)      # Sleep for 1 sec
            print("Sample: ",sample_num, ',', self.ds.read_temp(self.roms[0]), ' C') # print the sample number and temperature
            print("\n")         # Print a line of space between temp readings so it is easier to read
            if lcdF ==1:
                lcd.clear()      # Sleep for 1 sec
                lcd.putstr("Sample: "+str(sample_num)+"\nTemp: "+str(round(self.ds.read_temp(self.roms[0]),2))+" C")
            sleep_ms(4000)      # Wait 5 sec, before repeating the loop and taking another reading
            sample_num+=1       # Increment the sample number for each reading
        if lcdF == 1:
            lcd.clear()
            lcd.putstr("Done!")
            sleep_ms(2000)
            lcd.clear()
