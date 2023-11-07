'''
init update later
'''
from machine import UART, Pin
from time import sleep



respo = "Response:"
#reset = "0x520x530x540x0D"
# reset = bytearray([0x52 ,0x53 ,0x54 ,0x0D])
reset = [0x52 ,0x53 ,0x54 ,0x0D]
#reset = b"\x52\x53\x54\x0D"

ets = bytearray([0x53, 0x54, 0x44, 0x20, 0x45, 0x54, 0x53, 0x0D])
sriOn = bytearray([0x53, 0x52, 0x49, 0x20, 0x4F, 0x4E, 0x0D])
inv = bytearray([0x49, 0x4E, 0x56, 0x0D])

the_text = "0x52 0x53 0x54 0x0D"

count = 0
# UART0 initialisieren
uart0 = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1), bits=8, parity=None, stop=1)
print('UART0:', uart0)

while True:
    if(count==1000):
        count=0
    else:
        count = count+1
        print(count)
    uart0.write("0x52 0x53 0x54 0x0D")
    #print("Command = ",reset)
    sleep(0.5)
    uart_read = uart0.read()
    if uart_read is not None:
        if "OK" in uart_read:
            print(''' xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxs ''')
        print(uart_read)
    else:
        print("Wait ..")