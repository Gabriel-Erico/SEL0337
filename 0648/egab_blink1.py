import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.IN, GPIO.PUD_UP)
def button(pin):
	if GPIO.input(pin):
		print("Released")
		GPIO.output(24, False)
	else:
		print("Pressed")
		GPIO.output(24, True)
GPIO.add_event_detect(23, GPIO.BOTH, callback = button, bouncetime=200)
try:
	while True:
		pass
except KeyboardInterrupt:
	GPIO.cleanup()

