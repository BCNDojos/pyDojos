"""
Hello workflow:

    1. Server starts listening.
    2. Client connects to server.
    3. Client sends a hello message to server.
    4. Server reads the message and returns the ack for the received message.
    5. Server closes connection.
    6. Assertions.
"""
import sys
sys.path.append("..")

from hellosocket.contract.client import Client
from hellosocket.contract.server import Server

EXPECTED_HELLO_CLIENT = Client.HELLO
EXPECTED_HELLO_SERVER_FORMAT = Server.HELLO_FORMAT


def expected_server_response():
    return EXPECTED_HELLO_SERVER_FORMAT.format(EXPECTED_HELLO_CLIENT)


def hello_from_client(client: Client, server: Server):
    """
    Assert received ack from the server in client side when server listens in
    a separated thread.
    :param client: Client
    :param server: Server
    :return: None
    """
    server.listen_background()
    client.connect()
    client.write(EXPECTED_HELLO_CLIENT)
    answer = client.read(256)
    server.close()
    assert answer == expected_server_response()


def hello_from_server(client: Client, server: Server):
    """
    Assert received hello from client in server side when client connects in a
    separated thread.
    :param client: Client
    :param server: Server
    :return: None
    """
    server.listen()
    client.connect_background()
    answer = server.read()
    server.write(EXPECTED_HELLO_SERVER_FORMAT)
    server.close()
    assert answer == EXPECTED_HELLO_CLIENT
