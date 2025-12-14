from machine import Pin, Timer  
from utime import sleep

led = Pin(0, Pin.OUT)
switch = Pin(28, Pin.IN, Pin.PULL_DOWN)

my_timer = Timer()
timer_set = False

def vypni(timer):
    global timer_set
    
    led.off()
    timer_set = False

while True:
    if switch.value() == 1 and not timer_set:
        my_timer.init(period=5000, mode=Timer.ONE_SHOT, callback=vypni)
        led.on()
        print("Časovač spuštěn")
        timer_set = True
    
    sleep(0.01)
