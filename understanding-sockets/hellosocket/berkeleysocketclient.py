from hellosocket.contract.client import Client


class BerkeleySocketClient(Client):

    def __init__(self, **kwargs):
        self._address = self.parse_address(kwargs)
        unix_type = type(self._address) == str
        self._socket = self.build_socket(unix_type)

    def disconnect(self):
        print("[client] Close socket")
        self._socket.close()

    def read(self):
        print("[client] Reads buffer")
        received = self._socket.recv(1024).decode()
        return received

    def write(self, message):
        print("[client] Sends message {!s}".format(message))
        self._socket.sendall(message.encode())

    def connect(self):
        self._socket.connect(self._address)


