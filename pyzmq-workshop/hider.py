import random
import zmq

cities = open('cities.txt').readlines()
city = random.choice(cities).strip()
print('[HIDER] City chosen is {}'.format(city))

context = zmq.Context()
server = context.socket(zmq.REP)
server.bind('tcp://*:5555')

while True:
    message = server.recv().decode()
    print('[HIDER] Received request: {}'.format(message))
    print('[HIDER] Current city: {}'.format(city))
    reply = 'INCORRECT'
    if message == city:
        reply = 'CORRECT'
        city = random.choice(cities).strip()
        print('[HIDER] City chosen is {}'.format(city))
    server.send(str.encode(reply))
