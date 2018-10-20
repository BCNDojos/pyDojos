import random
import sys
import zmq

cities = open('cities.txt').readlines()

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

response = ''
while response != 'CORRECT':
    city = random.choice(cities).strip()
    print('[SEEKER] Guessed city is {}'.format(city))
    socket.send(str.encode(city))
    response = socket.recv().decode()
    print('[SEEKER] Received reply {}: {}'.format(city, response))
