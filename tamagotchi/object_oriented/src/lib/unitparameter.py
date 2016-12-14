from tamagotchi.object_oriented.src.interface.parameter import Parameter


class UnitParameter(Parameter):

    _UNIT_VALUE = 1

    def __init__(self, start_value=0):
        self._value = start_value

    @property
    def value(self):
        return self._value

    def decrease(self):
        self._value -= self._UNIT_VALUE

    def increase(self):
        self._value += self._UNIT_VALUE
