import zmq
import time
import sys

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)
topic = 0
while True:
    topic, now = topic + 1, time.ctime()
    socket.send_string("1 update {} {}".format(topic, now))
    socket.send_string("2 update {} {}".format(topic, now))
    time.sleep(1)
