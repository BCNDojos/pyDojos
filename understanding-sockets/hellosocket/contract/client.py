from abc import ABCMeta, abstractmethod


class Client(metaclass=ABCMeta):

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
