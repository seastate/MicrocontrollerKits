import machine, time
from pyb import I2C
from pyb_i2c_lcd import I2cLcd
import hcsr04

def main():
    button = machine.Pin('D13', machine.Pin.IN, machine.Pin.PULL_UP)
    sensor = hcsr04.HCSR04(trigger_pin = 'D10', echo_pin = 'D9', c = 343)
    time.sleep(1)
    i2c = I2C(1, I2C.MASTER)
    lcd = I2cLcd(i2c, 0x27,2,16)
    lcd.clear()
    lcd.putstr("Ready for\nDistance!")
    while True:
        first = button.value()
        time.sleep(0.01)
        second = button.value()
        if first and not second:
            dist = sensor.distance() # return is in cm
            lcd.clear()
            lcd.putstr(str(dist)+" cm")
            print(str(dist)+" cm")
        elif not first and second:
            pass
