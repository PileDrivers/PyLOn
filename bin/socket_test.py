from socketIO_client import SocketIO, BaseNamespace

# import logging
# logging.getLogger('requests').setLevel(logging.WARNING)
# logging.basicConfig(level=logging.DEBUG)

class PylonNamespace(BaseNamespace):
    
    def on_connect(self):
        print('[Connected to Node]')

    def on_event(self, *args):
        print(args)


socketIO = SocketIO('localhost', 5000)
#socketIO.wait(seconds=1)
pylon_namespace = socketIO.define(PylonNamespace, '/pylon')
print("3")
#SocketIO.on('connect', hello)
print("4")
#socketIO.emit('command')
print("5")
socketIO.wait()#socketIO.wait()

