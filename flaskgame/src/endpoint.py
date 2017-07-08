import random

from flask import Flask, request, abort

from flaskgame.src.fightvalue import FightValue
from flaskgame.src.randompunchservice import RandomPunchService

app = Flask(__name__)

is_ready = None
fight = None
final_score = 0


@app.route('/', methods=['GET', 'DELETE'])
def ready():
    global is_ready, fight, final_score
    if request.method not in ['GET', 'DELETE']:
        return abort(405)
    if is_ready and request.method == 'GET':
        return abort(400)
    else:
        # Reset fight on DELETE
        fight = None
        final_score = 0
    is_ready = True
    return 'Fight ready to start!\n'


@app.route('/fight', methods=['POST', 'PUT', 'GET', 'DELETE'])
def fighting():
    global fight, final_score
    if request.method not in ['POST', 'PUT', 'GET', 'DELETE']:
        return abort(405)

    query_args = request.args.to_dict()

    if request.method == 'POST':
        return _start()

    if request.method == 'PUT':
        multiplier = request.form.get('multiplier', type=int)
        return _punch(multiplier)

    if request.method == 'GET':
        return _score(query_args)

    if request.method == 'DELETE':
        return _end()


def _end():
    global fight, final_score
    if fight:
        final_score = fight.current_damage
        fight = None
    return 'Fight ended\n'


def _score(query_args):
    global fight
    score_prefix = ''
    if 'score_prefix' in query_args:
        score_prefix = query_args['score_prefix']
    score_value = final_score
    if fight:
        score_value = fight.current_damage
    return '{!s}{:d}\n'.format(score_prefix, score_value)


def _punch(multiplier):
    global fight
    if not fight:
        return abort(400)
    if not multiplier:
        multiplier = 1
    while multiplier:
        fight.punch()
        multiplier -= 1
    damage = fight.current_damage
    whining = random.choice(['Uuuffh', 'Oughhh', 'Aix', 'Pufghfs'])
    return '{!s} ({:d})\n'.format(whining, damage)


def _start():
    global fight
    if fight:
        return abort(400)
    puncher = RandomPunchService(min_value=0, max_damage=100)
    fight = FightValue(punch_service=puncher)
    return 'Fighting!!\n'


if __name__ == '__main__':
    app.run(debug=True)
