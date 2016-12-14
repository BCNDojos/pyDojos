from tamagotchi.object_oriented.src.interface.digestivesystem import \
    DigestiveSystem


class Tamagotchi(object):

    def __init__(
            self,
            digestive_sys: DigestiveSystem
    ):
        self._digestive_sys = digestive_sys

    @property
    def fullness(self):
        return self._digestive_sys.fullness

    @property
    def hungriness(self):
        return self._digestive_sys.hungriness

    def feed_it(self):
        self._digestive_sys.eat()
