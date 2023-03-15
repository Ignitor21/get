import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        T = 2
        for i in range(256):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(T/512)
        for i in range(255, -1, -1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(T/512)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)