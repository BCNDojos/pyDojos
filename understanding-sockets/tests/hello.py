"""
Hello workflow:

    1. Server starts listening.
    2. Client connects to server.
    3. Client sends a hello message to server.
    4. Server reads the message and returns the ack for the received message.
    5. Client closes connection.
    5. Server closes socket.
    6. Assertions.
"""
import sys

import time

sys.path.append("..")

from hellosocket.contract.client import Client
from hellosocket.contract.server import Server

EXPECTED_HELLO_CLIENT = Client.HELLO
EXPECTED_HELLO_SERVER_FORMAT = Server.HELLO_FORMAT


def expected_server_response():
    return EXPECTED_HELLO_SERVER_FORMAT.format(EXPECTED_HELLO_CLIENT)


def say_hello(client: Client, server: Server):
    """
    Assert received ack from the server in client side when server listens in
    a separated thread.
    :param client: Client
    :param server: Server
    :return: None
    """
    server.listen()
    time.sleep(1)               # Let start socket server
    client.connect()
    client.write(EXPECTED_HELLO_CLIENT)
    answer = client.read()
    client.disconnect()
    server.close()
    assert answer == expected_server_response()
