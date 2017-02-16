from abc import ABCMeta, abstractmethod


class Server(metaclass=ABCMeta):

    HELLO_FORMAT = "Received message: {!s}"

    @abstractmethod
    def listen(self):
        pass

    @abstractmethod
    def close(self):
        pass
