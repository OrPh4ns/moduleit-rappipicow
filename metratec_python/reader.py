'''
@author Abdulrahman Othman
@email  abdulrahman.othman@web.de
@date   09.11.2023
@brief  Blind UHF Project
@device Rasp Pi Pico W MicroPython
@UHF    MetraTec
'''
from machine import UART, Pin

# Reader Commands (Constants)
metrca = {
    "reset": bytearray([0x52, 0x53, 0x54, 0x0D]),
    "ets": bytearray([0x53, 0x54, 0x44, 0x20, 0x45, 0x54, 0x53, 0x0D]),
    "sriOn": bytearray([0x53, 0x52, 0x49, 0x20, 0x4F, 0x4E, 0x0D]),
    "inv": bytearray([0x49, 0x4E, 0x56, 0x0D]),
    "setMsk": bytearray([0x53, 0x45, 0x54, 0x20, 0x4D, 0x53, 0x4B]),
    "tagRead": bytearray([0x52, 0x44, 0x54, 0x20, 0x54, 0x49, 0x44]),
    "tagRead1": bytearray([0x52, 0x44, 0x54, 0x20, 0x54, 0x49, 0x44, 0x20, 0x30, 0x20, 0x30])
}
repo = "Response= "

class Reader:
    counter = 0
    def __init__(self, baudrate:int, tx_pin:int, rx_pin:int):
        self.__uart = UART(0, baudrate=baudrate, tx=Pin(tx_pin), rx=Pin(rx_pin))

    def init_reader(self):
        pass
    def transmit(self, command):
        self.__uart.write(command)

    def receive(self):
         return self.__uart.read()
         #print(self.__uart.read())

    def reset(self):
        self.transmit()

    def read_tag(self):
        pass

    def prepare(self):
        pass

    def sleep(self):
        pass

    def wake_up(self):
        pass

    def response_print(self, msg:str, reponse):
        pass