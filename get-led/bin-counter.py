import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = reversed([24, 22, 23, 27, 17, 25, 12, 16])
print(leds)
GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)

up = 9
down = 10
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

while True:
    if GPIO.input(up) and num < 255:
        num += 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(down) and num > 0:
        num -= 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    GPIO.output(leds, dec2bin(num))