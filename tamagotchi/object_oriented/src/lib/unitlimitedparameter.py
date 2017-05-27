from tamagotchi.object_oriented.src.interface.limitedparameter import \
    LimitedParameter


class UnitLimitedParameter(LimitedParameter):

    _UNIT_VALUE = 1

    def __init__(self, start_value=0, limit=0):
        self._value = start_value
        self._limit = limit

    @property
    def value(self):
        return self._value

    @property
    def difference(self):
        return self._UNIT_VALUE

    @property
    def remain(self):
        if self._limit:
            return self._limit - self._value
        return None

    def decrease(self):
        self._value -= self._UNIT_VALUE

    def increase(self):
        if not self._limit or self._value + self._UNIT_VALUE <= self._limit:
            self._value += self._UNIT_VALUE
