import machine
from time import sleep_ms

led = machine.Pin(4, machine.Pin.OUT)
led.off()
sw = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

def blink(sw):
    print("Interrupt is enabled")
    led.on()
    sleep_ms(500)
    led.off()
    sleep_ms(500)
    
sw.irq(trigger = machine.Pin.IRQ_FALLING, handler = blink)    