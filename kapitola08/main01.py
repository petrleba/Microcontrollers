from machine import Pin, Timer  
from utime import sleep

led = Pin(0, Pin.OUT)
switch = Pin(28, Pin.IN, Pin.PULL_DOWN)

my_timer = Timer()

def blinker(timer):
    led.toggle()

while True:
    if switch.value() == 1:
        my_timer.init(period=300, mode=Timer.PERIODIC, callback=blinker)
        print("Časovač spuštěn")
    elif switch.value() == 0:
        my_timer.deinit()
        print("Časovač vypnut")
