import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(10):
    print('Sending request {}...'.format(request))
    socket.send(b'Hello')
    response = socket.recv().decode()
    print('Received reply {}: {}'.format(request, response))
