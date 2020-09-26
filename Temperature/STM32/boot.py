# This file is executed on every boot (including wake-boot from deepsleep)

# code block from original boot.py on STM32 Micropython v1.13
#import machine
#import pyb
#pyb.country('US') # ISO 3166-1 Alpha-2 code, eg US, GB, DE, AU
##pyb.main('main.py') # main script to run after this one
##pyb.usb_mode('VCP+MSC') # act as a serial and a storage device
##pyb.usb_mode('VCP+HID') # act as a serial device and a mouse


try:
    from pyb import I2C
    from pyb_i2c_lcd import I2cLcd
    #import main
    i2c = I2C(1, I2C.MASTER)
    lcd = I2cLcd(i2c, 0x27,2,16)
    lcd.putstr("Hello!")
    import time
    time.sleep(5)
    #main.main()
except:
    pass
