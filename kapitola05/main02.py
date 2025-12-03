from machine import Pin  # importujeme knihovnu
 
led = Pin(0, Pin.OUT)  # nastavíme pin číslo 1 jako výstupní

led.value(1) # nastaví hodnotu pinu na logickou 1
