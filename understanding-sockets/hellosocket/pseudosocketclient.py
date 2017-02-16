import os

from hellosocket.contract.client import Client
from hellosocket.contract.pseudoside import PseudoSide


class PseudoSocketClient(Client, PseudoSide):

    def __init__(self, file_path):
        self._file_path = file_path

    def read(self):
        print("[client] Reads buffer")
        return self.read_and_remove(self._file_path, "client")

    def write(self, message):
        print("[client] Sends message {!s}".format(message))
        self.append_to_file(self._file_path, message, "client")

    def disconnect(self):
        print("[client] Close socket")

    def connect(self):
        print("[client] Open socket")
        os.path.isfile(self._file_path)
