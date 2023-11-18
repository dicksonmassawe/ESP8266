import machine
import time

# Set object for buzz and pwm pin
buz = machine.Pin(12, machine.Pin.OUT)

# Attach pwm to buz pin
pwm =machine.PWM(buz)

# Set buzz frequency and duty
pwm.freq(1047)
pwm.duty(512)

time.sleep(10)

# Turn off the buzzer pulse
pwm.duty(0)

# Disconnect pwm from buz pin
pwm.deinit()