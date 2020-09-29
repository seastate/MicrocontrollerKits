# This file is executed on every boot (including wake-boot from deepsleep)

try:
    from pyb import I2C
    from pyb_i2c_lcd import I2cLcd
    import main
    i2c = I2C(1, I2C.MASTER)
    lcd = I2cLcd(i2c, 0x27,2,16)
    lcd.putstr("Hello!")
    import time
    time.sleep(5)
    main.main()
except:
    pass
