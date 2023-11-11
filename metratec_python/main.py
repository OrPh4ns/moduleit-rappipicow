'''
init update later
'''
from machine import UART, Pin
from time import sleep
from .reader import Reader

led_onboard = Pin("LED", Pin.OUT)

respo = "Response:"
reset = bytearray([0x52, 0x53, 0x54, 0x0D])
ets = bytearray([0x53, 0x54, 0x44, 0x20, 0x45, 0x54, 0x53, 0x0D])
sriOn = bytearray([0x53, 0x52, 0x49, 0x20, 0x4F, 0x4E, 0x0D])
inv = bytearray([0x49, 0x4E, 0x56, 0x0D])


from machine import UART, Pin
from time import sleep
import binascii


reader = Reader(115200,12,1)
uart0 = UART(0, baudrate=115200, tx=Pin(12), rx=Pin(1) ,bits=8, parity=None, stop=1)


while True:
    #binascii.hexlify("5253540D")

    uart0.write()
    sleep(0.1)
    if uart0.any():
        print(uart0.read())
    sleep(0.3)
    
    "52 53 54 0D"