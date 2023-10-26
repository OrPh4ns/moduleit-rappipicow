'''
init update later
'''
from machine import UART, Pin
from time import sleep


respo = "Response:"
reset = bytearray([0x52, 0x53, 0x54, 0x0D])
ets = bytearray([0x53, 0x54, 0x44, 0x20, 0x45, 0x54, 0x53, 0x0D])
sriOn = bytearray([0x53, 0x52, 0x49, 0x20, 0x4F, 0x4E, 0x0D])
inv = bytearray([0x49, 0x4E, 0x56, 0x0D])


xxxx = bytearray([0x0D, 0x53, 0x54, 0x52])
# UART0 initialisieren
uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), bits=8, parity=None, stop=1)
print('UART0:', uart0)
print()

# UART1 initialisieren
uart1 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9), bits=8, parity=None, stop=1)
print('UART1:', uart1)

while True:
    txData = 'Hallo Welt'

    #print('Daten empfangen:', rxData.decode('utf-8'))
    #print("oooooooooooooooooooooooooooooooo")
    uart0.write(reset)
    sleep(0.5)
    print(uart0.read())
    #sleep(0.5)