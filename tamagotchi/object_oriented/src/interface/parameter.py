from abc import ABCMeta, abstractmethod, abstractproperty


class Parameter(metaclass=ABCMeta):

    @abstractmethod
    def increase(self):
        pass

    @abstractmethod
    def decrease(self):
        pass

    @abstractproperty
    def value(self):
        pass

    @abstractproperty
    def difference(self):
        pass
