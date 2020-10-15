from pyb import Pin, ADC

def print_resistance():
  adc = ADC(Pin('A2')) # Identify the pin to measure V2
  V1 = 3.3 # Set V1 to 3.3 Volts since we're using the '3.3V' pin to power the circuit
  V2 = adc.read()/1024.0 # Set V2 to the voltage measured by the A2 pin
  R1 = 220000 # Set R1 as the 220 KOhm resistor at the beginning of our circuit
  R2 = (V2/(V1-V2))*R1 # solve for the resistance of R2 (thermistor) using Ohm's Law
  print(V2, ' Volts, ',R2,' Ohms')
