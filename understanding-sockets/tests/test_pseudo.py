import sys
sys.path.append("..")

from tests import hello

from hellosocket.pseudosocketclient import PseudoSocketClient
from hellosocket.pseudosocketserver import PseudoSocketServer


def test_pseudo_pair():
    file_path = "/tmp/pseudo_socket.tmp"
    client = PseudoSocketClient(file_path)
    server = PseudoSocketServer(file_path)

    hello.say_hello(client, server)
