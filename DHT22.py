import machine
import dht
from time import sleep_ms

dht22 = dht.DHT22(machine.Pin(4))

while True:
	dht22.measure()
	print("Temperature is: ", dht22.temperature(), "掳C")
	print("Humidity is: ", dht22.humidity(), "%")
	print("")
	sleep_ms(2000)