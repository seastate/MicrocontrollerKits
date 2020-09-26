# Board-specific definitions: PyBoard v1.1
from machine import Pin, UART
from pyb import Switch

p_pwr1 = Pin('X19', Pin.OUT)  # Pin X19 is power supplied to the DS18B20, V+
p_pwr2 = Pin('X18', Pin.OUT)  # Pin X18 is power supplied to the GPS, V+

p_DS18B20 = Pin('X20', Pin.IN)  # Pin X20 is the data pin for DS18B20 temperature sensors

uartGPS= UART(4, 9600)

button = Switch()  # use onbpoard USR button


'''
p_batt=14
p_sens=4
p_I2Cscl=13
p_I2Csda=12
'''
