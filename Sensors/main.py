# Initialize microcontrollers for PublicSensors/SensoresPublicos temperature activities

from platform_defs import *
try:
    import active_sensors
    asFlag = 1
except:
    asFlag = 0

from sys import print_exception
from machine import I2C
from time import sleep
from esp8266_i2c_lcd import I2cLcd

def main():
    global sensor # use a global variable to fix global vs. local namespace issues
    activeNames, activeFuncs, sensors =  [[] for i in range(3)]  # Lists for when we are going to use multiple sensors
    sensorFuncs = {'light': 'light', 'distance': 'dist', 'temperature': 'temp', 'GPS': 'GPS'}
    for sensr in ['GPS','distance','light','temperature']: # lets try talking to all the sensors
            try:
                activeName = sensr
                activeFunc = sensorFuncs[sensr]
                exec('import read_'+activeFunc)
                sensor = eval('read_'+activeFunc+'.read_'+activeFunc+'()')
                sleep(1)
                print('success: queuing sensor driver ',activeFunc)
                exec('sTest = sensor.test_'+activeFunc+'()')
                if sTest:
                    activeNames.append(activeName)
                    activeFuncs.append(activeFunc)
                    sensors.append(sensor)
                    print('success: able to make measurement using ',activeFunc)
                else:
                    print('Error: unable to connect to ',activeFunc, ' sensor')
            except:
                print('Error: sensor driver ',activeFunc,' was requested but failed to load')

    if asFlag ==1:
        activeList = [s for s in [item for item in dir(active_sensors) if not item.startswith("__")] if eval('active_sensors.'+s) == 1]
        activeNamesMeasure = [k for k in activeList if (k inactive Names) and (k in activeList)] # check which from the active list work
        activeIndex = [activeNames.index(k) for k in activeNamesMeasure] # get the index of the active & good sensors
        activeFuncs = [activeFuncs[k] for k in activeIndex] # use the index to get the good and active funcs
        sensors = [sensors[k] for k in activeIndex] # get the good and active sensor objects
    else: # if no active_sensors, use all the sensors found and the original lists as above
        activeNamesMeasure = activeNames
    try:
        i2c = I2C(scl=Pin(p_I2Cscl_lbl),sda=Pin(p_I2Csda_lbl))
        lcd = I2cLcd(i2c, 0x27,2,16)
        lcd.clear()
        lcd.scrollstr('Found the following sensors: '+', '.join(activeNames))
        lcd.clear()
        lcd.scrollstr('Preparing to measure: '+', '.join(activeNamesMeasure))
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
                i = (i+1) % len(activeNamesMeasure)
            elif not first and second:
                pass
    except Exception as e:
        print_exception(e)
        print('LCD not registered...')


main()
