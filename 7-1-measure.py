import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

#Переводит десятичное число в двоичное
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
#Выводит двоичное представление числа в блоке светодиодов
def num2led(value):
    signal = decimal2binary(value)
    GPIO.output(leds, signal)
    return signal

#Считывет напряжение с тройка модуля
# def adc():
#     for value in range(256):
#         signal = decimal2binary(value)
#         GPIO.output(dac, signal)
#         time.sleep(0.01)
#         comparator_value = GPIO.input(comp)
#         if comparator_value == 0:
#             return value

def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        GPIO.output(dac, decimal2binary(k))
        time.sleep(0.01)
        comp_val = GPIO.input(comp)
        if (comp_val == 0):
            k -= 2**i
    return k

try:
    adc_value_list = []
    adc_value = 0
    GPIO.output(troyka, GPIO.HIGH)
    start = time.time()

    while (adc_value < 50):
        adc_value = adc()
        print("Voltage:", adc_value)
        adc_value_list.append(adc_value)
        GPIO.output(leds, num2led(adc_value))

    GPIO.output(troyka, GPIO.LOW)

    while (adc_value >= 2):
        adc_value = adc()
        print("Voltage:", adc_value)       
        adc_value_list.append(adc_value)
        GPIO.output(leds, num2led(adc_value))

    finish = time.time()
    duration = finish - start
    plt.plot(adc_value_list)
    plt.show()

    adc_value_list_str = [str(i) for i in adc_value_list]

    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(adc_value_list_str))

    with open("settings.txt", "w") as outfile:
        outfile.write("Частота дискретизации: " + str(duration / len(adc_value_list)) + "\n")
        outfile.write("Шаг кванования: " + str(3.3/256))

    print("Продолжительность эксперимента:", duration)
    print("Период одного измерения:", 0.01)
    print("Средняя частота дискретизации:", duration / len(adc_value_list))
    print("Шаг квантования:", 3.3/256)

except KeyboardInterrupt:
        print("\nProgram was stopped")
else:
    print("No exceptions")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(leds, GPIO.LOW)
    GPIO.cleanup(dac)
