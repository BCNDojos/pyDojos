from queue import Queue
from threading import Thread

from hellosocket.berkeleysocketserver import BerkeleySocketServer


class MultiConnSyncBerkeleySocketServer(BerkeleySocketServer):

    PREFIX = ":) "

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._listeners = Queue()

    def _build_async_listener(self, client_conn, address):
        return Thread(
            target=self._listen_task_by_conn,
            args=(client_conn, address)
        )

    def listen(self):
        self._socket.bind(self._address)
        self._socket.listen(1)
        self._listening = True
        while self._listening:
            client_conn, address = self._socket.accept()
            listener = self._build_async_listener(client_conn, address)
            listener.start()
            self._listeners.put((address, listener))

    def _listen_task_by_conn(self, client_conn, address):
        with client_conn:
            print("[server] Connects by {!s}".format(address))
            self._send_all(
                client_conn,
                address,
                "PyDojo PyBCN Socket Server v-0.1b\n"
            )
            self._send_all(client_conn, address, "Type 'quit' to exit\n")
            self._send_all(client_conn, address, self.PREFIX)
            while self._listening:
                try:
                    self._answer(client_conn, address)
                except BrokenPipeError:
                    break

    def _answer(self, client_conn, address):
        received = client_conn.recv(1024).decode()
        if received[:-1] == 'quit':
            print(
                "[server] {!s} exited".format(address)
            )
            raise BrokenPipeError('Gracefully disconnected')
        print(
            "[server] Received {!s} from {!s}".format(
                received[:-1],
                address
            )
        )
        answer = self.HELLO_FORMAT.format(received)
        self._send_all(client_conn, address, answer)
        self._send_all(client_conn, address, self.PREFIX)


if __name__ == "__main__":
    bind_address = "0.0.0.0"
    port = 43210
    server = MultiConnSyncBerkeleySocketServer(host=bind_address, port=port)
    server.listen()
