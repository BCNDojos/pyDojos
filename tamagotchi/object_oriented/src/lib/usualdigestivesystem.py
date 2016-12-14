from tamagotchi.object_oriented.src.interface.digestivesystem import \
    DigestiveSystem
from tamagotchi.object_oriented.src.interface.limitedparameter import \
    LimitedParameter


class UsualDigestiveSystem(DigestiveSystem):

    def __init__(self, fullness: LimitedParameter):
        self._fullness = fullness

    @property
    def hungriness(self):
        return self._fullness.remain

    @property
    def fullness(self):
        return self._fullness.value

    def eat(self):
        self._fullness.increase()
