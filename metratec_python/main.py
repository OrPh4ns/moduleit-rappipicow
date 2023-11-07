'''
init update later
'''
from machine import UART, Pin
from time import sleep

led_onboard = Pin("LED", Pin.OUT)

respo = "Response:"
reset = [0x52 ,0x53 ,0x54 ,0x0D]

ets = bytearray([0x53, 0x54, 0x44, 0x20, 0x45, 0x54, 0x53, 0x0D])
sriOn = bytearray([0x53, 0x52, 0x49, 0x20, 0x4F, 0x4E, 0x0D])
inv = bytearray([0x49, 0x4E, 0x56, 0x0D])

the_text = "0x52 0x53 0x54 0x0D"

# UART0 initialisieren
uart0 = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1), bits=8, parity=None, stop=1)


while True:
    led_onboard.on()
    # halbe Sekunde warten
    sleep(0.5)
    # LED ausschalten
    led_onboard.off()
    uart0.write("0x52 0x53 0x54 0x0D")
    if uart0.any():
        print(uart0.read())
        sleep(1)
    print("Connected..")
    uart_read = uart0.read()
    if uart_read is not None:
        if "OK" in uart_read:
            uart0.write(''' xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxs ''')
            uart0.read()
        uart0.write(uart_read)
        uart0.read()
    else:
        print(uart0.read())