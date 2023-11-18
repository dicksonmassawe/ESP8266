# Importing libraries
import machine
import time

# Creating Led Object and setting it to be off
led = machine.Pin(12, machine.Pin.OUT)
led.off()

# Configuring esp8266 as Access Point
import network
ssid = "ESP8266"
password = "electronics"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)
while not ap.active():
    pass
print('network config:', ap.ifconfig())


# ************************
# Configure the socket connection over TCP/IP
import socket

# AF_INET - use Internet Protocol v4 addresses
# SOCK_STREAM means that it is a TCP socket.
# SOCK_DGRAM means that it is a UDP socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80)) # specifies that the socket is reachable by any address the machine happens to have
s.listen(5)     # max of 5 socket connections

# ************************
# Function for creating the
# web page to be displayed
def web_page():
    if led.value()==1:
        led_state = 'ON'
        print('led is ON')
    elif led.value()==0:
        led_state = 'OFF'
        print('led is OFF')
        
    html_page = """<!DOCTYPE HTML>   
    <html>   
    <head>   
        <meta name="viewport" content="width=device-width, initial-scale=1">   
    </head>   
    <body>   
        <center><h2>ESP32 Web Server in MicroPython </h2></center>   
        <center>   
            <form>   
                <button type='submit' name="LED" value='1'> LED ON </button>   
                <button type='submit' name="LED" value='0'> LED OFF </button>   
            </form>   
        </center>   
        <center><p>LED is now <strong>""" + led_state + """</strong>.</p></center>   
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
    print("")
    print("Content %s" % str(request))

    # Socket send()
    request = str(request)
    led_on = request.find('/?LED=1')
    led_off = request.find('/?LED=0')
    if led_on == 6:
        print('LED ON')
        print(str(led_on))
        led.value(1)
    elif led_off == 6:
        print('LED OFF')
        print(str(led_off))
        led.value(0)
    response = web_page()
    conn.send('HTTP/1.1 200 OKn')
    conn.send('Content-Type: text/htmln')
    conn.send('Connection: close\n')
    conn.sendall(response)
    
    # Socket close()
    conn.close()
