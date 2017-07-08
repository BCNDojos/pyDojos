import unittest

from flaskgame.src.fightvalue import FightValue
from flaskgame.tests.mockpunchservice import MockPunchService


class TestFight(unittest.TestCase):

    def setUp(self):
        pass

    def test_punches_limit(self):
        puncher = MockPunchService(1)
        fight = FightValue(puncher)
        counter = 1
        while counter < FightValue.MAX_PUNCHES:
            fight.punch()
            counter += 1
        assert counter == FightValue.MAX_PUNCHES
        fight.punch()
        assert fight.current_damage == FightValue.MIN_DAMAGE

    def test_damage_limit(self):
        INC_VALUE = 20
        MAX_DAMAGE = 100
        puncher = MockPunchService(INC_VALUE, MAX_DAMAGE)
        fight = FightValue(puncher)
        counter = 1
        while counter <= 5:
            fight.punch()
            counter += 1
        assert fight.current_damage == MAX_DAMAGE
        fight.punch()
        assert fight.current_damage == FightValue.MIN_DAMAGE

if __name__ == '__main__':
    unittest.main()
