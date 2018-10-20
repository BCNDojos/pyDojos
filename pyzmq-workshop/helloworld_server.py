import time
import zmq

context = zmq.Context()
server = context.socket(zmq.REP)
server.bind('tcp://*:5555')

while True:
    message = server.recv().decode()
    print('Received request: {}'.format(message))
    time.sleep(1)
    server.send(b'World')
