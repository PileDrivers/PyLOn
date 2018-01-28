#import RPi.GPIO as GPIO
import time
import serial

# from socketIO_client import SocketIO, LoggingNamespace Need
# https://github.com/socketio/socket.io-client

FETChannels = [7,11] # Left motor is pin 7, right motor is pin 11

# def fwd():
#     GPIO.output(FETChannels, GPIO.HIGH)
#     time.sleep(3)
#     GPIO.output(FETChannels, GPIO.LOW)
#
# def left():
#     GPIO.output(FETChannels[0], GPIO.HIGH)
#     time.sleep(3)
#     GPIO.output(FETChannel[0], GPIO.LOW)
#
# def right():
#     GPIO.output(FETChannel[1], GPIO.HIGH)
#     time.sleep(3)
#     GPIO.output(FETChannel[1], GPIO.LOW)

def main():
    # GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(FETChannels, GPIO.OUT)
    # GPIO.setup(FETChannels, GPIO.OUT, initial=GPIO.LOW)
    # fwd()
    # configure the serial connections (the parameters differs on the device you are connecting to)
    print('run check') #/dev/ttyUSB1
    ser = serial.Serial(
        port='COM6',
        baudrate=9600,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.SEVENBITS
    )
    ser.isOpen(); print('Serial Open')
    while 1:

        ser.write('1'.encode('utf-8'))
        time.sleep(2)
        # print(a)s

if __name__ == "__main__":
    main()
    GPIO.cleanup()
##### SocketIO client shit that we can look at when Nathan stops being a bitch

# def on_connect():
#     print('connect')
#
# def on_disconnect():
#     print('disconnect')
#
# def on_reconnect():
#     print('reconnect')
#
# def on_aaa_response(*args):
#     print('on_aaa_response', args)
#
# socketIO = SocketIO('localhost', 8000, LoggingNamespace)
# socketIO.on('connect', on_connect)
# socketIO.on('disconnect', on_disconnect)
# socketIO.on('reconnect', on_reconnect)
#
# # Listen
# socketIO.on('aaa_response', on_aaa_response)
# socketIO.emit('aaa')
# socketIO.emit('aaa')
# socketIO.wait(seconds=1)
#
# # Stop listening
# socketIO.off('aaa_response')
# socketIO.emit('aaa')
# socketIO.wait(seconds=1)
#
# # Listen only once
# socketIO.once('aaa_response', on_aaa_response)
# socketIO.emit('aaa')  # Activate aaa_response
# socketIO.emit('aaa')  # Ignore
# socketIO.wait(seconds=1)
