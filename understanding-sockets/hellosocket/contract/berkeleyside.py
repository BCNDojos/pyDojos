import os
import socket


class BerkeleySide:

    SHUTDOWN_FLAG = socket.SHUT_RDWR

    @classmethod
    def parse_address(cls, params):
        if "host" in params and "port" in params:
            address = (params["host"], params["port"])
        elif "file_path" in params:
            address = params["file_path"]
            if os.path.exists(address):
                os.remove(address)
        else:
            raise AttributeError("Missing address")

        return address

    @classmethod
    def build_socket(cls, unix_type=False):
        if unix_type:
            socket_af = socket.AF_UNIX
        else:
            socket_af = socket.AF_INET
        return socket.socket(socket_af, socket.SOCK_STREAM)
