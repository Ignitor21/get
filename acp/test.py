import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 0.5)
p.start(50)
input('Press return to stop:')   # use raw_input for Python 2
p.stop()
GPIO.cleanup()