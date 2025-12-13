from machine import Pin, Timer  
from utime import sleep

led = Pin(0, Pin.OUT)
switch = Pin(28, Pin.IN, Pin.PULL_DOWN)

my_timer = Timer()
timer_runs = False

def blinker(timer):
    led.toggle()

while True:
    if switch.value() == 1 and not timer_runs:
        my_timer.init(period=300, mode=Timer.PERIODIC, callback=blinker)
        timer_runs = True
        print("Časovač spuštěn")
    elif switch.value() == 0 and timer_runs:
        my_timer.deinit()
        led.off()
        timer_runs = False
        print("Časovač vypnut")
    sleep(0.01)
