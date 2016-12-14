from tamagotchi.object_oriented.src.interface.addiction import Addiction
from tamagotchi.object_oriented.src.interface.digestivesystem import \
    DigestiveSystem
from tamagotchi.object_oriented.src.interface.energy import Energy


class Tamagotchi(object):

    def __init__(
            self,
            addiction: Addiction,
            digestive_sys: DigestiveSystem,
            energy: Energy
    ):
        self._addiction = addiction
        self._digestive_sys = digestive_sys
        self._energy = energy

    @property
    def fullness(self):
        return self._digestive_sys.fullness

    @property
    def hungriness(self):
        return self._digestive_sys.hungriness

    @property
    def happiness(self):
        return self._addiction.happiness

    @property
    def tiredness(self):
        return self._energy.emptiness

    def feed_it(self):
        self._digestive_sys.eat()

    def play_with_it(self):
        self._addiction.satisfy()
        self._energy.discharge()
