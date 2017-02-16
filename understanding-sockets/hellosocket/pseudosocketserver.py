import os
from threading import Thread

import time

from hellosocket.contract.pseudoside import PseudoSide
from hellosocket.contract.server import Server


class PseudoSocketServer(Server, PseudoSide):

    def __init__(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
        self._file_path = file_path
        self._listening = False
        self._async_listener = Thread(target=self._listen_task)

    def _listen_task(self):
        print("[server] Connects by {!s}".format(self._file_path))
        open(self._file_path, 'a').close()
        self._listening = True
        while self._listening:
            received = self.read_and_remove(self._file_path, "server")
            if received:
                print("[server] Server got message")
                answer = self.HELLO_FORMAT.format(received)
                self.append_to_file(self._file_path, answer, "server")
            time.sleep(0.25)

    def listen(self):
        self._async_listener.start()

    def close(self):
        print("[server] Shutdowns socket")
        self._listening = False

        if self._async_listener.is_alive():
            print("[server] Joins background task")
            self._async_listener.join()
