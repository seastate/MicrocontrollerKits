# Initialize microcontrollers for PublicSensors/SensoresPublicos temperature activities

from platform_defs import *

from machine import I2C
from time import sleep
from esp8266_i2c_lcd import I2cLcd
import active_sensors

def main():
    #activeName, activeFuncs =  [[] for i in range(2)] For when we are going to use multiple sensors
    sensorFuncs = {'light': 'light', 'distance': 'dist', 'temperature': 'temp', 'GPS': 'GPS'}
    for sensr in [item for item in dir(active_sensors) if not item.startswith("__")]:
        if eval('active_sensors.'+sensr) == 1:
            activeName = sensr
            activeFuncs = sensorFuncs[sensr]
    exec('import read_'+activeFuncs)
    exec('sensor = read_'+activeFuncs+'.read_'+activeFuncs+'()')
    sleep(1)
    try:
        i2c = I2C(scl=Pin(p_I2Cscl_lbl),sda=Pin(p_I2Csda_lbl))
        lcd = I2cLcd(i2c, 0x27,2,16)
        lcd.clear()
        lcd.scrollstr('Preparing to measure '+activeName)
        lcd.clear()
        lcd.putstr("Ready!\n"+chr(0)+'Listo!')

        while True:
            first = button.value()
            sleep(0.01)
            second = button.value()
            if first and not second:
                exec('sensor.print_'+activeFuncs+'()')
            elif not first and second:
                pass
    except:
        print('LCD not registered...')

main()
