from machine import Pin, Timer  
from utime import sleep

led = Pin(0, Pin.OUT)
switch = Pin(28, Pin.IN, Pin.PULL_DOWN)

my_timer = Timer()

def vypni(timer):
    led.off()

while True:
    if switch.value() == 1:
        my_timer.init(period=5000, mode=Timer.ONE_SHOT, callback=vypni)
        led.on()
        print("Časovač spuštěn")
    
    sleep(0.01)
