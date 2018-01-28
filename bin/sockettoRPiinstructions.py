#import RPi.GPIO as GPIO
import time
import serial
from socketIO_client import SocketIO, BaseNamespace

# import logging
# logging.getLogger('requests').setLevel(logging.WARNING)
# logging.basicConfig(level=logging.DEBUG)

# FETChannels = [7,11] # Left motor is pin 7, right motor is pin 11

ser = serial.Serial(
    port='COM6',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

class PylonNamespace(BaseNamespace):
    
    def on_connect(self):
        print('[Connected to Node]')

    def on_event(self, *args):
        #print(args[0])
        #print(args[1])
        command = args[1]['command']
        #print(command)
        if command == "left":
            ser.write('2'.encode('utf-8'))
        elif command == "right":
            ser.write('3'.encode('utf-8'))
        elif command == "forward":
            ser.write('1'.encode('utf-8'))

def main():
   
    print('run check') #/dev/ttyUSB1
    ser.isOpen(); print('Serial Open')

    socketIO = SocketIO('https://pylon-driver-101.herokuapp.com/', verify=False)
    #socketIO.wait(seconds=1)
    pylon_namespace = socketIO.define(PylonNamespace, '/pylon')
    socketIO.wait()

    # while 1:

    #     ser.write('1'.encode('utf-8'))
    #     time.sleep(2)
        # print(a)s

if __name__ == "__main__":
    main()
