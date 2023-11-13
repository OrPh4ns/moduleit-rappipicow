'''
@author Abdulrahman Othman
@email  abdulrahman.othman@web.de
@date   09.11.2023
@brief  Blind UHF Project
@device Rasp Pi Pico W MicroPython
@UHF    MetraTec
'''
from machine import UART, Pin
from time import sleep, sleep_ms
# Reader Commands (Constants)
metra = {
    "reset": bytearray([0x52, 0x53, 0x54, 0x0D]),
    "ets": bytearray([0x53, 0x54, 0x44, 0x20, 0x45, 0x54, 0x53, 0x0D]),
    "sriOn": bytearray([0x53, 0x52, 0x49, 0x20, 0x4F, 0x4E, 0x0D]),
    "inv": bytearray([0x49, 0x4E, 0x56, 0x0D]),
    "setMsk": bytearray([0x53, 0x45, 0x54, 0x20, 0x4D, 0x53, 0x4B]),
    "tagRead": bytearray([0x52, 0x44, 0x54, 0x20, 0x54, 0x49, 0x44]),
    "tagRead1": bytearray([0x52, 0x44, 0x54, 0x20, 0x54, 0x49, 0x44, 0x20, 0x30, 0x20, 0x30])
}

class Reader:
    def __init__(self, baudrate:int, tx_pin:int, rx_pin:int):
        self.__uart = UART(0, baudrate=baudrate, tx=Pin(tx_pin), rx=Pin(rx_pin))
        self.init_reader()

    def init_reader(self):
        res = None
        suc = False
        self.__uart.write(metra['reset'])
        sleep(0.1)
        res = str(self.__uart.read())
        if "OK" in res:
            self.__uart.write(metra['ets'])
            sleep(0.1)
            res = str(self.__uart.read())
            if "OK" in res:
                self.__uart.write(metra['sriOn'])
                sleep(0.1)
                res = str(self.__uart.read())
                if "OK" in res:
                    suc = True
        if suc:
            print(self.response("Reader Init Success"))
        else:
            print(self.response("Init Error => "+res))
        
    def transmit(self, command):
        self.__uart.write(command)

    def response(self, message:str):
        return "Reponse["+message+"]"

    def reset(self):
        self.__uart.transmit(metra['reset'])

    def read_epc(self):
        if self.__uart.any():
            resp = str(self.__uart.read())
            print(resp)
        else:
            self.__uart.write(metra['inv'])
            sleep_ms(50)

    def prepare(self):
        pass

    def sleep(self):
        pass

    def wake_up(self):
        pass

    def response_print(self, msg:str, reponse):
        pass