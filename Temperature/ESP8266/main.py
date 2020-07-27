import machine
import time
import read_temp

def main():
    button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
    sensor = read_temp.read_temp()
    while True:
        first = button.value()
        time.sleep(0.01)
        second = button.value()
        if first and not second:
            sensor.print_temp()
        elif not first and second:
            pass
