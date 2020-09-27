#  Definitions of platform-specific pins and commands.
# 
#  Currently supported boards are: STM32f405 Feather, ESP8266 Huzzah Feather/Breakout Board, Pyboard v1.1

# Detect platform via uos command
from uos import uname
sys_info = uname()
print(sys_info)
platform=sys_info[4]


if platform.find('Adafruit Feather STM32F405 with STM32F405RG')>-1:  # Board-specific definitions: STM32f405 Feather
    
    print('Loading definitions for STM32 Feather')
    from machine import Pin, UART

    p_pwr1 = Pin('D9', Pin.OUT)  # Pin 12 is power supplied to the DS18B20, V+
    #p_pwr2 = Pin('X18', Pin.OUT)  # Pin X18 is power supplied to the GPS, V+
    p_DS18B20 = Pin('D10', Pin.IN)  # Pin X20 is the data pin for DS18B20 temperature sensors
    #uartGPS= UART(4, 9600)
    button = Pin('D13', Pin.IN, Pin.PULL_UP)

elif platform.find('ESP module with ESP8266')>-1:  # Board-specific definitions: ESP8266 Huzzah Feather/Breakout Board
    print('Loading definitions for ESP8266')


elif platform.find('PYBv1.1 with STM32F405RG')>-1:  # Board-specific definitions: Pyboard v1.1

    print('Loading definitions for PYBv1.1')
    from machine import Pin, UART
    from pyb import Switch

    p_pwr1 = Pin('X19', Pin.OUT)  # Pin X19 is power supplied to the DS18B20, V+
    p_pwr2 = Pin('X18', Pin.OUT)  # Pin X18 is power supplied to the GPS, V+
    p_DS18B20 = Pin('X20', Pin.IN)  # Pin X20 is the data pin for DS18B20 temperature sensors
    uartGPS= UART(4, 9600)
    button = Switch()  # use onboard USR button
    #p_batt=14
    #p_sens=4
    #p_I2Cscl=13
    #p_I2Csda=12


'''
(sysname='pyboard', nodename='pyboard', release='1.13.0', version='v1.13-53-gc20075929-dirty on 2020-09-21', machine='Adafruit Feather STM32F405 with STM32F405RG')

(sysname='esp8266', nodename='esp8266', release='2.2.0-dev(9422289)', version='v1.9.4-701-g10bddc5c2 on 2019-01-17', machine='ESP module with ESP8266')
(sysname='pyboard', nodename='pyboard', release='1.13.0', version='v1.13 on 2020-09-02', machine='PYBv1.1 with STM32F405RG')
'''

