import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 0, 0, 0, 0, 1, 0, 1]

GPIO.setmode(GPIO.BCM)

[GPIO.setup(j, GPIO.OUT) for j in dac]

for i in range(len(dac)):
            GPIO.output(dac[i], number[i])

time.sleep(15)                                                                                                                                                                                                                                                                                                                                                  

for led in dac:
    GPIO.output(led, 0)



GPIO.cleanup()
