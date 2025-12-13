from machine import Pin, Timer  
from utime import sleep

led = Pin(0, Pin.OUT)
switch = Pin(28, Pin.IN, Pin.PULL_DOWN)

my_timer = Timer()
last_button_state = 0
blinking = False

def blinker(timer):
    led.toggle()

while True:
    current_button_state = switch.value()

    if current_button_state == 1 and last_button_state == 0:  
        blinking = not blinking      

        if blinking:
            my_timer.init(period=300, mode=Timer.PERIODIC, callback=blinker)      
            print("Časovač spuštěn")
        else:
            my_timer.deinit() 
            led.off()   
            print("Časovač vypnut")

    last_button_state = current_button_state
    sleep(0.01)
