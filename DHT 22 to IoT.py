# Importing Libraries
import machine
import urequests
import network
import dht
from time import sleep

# API keys for ThingSpeaks
api_key = "***************"
field_01 = "1" # Temperature
field_02 = "2" # Humidity

# Function for connecting ESP 8266 to Station
def get_connect():
	
	# Station name and password
	ssid = "*********"
	password = "**************"
	
	sta = network.WLAN(network.STA_IF)
	if not sta.isconnected():
		print("Connecting.......................")
		sta.active(True)
		sta.connect(ssid, password)
		
		# Checking if is ESP 8266 has connected to station
		while not sta.isconnected():
			pass
		
	# Printing network configuration
	print("Network configuration: ", sta.ifconfig())
	
# Function to send request to ThingSpeaks via HTTP
def get_send(value1, value2):
	# url = "https://api.thingspeak.com/update?api_key=716VJH7A021S5O6U&field1=0"
	url = "https://api.thingspeak.com/update?api_key="
	url += api_key
	
	url += "&field"
	url += field_01
	url += "="
	url += str(value1)
	
	url += "&field"
	url += field_02
	url += "="
	url += str(value2)
	
	print(url)
	response = urequests.get(url)
	print(response.text)
	
# Object for DHT22 and Led
dht = dht.DHT22(machine.Pin(4))
led = machine.Pin(2, machine.Pin.OUT)
	
# Connecting to station
get_connect()

while True:
	dht.measure()
	temp = dht.temperature()
	humd = dht.humidity()
	get_send(temp, humd)
	sleep(16)
	led.off()
	sleep(1)
	led.on()
	sleep(1)
