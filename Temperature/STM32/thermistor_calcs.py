import machine

def print_resistance():
  adc = machine.Pin('A2') # Identify the ADC pin
  V1 = 3 # Set V1 to 3 Volts since we're using our '3V' pin to power the circuit
  V2 = adc.read()/1024.0 # Set V2 to the current voltage at the ADC pin
  R1 = 220000 # Set R1 as the 220 KOhm resistor at the beginning of our circuit
  R2 = (V2/(V1-V2))*R1 # Solve for the resistance of R2 (thermistor) using Ohm's Law
  print(V2, ' Volts, ',R2,' Ohms')
