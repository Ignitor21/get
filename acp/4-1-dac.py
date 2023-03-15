import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

try:
    while(1):
        n = input("Введите целое число или q для завершения программы: ")

        if n == "q":
            break
        elif not n.isdecimal():
            print("Введите целое число!")
            continue
        elif int(n) < 0 or int(n) > 255:
            print("Введите число от 0 до 255 включительно!")
            continue
        elif not is_int(n):
            print("Введите целое число!")
            continue
        else:
            n = int(n)
            
        voltage = (n/2**8) * 3.3
        print("Напряжение на выходе равно:", voltage)
        GPIO.output(dac, decimal2binary(n))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()