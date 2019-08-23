from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from models import db, User

api = Blueprint('api', __name__)


@api.route('/save-token', methods=['POST'])
def save_token():
    token = request.json.get('token')
    user = User(token=token)

    try:
        db.session.add(user)
        db.session.commit()
    except SQLAlchemyError:
        return jsonify({'error': SQLAlchemyError.__name__})

    return jsonify({'token': token})
