# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
uos.dupterm(machine.UART(0, 115200), 1)
import gc
#import webrepl
#webrepl.start()
gc.collect()

try:
    from machine import I2C, Pin
    from esp8266_i2c_lcd import I2cLcd
    i2c = I2C(scl=Pin(5),sda=Pin(4))
    lcd = I2cLcd(i2c, 0x27,2,16)
    exclam_u = bytearray([0x00,0x04,0x00,0x00,0x04,0x04,0x04,0x04])
    lcd.custom_char(0,exclam_u)
    lcd.putstr('Hello\n'+chr(0)+'Hola!')
    try:
        import main
        main.main()
    except:
        lcd.clear()
        lcd.putstr("No Sensors Detected")
except:
    pass
