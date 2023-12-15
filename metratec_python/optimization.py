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
    "reset": b'\x52\x53\x54\x0D',
    "ets": b'\x53\x54\x44\x20\x45\x54\x53\x0D',
    "sriOn": b'\x53\x52\x49\x20\x4F\x4E\x0D',
    "inv": b'\x49\x4E\x56\x0D',
    "stb": b'\x53\x54\x42\x0D',
    "setMsk": b'\x53\x45\x54\x20\x4D\x53\x4B',
    "wak": b'\x57\x41\x4B\x0D'
}

class Reader:
    def __init__(self, baudrate: int, tx_pin: int, rx_pin: int):
        self.__uart = UART(0, baudrate=baudrate, tx=Pin(tx_pin), rx=Pin(rx_pin))
        self.init_reader()

    def init_reader(self):
        suc = False
        if self.send_command(metra['reset']):
            if self.send_command(metra['ets']):
                if self.send_command(metra['sriOn']):
                    suc = True
        if suc:
            print(self.response("Reader Init Success"))
        else:
            print(f"Init Error => {self.response(self.__uart.read())}")

    def send_command(self, command):
        self.__uart.write(command)
        sleep(0.1)
        res = self.__uart.read()
        return b"OK" in res

    def response(self, message: str):
        return f"Response[{message}]"

    def read_epc(self):
        if self.__uart.any():
            resp = self.__uart.read()

            if b"IVF" in resp and len(resp) > 20:
                print(self.response(resp))
                return self.response(resp)
            elif b"NSS" in resp:
                print(self.response("NSS Failure"))
                self.send_command(metra['ets'])
                return self.response(resp)
            elif b"CRT" in resp:
                print(self.response("CRT Failure"))
                self.init_reader()
        else:
            self.send_command(metra['inv'])
            sleep_ms(50)
            return False

    def sleep(self):
        self.send_command(metra['stb'])
        print("Metratec is sleeping ..")

    def wake_up(self):
        self.send_command(metra['wak'])
        print("Metratec is waking up ..")