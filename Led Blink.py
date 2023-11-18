import machine
from time import sleep_ms

led = machine.Pin(2, machine.Pin.OUT)

while True:
	led.on()
	print("Led is On")
	sleep_ms(1000)
	
	led.off()
	print("Led is Off")
	sleep_ms(1000)