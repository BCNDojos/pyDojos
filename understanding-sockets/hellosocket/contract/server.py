from abc import ABCMeta, abstractmethod


class Server(metaclass=ABCMeta):

    HELLO_FORMAT = "Received message: {!s}"

    @abstractmethod
    def listen_background(self):
        pass

    @abstractmethod
    def listen(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, message_format):
        pass

    @abstractmethod
    def close(self):
        pass
