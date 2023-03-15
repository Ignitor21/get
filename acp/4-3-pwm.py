import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

p = GPIO.PWM(2, 1000)
try:
    while True:
        n = int(input("Введите коэффициент заполнения: "))
        p.start(n)
finally:
    p.stop()
    GPIO.output(2, 0)
    GPIO.cleanup()