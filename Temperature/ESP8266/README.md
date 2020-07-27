# Temperature Sensor - ESP8266 Microcontrollers

The following code should be included in the firmware installed on your  microcontroller:
- `boot.py`: Initiates the bootup sequence for the microcontroller, including activating the USB for connection to your computer.
- `ds18x20.py`: Python driver needed to use digital temperature sensor.
- `onewire.py`: Python driver needed to use "one wire" devices such as the digital temperature sensor.
- `esp8266_i2c_lcd.py`: ESP8266 micropython driver for communicating with an LCD screen via I2C protocol.
- `lcd_api.py`: Micropython driver for writing to HD44780 character LCD screens.
- `read_temp.py`: Code for collecting and printing temperature measurements from the digital temperature sensor.

The following code should be included in your microcontroller's storage
- `main.py`: This code is run when booting to detect the digital temperature sensor and LCD screen when the microcontroller is first turned on.

For the advanced activities, you will need the following to be copied to your microcontroller's storage:
- `thermistor_calcs.py`: Calculate and return the resistance of the thermistor/resistor connected to the microcontroller's ADC pin.
