#import RPi.GPIO as GPIO
import time
import serial
from socketIO_client import SocketIO, BaseNamespace
from gtts import gTTS
import os

# import logging
# logging.getLogger('requests').setLevel(logging.WARNING)
# logging.basicConfig(level=logging.DEBUG)

# FETChannels = [7,11] # Left motor is pin 7, right motor is pin 11

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
)

class PylonNamespace(BaseNamespace):
    
    def on_connect(self):
        print('[Connected to Node]')

    def talk(self, words):
        tts = gTTS(text=words, lang='en')
        filename = words + ".mp3"
        tts.save(filename)
        os.system("mpg321 " + filename)

    def on_event(self, *args):
        #print(args[0])
        #print(args[1])
        command = args[1]['command']
        #print(command)
        if command == "left":
            ser.write('2'.encode('utf-8'))
        elif command == "right":
            ser.write('4'.encode('utf-8'))
        elif command == "forward":
            ser.write('1'.encode('utf-8'))
        elif command == "speak1" or command == "speak2" or command == "speak3":
            speak_text = args[1]['data']
            self.talk(speak_text)

def main():
   
    print('run check') #/dev/ttyUSB1
    ser.isOpen(); print('Serial Open')

    socketIO = SocketIO('https://pylon-driver-101.herokuapp.com', verify=False)
    pylon_namespace = socketIO.define(PylonNamespace, '/pylon')
    socketIO.wait()

        # ser.write('3'.encode('utf-8'))
        # time.sleep(2)
        # print('ggg')

     # print(a)s

if __name__ == "__main__":
    main()
