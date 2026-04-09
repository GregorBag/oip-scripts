import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

foto_trans = 6
GPIO.setup(foto_trans, GPIO.IN)

state = 1

while True:
    if GPIO.input(foto_trans):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)