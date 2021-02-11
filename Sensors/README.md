# Sensors

The code in this directory will operate for the following types of microcontrollers running Micropython:
- [**Adafruit Feather STM32F405**](https://www.adafruit.com/product/4382), which is used for all sensor kit activites on [PublicSensors](https://www.publicsensors.org)
- **ESP8266-based microcontrollers**
  - [HUZZAH Breakout](https://www.adafruit.com/product/2471)
  - [Feather HUZZAH](https://www.adafruit.com/product/2821)
- [**MicroPython pyboard v1.1**](https://www.adafruit.com/product/2390)

To conduct any of the activities on [PublicSensors](https://www.publicsensors.org), you will need the 6 `.py` files contained in this directory:
- `boot.py`
- `main.py`
- `active_sensors.py`
- `platform_defs.py`
- `esp8266_i2c_lcd.py`
- `lcd_api.py`

In addition, copy all of the `.py` files from the sensor-specific directories:
- Temperature
  - `read_temp.py`
  - `ds18x20.py`
  - `thermistor_calcs.py`
- Acoustic
  - `read_dist.py`
  - `hcsr04.py`
- Light
  - `read_light.py`
  - `tsl25x1.py`

To operate a specific sensor, you can edit `active_sensors.py`. For example, if you want to measure distance, modify the file to read:
```python
distance = 1
temperature = 0
light = 0
```
For temperature...
```python
distance = 0
temperature = 1
light = 0
```
And for light...
```python
distance = 0
temperature = 0
light = 1
```

You can also operate multiple connected sensors by simply setting more than one sensor to 1:
```python
distance = 1
temperature = 1
light = 1
```
