import random

from flask import Flask, request, abort, render_template

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
    if request.method == 'DELETE':
        fight = None
        final_score = 0
    _update_score()
    is_ready = True
    return _render(message='Fight ready to start!', score=final_score)


@app.route('/fight', methods=['POST', 'PUT', 'GET', 'DELETE'])
def fighting():
    global fight, final_score
    if request.method not in ['POST', 'PUT', 'GET', 'DELETE']:
        return abort(405)

    query_args = request.args.to_dict()

    if request.method == 'POST':
        return _start()

    if request.method == 'PUT':
        multiplier = None
        whining_choices = None
        if request.is_json:
            request_data = request.json
        else:
            request_data = request.form
        if 'multiplier' in request_data:
            multiplier = int(request_data['multiplier'])
        if 'whining_choices' in request_data:
            whining_choices = request_data['whining_choices']
        return _punch(multiplier, whining_choices)

    if request.method == 'GET':
        return _score(query_args)

    if request.method == 'DELETE':
        return _end()


def _update_score():
    global fight, final_score
    if fight:
        final_score = fight.current_damage


def _render(with_template=True, **kwargs):
    if with_template:
        return render_template('index.html', **kwargs)
    else:
        if 'message' in kwargs:
            return kwargs['message']


def _end():
    global fight, final_score
    if fight:
        final_score = fight.current_damage
        fight = None
    return _render(False, message='Fight ended')


def _score(query_args):
    global fight
    score_prefix = ''
    if 'score_prefix' in query_args:
        score_prefix = query_args['score_prefix']
    _update_score()
    score_value = final_score
    if fight:
        score_value = fight.current_damage
    return _render(False, message='{!s}{:d}'.format(score_prefix, score_value))


def _punch(multiplier, whining_choices=None):
    global fight

    if not fight:
        return abort(400)

    if not whining_choices:
        whining_choices = ['Uuuffh', 'Oughhh', 'Aix', 'Pufghfs']
    if not multiplier:
        multiplier = 1

    while multiplier:
        fight.punch()
        multiplier -= 1

    damage = fight.current_damage
    whining = random.choice(whining_choices)
    return _render(False, message='{!s} ({:d})'.format(whining, damage))


def _start():
    global fight
    if fight:
        return abort(400)
    puncher = RandomPunchService(min_value=0, max_damage=100)
    fight = FightValue(punch_service=puncher)
    return _render(False, message='Fighting!!')


if __name__ == '__main__':
    app.run(debug=True)
