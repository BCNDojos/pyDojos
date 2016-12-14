from abc import ABCMeta, abstractmethod, abstractproperty


class DigestiveSystem(metaclass=ABCMeta):

    @abstractmethod
    def eat(self):
        pass

    @abstractproperty
    def hungriness(self):
        pass

    @abstractproperty
    def fullness(self):
        pass
