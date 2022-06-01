# https://techhobby.net/2020/04/16/raspberry-pi%E3%81%AEgpio%E3%81%A7%E3%83%AA%E3%83%AC%E3%83%BC%E9%A7%86%E5%8B%95/

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) # GPIOの接続先を指定する。
channel1 = 6
#channel2 = 15

GPIO.setwarnings(False)
GPIO.setup(channel1, GPIO.OUT)
#GPIO.setup(channel2, GPIO.IN)

try:
    while True:
        GPIO.output(channel1, GPIO.HIGH)
        print('Relay ON')
        sleep(1)
        GPIO.output(channel1, GPIO.LOW)
        print('Relay OFF')
        sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
