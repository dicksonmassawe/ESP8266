from machine import PWM, Pin
from time import sleep_ms

led = machine.PWM(Pin(4))

while True:
	led.freq(700)
	for i in range(0, 1024, 2):
		led.duty(i)
		sleep_ms(100)
	led.duty(0)
	sleep_ms(1000)
