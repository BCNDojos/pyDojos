from threading import Thread

from hellosocket.contract.berkeleyside import BerkeleySide
from hellosocket.contract.server import Server


class BerkeleySocketServer(Server, BerkeleySide):

    def __init__(self, **kwargs):
        self._address = self.parse_address(kwargs)
        unix_type = type(self._address) == str
        self._socket = self.build_socket(unix_type)
        self._listening = False
        self._async_listener = Thread(target=self._listen_task)

    def _listen_task(self):
        self._socket.bind(self._address)
        self._socket.listen(1)
        client_conn, address = self._socket.accept()
        with client_conn:
            print("[server] Connects by {!s}".format(address))
            self._listening = True
            while self._listening:
                print("[server] while")
                received = client_conn.recv(1024).decode()
                answer = self.HELLO_FORMAT.format(received).encode()
                self._send_all(client_conn, answer)

    def _send_all(self, conn, answer):
        if self._listening:
            conn.sendall(answer)

    def listen(self):
        self._async_listener.start()

    def close(self):
        print("[server] Shutdowns socket")
        self._listening = False
        self._socket.shutdown(self.SHUTDOWN_FLAG)
        self._socket.close()

        if self._async_listener.is_alive():
            print("[server] Joins background task")
            self._async_listener.join()
