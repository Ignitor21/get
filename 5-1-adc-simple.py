import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    for value in range(256):
            signal = decimal2binary(value)
            GPIO.output(dac, signal)
            comparator_value = GPIO.input(comp)
            time.sleep(0.001)
            if comparator_value == 0:
                return value

try:
    while True: 
        voltage = adc()*3.3/256
        if voltage != 0:
            print(f"Voltage: {voltage}")
except KeyboardInterrupt:
        print("\nProgram was stopped")
else:
    print("No exceptions")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)

