# Acoustic (Ultrasonic) Sensor

Micropython code needed for the [Acoustic Sensor](http://www.publicsensors.org/acoustic-sensor/) activities.

The code in this directory will operate for the following types of microcontrollers running Micropython:
- [**Adafruit Feather STM32F405**](https://www.adafruit.com/product/4382), which is used for all sensor kit activites on [PublicSensors](https://www.publicsensors.org)
- **ESP8266-based microcontrollers**
  - [HUZZAH Breakout](https://www.adafruit.com/product/2471)
  - [Feather HUZZAH](https://www.adafruit.com/product/2821)
-[**MicroPython pyboard v1.1**](https://www.adafruit.com/product/2390)

To complete the temperature sensor module, copy all `.py` files onto your microcontroller. Auxillary code is included in the sensor-specific folders but is not required for any PublicSensors activities. 

Example assembly using STM32F405, 1602 I2C LCD and HCSR04 ultrasonic distance sensor:
<p align="center">
  <img src="https://raw.githubusercontent.com/publicsensors/MicrocontrollerKits/master/images/hcsr04_Battery.png" width=600>
</p>
