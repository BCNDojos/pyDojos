from flaskgame.src.punchservice import PunchService


class MockPunchService(PunchService):

    def __init__(self, inc_value, max_damage=1000):
        self._value = 0
        self._inc_value = inc_value
        self._max_damage = max_damage

    def punch(self):
        self._value += self._inc_value
        if self._value > self._max_damage:
            raise ValueError('Reached maximum punch value')
        return self._value
