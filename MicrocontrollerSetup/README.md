# Microcontroller Setup

The code for this repository is based on the use of the [Feather STM32](https://www.adafruit.com/product/4382) microcontroller. The following are additional resources for working with these microcontrollers:
- [Pin Identifiers](https://github.com/micropython/micropython/blob/master/ports/stm32/boards/ADAFRUIT_F405_EXPRESS/pins.csv)
- [Using the STM32 with Micropython](https://learn.adafruit.com/adafruit-stm32f405-feather-express/micropython-setup)

All of the code for the activites uses MicroPython v1.13, available directly from [MicroPython.org](https://micropython.org/download/) and provided here as `firmware.dfu`. Instructions are provided for installing using a [DFU bootloader](https://learn.adafruit.com/adafruit-stm32f405-feather-express/dfu-bootloader-details), either using a GUI (such as [STM32CubeProg](https://www.st.com/en/development-tools/stm32cubeprog.html)) or command line ([dfu-util](http://dfu-util.sourceforge.net/)) available for Windows, Mac, and Linux.

To use dfu-util:
1. Download [dfu-util](http://dfu-util.sourceforge.net/) from sourceforge.
2. Connect your microcontroller to your computer via USB in bootloader mode. For the Feather STM32, this involves connecting the **B0** pin to either of the **3.3V** pins, then connecting to your computer via USB.
3. In a terminal/command window, navigate to the dfu-util directory.
4. You can confirm that your microcontroller is detected by dfu-util using
```
dfu-util -l
```
5. To update the firmware on the microcontroller, you can use the following syntax (note, `firmware.dfu` should be the complete path of the file):
```
dfu-util -a 0 -D firmware.dfu
```
