import random
from pytz import timezone

from chalice import Chalice

app = Chalice(app_name='tank')

app.debug = True


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/info', cors=True)
def info():
    return {
        'name': 'My Tank {!s}'.format(str(timezone('Europe/Amsterdam').zone)),
        'owner': 'PyBCN Dojo'
    }


@app.route('/command', methods=['POST'], cors=True)
def command():
    commands = [
        'turn-left',
        'turn-right',
        'forward',
        'reverse',
        'fire',
        'pass'
    ]
    return {
        'command': random.choice(commands)
    }
