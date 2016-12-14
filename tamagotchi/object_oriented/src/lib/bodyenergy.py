from tamagotchi.object_oriented.src.interface.energy import Energy
from tamagotchi.object_oriented.src.interface.limitedparameter import \
    LimitedParameter


class BodyEnergy(Energy):

    def __init__(self, fullness: LimitedParameter):
        self._fullness = fullness

    @property
    def fullness(self):
        return self._fullness.value

    @property
    def emptiness(self):
        return self._fullness.remain

    def discharge(self):
        self._fullness.decrease()

    def charge(self):
        self._fullness.increase()
