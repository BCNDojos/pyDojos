import socket

from hellosocket.contract.client import Client


class BerkeleySocketClient(Client):

    def __init__(self, **kwargs):
        if "host" in kwargs and "port" in kwargs:
            self._address = (kwargs["host"], kwargs["port"])
        elif "file_path" in kwargs:
            self._address = kwargs["file_path"]
        else:
            raise AttributeError("Missing address")

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __del__(self):
        self._socket.close()

    def connect_background(self):
        pass

    def read(self, buffer_size):
        return self._socket.recv(buffer_size)

    def write(self, message):
        self._socket.sendall(message.encode())

    def connect(self):
        self._socket.connect(self._address)


