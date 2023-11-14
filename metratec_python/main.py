'''
@author Abdulrahman Othman
@email  abdulrahman.othman@web.de
@date   25.10.2023
@brief  Blind UHF Project
@device Rasp Pi Pico W MicroPython
@UHF    MetraTec
'''
from machine import Pin,deepsleep
from bluetooth import BLE
from ble_simple_peripheral import BLESimplePeripheral
from time import sleep
from reader import Reader


# Objects
power_button = Pin(15, Pin.IN, Pin.PULL_DOWN)
# Create a Bluetooth Low Energy (BLE) object
ble = BLE()
# Create an instance of the BLESimplePeripheral class with the BLE object
sp = BLESimplePeripheral(ble)
# MetraTec Module object
reader = Reader(115200,12,1)
reader.init_reader()

xPower = False

def response(message:str):
    return "Reponse["+message+"]"

while True:
    if power_button.value():
        if xPower:
            sleep(0.5)
            xPower=False
            sp.send(response("Device + Bluetooth Desconnected"))
            sp.desonnect()
        else:
            sleep(0.5)
            xPower=True
            sp.connect()
            
    if xPower:
        # if sp.is_connected():
        sp.send(str(reader.read_epc()))
        sleep(0.5)
    
    # if power_button.value() == 1:
    #     reader.read_epc()
    # else:
    #     print("Power Off")
    # if not interrupt_pin.value():
    #     machine.deepsleep(sleep_time * 1000)
    # else:
    #     time.sleep(sleep_time)
    
    
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
