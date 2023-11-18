import machine
import time

led = machine.Pin(4, machine.Pin.OUT)
pwm = machine.PWM(led)
# duty increase the voltage in PWM
pwm.init(freq=1, duty=512) # Initialize the PWM
# pwm.deinit() # Deinitialize the PWM

while True:
    for i in range(1024):
        led.value(1)
        pwm.duty(i)
        #time.sleep(0.1)