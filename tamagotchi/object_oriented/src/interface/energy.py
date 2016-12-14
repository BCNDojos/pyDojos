from abc import ABCMeta, abstractmethod, abstractproperty


class Energy(metaclass=ABCMeta):

    @abstractproperty
    def fullness(self):
        pass

    @abstractproperty
    def emptiness(self):
        pass

    @abstractmethod
    def charge(self):
        pass

    @abstractmethod
    def discharge(self):
        pass
