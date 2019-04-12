from flask import Blueprint, render_template
from models import get_list

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')


@views.route('/list')
def list():
    token_list = get_list()
    return render_template('list.html', token_list=token_list)
