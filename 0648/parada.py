#!/usr/bin/python3
#programa para desligar o LED e liberar as GPIOs ao parar o servico(ExecStop)

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

#desliga o LED (na GPIO 24) e limpa as configuracoes
GPIO.output(24, False)
GPIO.cleanup()
print("Serviço parado: LED desligado e GPIOs liberadas.")
