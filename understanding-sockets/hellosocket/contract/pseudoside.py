import os

import time


class PseudoSide:

    @classmethod
    def append_to_file(cls, file_path, content, caller):
        print("[{!s}] append".format(caller))
        with open(file_path, "a") as pseudo_socket:
            pseudo_socket.write(content)
        time.sleep(0.5)           # Let it read for other

    @classmethod
    def read_and_remove(cls, file_path, caller):
        print("[{!s}] tries to read".format(caller))
        with open(file_path, "r") as pseudo_socket:
            received = pseudo_socket.read()
        if not received:
            return
        os.remove(file_path)
        print("[{!s}] read and remove ({!s})".format(caller, received))
        return received
