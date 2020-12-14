# Initialize microcontrollers for PublicSensors/SensoresPublicos temperature activities

from platform_defs import *
import active_sensors

from sys import print_exception
from machine import I2C
from time import sleep
from esp8266_i2c_lcd import I2cLcd

def main():
    global sensor # use a global variable to fix global vs. local namespace issues
    num_sensors=0  # number of sensors successfuly initialized
    activeNames, activeFuncs, sensors =  [[] for i in range(3)]  # Lists for when we are going to use multiple sensors
    #activeNames = []
    #activeFuncs = []
    #sensors = []
    sensorFuncs = {'light': 'light', 'distance': 'dist', 'temperature': 'temp', 'GPS': 'GPS'}
    for sensr in [item for item in dir(active_sensors) if not item.startswith("__")]:
        if eval('active_sensors.'+sensr) == 1:
            try:
                activeName = sensr
                activeFunc = sensorFuncs[sensr]
                exec('import read_'+activeFunc)
                sensor = eval('read_'+activeFunc+'.read_'+activeFunc+'()')
                sleep(1)
                print('success: queuing sensor driver ',activeFunc)
                num_sensors+=1
                activeNames.append(activeName)
                activeFuncs.append(activeFunc)
                sensors.append(sensor)
            except:
                print('Error: sensor driver ',activeFunc,' was requested but failed to load')
    try:
        i2c = I2C(scl=Pin(p_I2Cscl_lbl),sda=Pin(p_I2Csda_lbl))
        lcd = I2cLcd(i2c, 0x27,2,16)
        lcd.clear()
        lcd.scrollstr('Preparing to measure '+', '.join(activeNames))
        lcd.clear()
        lcd.putstr("Ready!\n"+chr(0)+'Listo!')

        i=0
        while True:
            first = button.value()
            sleep(0.01)
            second = button.value()
            if first and not second:
                sensor=sensors[i]
                exec('sensor.print_'+activeFuncs[i]+'()')
                i = (i+1) % num_sensors
            elif not first and second:
                pass
    except Exception as e:
        print_exception(e)
        print('LCD not registered...')


main()
