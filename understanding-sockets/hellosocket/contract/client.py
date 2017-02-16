from abc import ABCMeta, abstractmethod

from hellosocket.contract.berkeleyside import BerkeleySide


class Client(BerkeleySide, metaclass=ABCMeta):

    HELLO = "Hello, my name is client"

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def write(self, message):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass
