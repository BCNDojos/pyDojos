from abc import ABCMeta, abstractproperty

from tamagotchi.object_oriented.src.interface.parameter import Parameter


class LimitedParameter(Parameter, metaclass=ABCMeta):

    @abstractproperty
    def remain(self):
        pass
