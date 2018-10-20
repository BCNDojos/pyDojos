import sys
import zmq

context = zmq.Context()
sock = context.socket(zmq.SUB)

topic = "1"
if len(sys.argv) > 1:
    topic = sys.argv[1]
sock.setsockopt_string(zmq.SUBSCRIBE, topic)
sock.connect("tcp://127.0.0.1:5556")

while True:
    message = sock.recv_string()
    print(message)
