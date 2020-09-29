# Initialize microcontrollers for PublicSensors/SensoresPublicos temperature activities

from platform_defs import *

from machine import I2C
from time import sleep
from esp8266_i2c_lcd import I2cLcd

import read_temp

def main():

    sensor = read_temp.read_temp()
    sleep(1)
    try:
        i2c = I2C(scl=Pin(p_I2Cscl_lbl),sda=Pin(p_I2Csda_lbl))
        lcd = I2cLcd(i2c, 0x27,2,16)
        lcd.clear()
        lcd.putstr("Ready!\n"+chr(0)+'Listo!')
    except:
        print('LCD not registered...')

    while True:
        first = button.value()
        sleep(0.01)
        second = button.value()
        if first and not second:
            sensor.print_temp()
        elif not first and second:
            pass

main()
