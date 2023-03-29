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
    while True: 
        voltage = binary2decimal(adc())*3.3/256
        if voltage != 0:
            print(f"Voltage: {voltage}")
except KeyboardInterrupt:
        print("\nProgram was stopped")
else:
    print("No exceptions")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)

