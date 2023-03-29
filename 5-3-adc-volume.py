import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def binary2decimal(value):
    answer = 0
    for i in range(8):
        answer += value[i]*(2**(7 - i))
    return answer

def adc():
    a = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        GPIO.output(dac[i], 1)
        a[i] = 1
        time.sleep(0.05)
        if GPIO.input(comp) == 0:
            GPIO.output(dac[i], 0)
            a[i] = 0
    return a
    


try:
    a = [0, 0, 0, 0, 0, 0, 0, 0]
    while True: 
        voltage = binary2decimal(adc())
        number = int(voltage / 8)
        for i in range(7, 8 - number , -1):  
            a[i] = GPIO.HIGH
        for i in range(0, 8 - number):
            a[i] = GPIO.LOW
        GPIO.output(leds, a)
        time.sleep(0.001)

        if voltage != 0:
            print(f"Voltage: {voltage}")

except KeyboardInterrupt:
        print("\nProgram was stopped")
else:
    print("No exceptions")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(leds, GPIO.LOW)
    GPIO.cleanup(dac)

