



from platform_defs import *

from machine import I2C, Pin
from time import sleep
from esp8266_i2c_lcd import I2cLcd



def read_light():
    # Wrapper function to synonymize calls to TSL2561 and SL2591 light sensors
    try:
        import tsl2591DG as tsl2591
        tsl = tsl2591.Tsl2591()  # initialize
        full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum and ir spectrum)
        lux = tsl.calculate_lux(full, ir)  # convert raw values to lux
        print('tsl2591 lux, full, ir:',lux, full, ir)
    except:
        pass

    try:
        import tsl2561
        i2c = I2C(scl=Pin(p_I2Cscl_lbl), sda=Pin(p_I2Csda_lbl),freq=50000)
        sensor = tsl2561.TSL2561(i2c)
        full, ir = sensor.read(raw=True)
        lux=sensor._lux((full,ir))
        print('tsl2561 lux, full, ir:',lux, full, ir)
    except:
        pass
