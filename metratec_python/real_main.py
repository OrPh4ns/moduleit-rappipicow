'''
@author Abdulrahman Othman
@email  abdulrahman.othman@web.de
@date   25.10.2023
@brief  Blind UHF Project
@device Rasp Pi Pico W MicroPython
@UHF    MetraTec
'''

# MicroPython Moduls
from machine import UART,Pin
import bluetooth
from ble_simple_peripheral import BLESimplePeripheral
from time import sleep

# Metra Commands
metrca = {
    "reset": bytearray([0x52, 0x53, 0x54, 0x0D]),
    "ets": bytearray([0x53, 0x54, 0x44, 0x20, 0x45, 0x54, 0x53, 0x0D]),
    "sriOn": bytearray([0x53, 0x52, 0x49, 0x20, 0x4F, 0x4E, 0x0D]),
    "inv": bytearray([0x49, 0x4E, 0x56, 0x0D]),
    "setMsk": bytearray([0x53, 0x45, 0x54, 0x20, 0x4D, 0x53, 0x4B]),
    "tagRead": bytearray([0x52, 0x44, 0x54, 0x20, 0x54, 0x49, 0x44]),
    "tagRead1": bytearray([0x52, 0x44, 0x54, 0x20, 0x54, 0x49, 0x44, 0x20, 0x30, 0x20, 0x30])
}

# Create a Bluetooth Low Energy (BLE) object
ble = bluetooth.BLE()

# Create an instance of the BLESimplePeripheral class with the BLE object
sp = BLESimplePeripheral(ble)

# UART0 initialisieren for MetraTec Module
uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), bits=8, parity=None, stop=1)
print('Started UART0:', uart0)

# Pins
# Vibration
vibration = False
vibPin = 11
# Ton
tonPin = 9

# Consts
respo = "Response:"

#Setups
uart0.write(metrca['reset'])
sleep(0.1)
print(respo + "RST="+ uart0.readline())

uart0.write(metrca['ets'])
sleep(0.1)
print(respo + "STD ETS="+ uart0.readline())

uart0.write(metrca['sriOn'])
sleep(0.1)
print(respo + "SRI ON="+ uart0.readline())

while True:
    if sp.is_connected(): # Check if a BLE connection is established
        # Read the value from the internal temperature sensor
        
        sp.send("1111111")
        uart0.write(reset)
        sleep(0.5)
        print(uart0.read())
        sleep(3)