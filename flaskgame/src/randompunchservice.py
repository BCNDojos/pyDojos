import random

from flaskgame.src.punchservice import PunchService


class RandomPunchService(PunchService):

    def __init__(self, min_value, max_damage):
        self._min_value = min_value
        self._max_damage = max_damage

    def punch(self):
        self._min_value = random.randrange(self._min_value, self._max_damage + 1)
        if self._min_value >= self._max_damage:
            raise ValueError('Reached maximum punch value')
        return self._min_value
