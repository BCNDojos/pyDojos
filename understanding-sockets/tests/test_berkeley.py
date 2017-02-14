import sys
sys.path.append("..")

from tests import hello

from hellosocket.berkeleysocketserver import BerkeleySocketServer
from hellosocket.berkeleysocketclient import BerkeleySocketClient


def test_unix_pair():
    file_path = "/tmp/pseudo_socket.tmp"
    client = BerkeleySocketClient(file_path)
    server = BerkeleySocketServer(file_path)

    hello.hello_from_client(client, server)
    hello.hello_from_server(client, server)


def test_internet_pair():
    host = "127.0.0.1"
    bind_address = "127.0.0.1"
    port = 43210
    client = BerkeleySocketClient(host, port)
    server = BerkeleySocketServer(bind_address, port)

    hello.hello_from_client(client, server)
    hello.hello_from_server(client, server)
