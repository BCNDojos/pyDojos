from abc import ABCMeta, abstractmethod, abstractproperty


class DigestiveSystem(metaclass=ABCMeta):

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def poo(self):
        pass

    @abstractmethod
    def burn(self):
        pass

    @abstractproperty
    def hungriness(self):
        pass

    @abstractproperty
    def fullness(self):
        pass
