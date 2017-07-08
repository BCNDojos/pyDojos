import random

from flask import Flask, request, abort

from flaskgame.src.fightvalue import FightValue
from flaskgame.src.randompunchservice import RandomPunchService

app = Flask(__name__)

is_ready = None
fight = None


@app.route('/', methods=['GET', 'DELETE'])
def ready():
    global is_ready, fight
    if request.method not in ['GET', 'DELETE']:
        return abort(405)
    if is_ready and request.method == 'GET':
        return abort(400)
    else:
        # Reset fight on DELETE
        fight = None
    is_ready = True
    return 'Fight ready to start!\n'


@app.route('/fight', methods=['POST', 'PUT', 'GET', 'DELETE'])
def fighting():
    global fight
    if request.method not in ['POST', 'PUT', 'GET', 'DELETE']:
        return abort(405)

    if request.method == 'POST':
        if fight:
            return abort(400)
        puncher = RandomPunchService(min_value=0, max_damage=100)
        fight = FightValue(punch_service=puncher)
        return 'Fighting!!\n'

    if request.method == 'PUT':
        if not fight:
            return abort(400)
        fight.punch()
        damage = fight.current_damage
        whining = random.choice(['Uuuffh', 'Oughhh', 'Aix', 'Pufghfs'])
        return '{!s} ({:d})\n'.format(whining, damage)


if __name__ == '__main__':
    app.run(debug=True)
