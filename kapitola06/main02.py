# IMPORT MODULŮ, KNIHOVEN A METOD
from machine import Pin  # importujeme třídu Pin z modulu machine
from utime import sleep  # importujeme metodu sleep z modulu utime

# NASTAVENÍ MIKROKONTROLERU
led = Pin(0, Pin.OUT)    # nastavíme pin číslo 0 jako výstupní

# HLAVNÍ SMYČKA (CYKLUS) PROGRAMU
while True:
    led.toggle()  # přepne hodnotu na výstupním pinu vedoucím k LED diodě
                  # z aktuální hodnoty na opačnou logickou hodnotu
                  # tedy z hodnoty 0 na 1 nebo z hodnoty 1 na 0
    print("Hodnota na pinu LED diody:", led.value())
    sleep(1)      # uspí mikrokontroler na daný počet sekund
