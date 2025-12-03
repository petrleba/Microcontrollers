import machine  # importujeme knihovnu

# nastavíme pin číslo 1 jako výstupní
led = machine.Pin(0, machine.Pin.OUT)  

led.value(1)  # nastaví hodnotu pinu na logickou 1
