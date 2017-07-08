from flaskgame.src.punchservice import PunchService


class FightValue:

    MIN_DAMAGE = 0
    MAX_PUNCHES = 25

    def __init__(self, punch_service: PunchService):
        self._current_damage = self.MIN_DAMAGE
        self._punch_service = punch_service
        self._punch_counter = 1

    @property
    def current_damage(self):
        return self._current_damage

    def punch(self):
        if self._punch_counter >= self.MAX_PUNCHES:
            self._current_damage = self.MIN_DAMAGE
            return
        try:
            self._current_damage = self._punch_service.punch()
            self._punch_counter += 1
        except ValueError:
            self._current_damage = self.MIN_DAMAGE

