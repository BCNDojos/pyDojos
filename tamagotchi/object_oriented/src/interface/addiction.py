from abc import ABCMeta, abstractmethod, abstractproperty


class Addiction(metaclass=ABCMeta):

    @abstractmethod
    def satisfy(self):
        pass

    @abstractmethod
    def dissatisfy(self):
        pass

    @abstractproperty
    def happiness(self):
        pass
