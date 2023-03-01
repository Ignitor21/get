import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2 ]

[GPIO.setup(led, GPIO.OUT) for led in leds]
[GPIO.setup(i, GPIO.IN) for i in aux]


GPIO.output(leds, 0)                                        
GPIO.cleanup()