# Bibliotheken laden
from machine import Pin,UART
from time import sleep

# Initialisierung der Onboard-LED
led_onboard = Pin("LED", Pin.OUT)
uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), bits=8, parity=None, stop=1)
# Wiederholung (Endlos-Schleife)
while True:
    uart0.write("RRRRRRRRRRRRRRRRRRRRRR")
    sleep(0.1)
    print("RST=" + uart0.readline())
    # LED einschalten
    led_onboard.on()
    # halbe Sekunde warten
    sleep(0.5)
    # LED ausschalten
    led_onboard.off()
    # 1 Sekunde warten
    sleep(1)