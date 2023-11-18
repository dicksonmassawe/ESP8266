import network

ssid = "**********"  # Replace with your Wi-Fi network SSID
password = "***********"  # Replace with your Wi-Fi network password

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    pass

print("ESP8266 connected to Wi-Fi network:", ssid)
print("IP address:", station.ifconfig()[0])
