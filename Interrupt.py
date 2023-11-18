import machine

led = machine.Pin(4, machine.Pin.OUT)
sw = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

def blink(pin):
    led.value(not led.value())

sw.irq(trigger=machine.Pin.IRQ_FALLING, handler=blink)