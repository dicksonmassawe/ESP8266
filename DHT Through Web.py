
# Import libraries
import machine
import time
led = machine.Pin(2,machine.Pin.OUT)
led.off()

# ************************
# Configure the ESP32 wifi as Access Point mode.
import network
ssid = 'EPAL'
password = 'electronics'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while not ap.active():
    pass
print('network config:', ap.ifconfig())

# ************************
# Configure the socket connection
# over TCP/IP
import socket
# AF_INET - use Internet Protocol v4 addresses
# SOCK_STREAM means that it is a TCP socket.
# SOCK_DGRAM means that it is a UDP socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80)) # specifies that the socket is reachable by any address the machine happens to have
s.listen(5)     # max of 5 socket connections
# DHT sensor initializations
import dht
d = dht.DHT22(machine.Pin(23))
# If you will use DHT11, change it to:
# d = dht.DHT11(machine.Pin(23))
# ************************
# Function for creating the
# web page to be displayed
def web_page():
    # Get the DHT readings
    d.measure()
    t = d.temperature()
    h = d.humidity()
    
   html_page = """<!DOCTYPE HTML>   
     <html>   
     <head>   
      <meta name="viewport" content="width=device-width, initial-scale=1">   
      <meta http-equiv="refresh" content="1">   
     </head>   
     <body>   
       <center><h2>ESP32 Web Server in MicroPython </h2></center>   
       <center><p>Temperature is <strong>""" + str(t) + """ C.</strong>.</p></center>   
       <center><p>Humidity is <strong>""" + str(h) + """ %.</strong>.</p></center>   
     </body>   
     </html>"""   
   return html_page   

while True:
    # Socket accept() 
    conn, addr = s.accept()
    print("Got connection from %s" % str(addr))
    
    # Socket receive()
    request=conn.recv(1024)
    print("")
    print("Content %s" % str(request))
    # Socket send()
    request = str(request)
    
    # Create a socket reply
    response = web_page()
    conn.send('HTTP/1.1 200 OKn')
    conn.send('Content-Type: text/htmln')
    conn.send('Connection: close\n')
    conn.sendall(response)
    
    # Socket close()
    conn.close()