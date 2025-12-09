# IMPORT MODULŮ, KNIHOVEN A METOD
from machine import Pin
from utime import sleep

# NASTAVENÍ MIKROKONTROLERU
led = Pin(0, Pin.OUT)    # nastavíme pin číslo 0 jako výstupní

# nastavíme pin číslo 28 jako vstupní 
# a jeho vstup ošetřený pull up rezistorem
tlacitko = Pin(28, Pin.IN, Pin.PULL_DOWN)  

led.value(0)

while True:
    if (tlacitko.value() == 1):  # zjistíme hodnotu na pinu 28. Je tlačítko sepnuto?
        led.value(1)
    else:
        led.value(0)

    sleep(0.1)      # uspí mikrokontroler na daný počet sekund