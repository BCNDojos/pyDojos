from abc import ABCMeta, abstractmethod

from hellosocket.contract.berkeleyside import BerkeleySide


class Server(BerkeleySide, metaclass=ABCMeta):

    HELLO_FORMAT = "Received message: {!s}"

    @abstractmethod
    def listen(self):
        pass

    @abstractmethod
    def close(self):
        pass
