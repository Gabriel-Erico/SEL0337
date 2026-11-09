#!/user/bin/python3

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)

GPIO.output(24,False)
GPIO.cleanup()
print("Serviço parado: LED desligado e GPIOs liberadas.")
