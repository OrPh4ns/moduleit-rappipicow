'''
@author Abdulrahman Othman
@email  abdulrahman.othman@web.de
@date   25.10.2023
@brief  Blind UHF Project
@device Rasp Pi Pico W MicroPython
@UHF    MetraTec
'''
from machine import UART, Pin
import bluetooth
from ble_simple_peripheral import BLESimplePeripheral
from time import sleep
from reader import Reader

# Objects
# Create a Bluetooth Low Energy (BLE) object
ble = bluetooth.BLE()
# Create an instance of the BLESimplePeripheral class with the BLE object
sp = BLESimplePeripheral(ble)
# MetraTec Module object
reader = Reader(115200,12,1)
reader.init_reader()

while True:

    # reader.transmit("xxxxx")
    reader.counter = reader.counter + 1
    print(reader.counter)
    #reader.transmit("rrrr")
    #sleep(0.1)
    #print(reader.receive())

    # i = 0
    # while True:
    #     if p.is_connected():
    #         # Short burst of queued notifications.
    #         for _ in range(3):
    #             data = str(i) + "_"
    #             print("TX", data)
    #             p.send(data)
    #             i += 1
    #     time.sleep_ms(100)
