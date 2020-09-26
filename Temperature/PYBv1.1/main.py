import machine
import time
import read_temp
from pyb import I2C
from pyb_i2c_lcd import I2cLcd


def main():
    button = machine.Pin('D13', machine.Pin.IN, machine.Pin.PULL_UP)
    sensor = read_temp.read_temp()
    time.sleep(1)
    i2c = I2C(1, I2C.MASTER)
    lcd = I2cLcd(i2c, 0x27,2,16)
    lcd.clear()
    lcd.putstr("Ready!")
    while True:
        first = button.value()
        time.sleep(0.01)
        second = button.value()
        if first and not second:
            sensor.print_temp()
        elif not first and second:
            pass
