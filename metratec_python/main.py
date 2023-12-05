'''
@author Abdulrahman Othman
@email  abdulrahman.othman@web.de
@date   25.10.2023
@brief  Blind UHF Project
@device Rasp Pi Pico W MicroPython
@UHF    MetraTec
'''
from machine import Pin, PWM
from bluetooth import BLE
from ble_simple_peripheral import BLESimplePeripheral
from time import sleep, sleep_ms
from reader import Reader


# Objects
power_button = Pin(15, Pin.IN, Pin.PULL_DOWN)
buzzer_pin =Pin(14, Pin.OUT)
buzzer = PWM(buzzer_pin)
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

def play_tone(frequency, duration, duty):
    buzzer.freq(frequency)
    buzzer.duty_u16(duty)
    sleep_ms(duration)
    buzzer.duty_u16(0)
    sleep_ms(duration)

while True:
    if power_button.value():
        if xPower:
            sleep(0.5)
            xPower=False
            sp.send(response("Device + Bluetooth Desconnected"))
            sp.desonnect()
            reader.sleep()
            play_tone(300, 250, 4000)
            play_tone(250, 200, 4000)
            play_tone(200, 150, 4000)
        else:
            sleep(0.5)
            xPower=True
            sp.connect()
            reader.wake_up()
            play_tone(200, 100, 4000)
            play_tone(250, 200, 4000)
            play_tone(300, 300, 4000)
            
    if xPower:
        # if sp.is_connected():
        reader.read_epc()
        #sp.send(str(reader.read_epc()))
        #sleep(0.5)