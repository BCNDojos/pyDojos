from tamagotchi.object_oriented.src.interface.addiction import Addiction
from tamagotchi.object_oriented.src.interface.parameter import Parameter


class GameAddiction(Addiction):

    def __init__(self, happiness: Parameter):
        self._happiness = happiness

    @property
    def happiness(self):
        return self._happiness.value

    def dissatisfy(self):
        self._happiness.decrease()

    def satisfy(self):
        self._happiness.increase()
