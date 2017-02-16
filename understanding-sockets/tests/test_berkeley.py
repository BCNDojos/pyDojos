import sys
sys.path.append("..")

from tests import hello

from hellosocket.berkeleysocketserver import BerkeleySocketServer
from hellosocket.berkeleysocketclient import BerkeleySocketClient


def test_unix_pair():
    file_path = "/tmp/unix_socket.sock"
    client = BerkeleySocketClient(file_path=file_path)
    server = BerkeleySocketServer(file_path=file_path)
    hello.say_hello(client, server)


def test_internet_pair():
    host = "127.0.0.1"
    bind_address = "127.0.0.1"
    port = 43210
    client = BerkeleySocketClient(host=host, port=port)
    server = BerkeleySocketServer(host=bind_address, port=port)
    hello.say_hello(client, server)
