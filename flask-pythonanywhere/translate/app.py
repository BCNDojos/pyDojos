import socket
from flask import Flask, jsonify, abort, request
# from db import translateDB
import db

app = Flask(__name__)

@app.route('/words')
def get_all_words():
    result = db.translateDB.get_all_translations()

    return jsonify({ 'words': result }), 200

@app.route('/words/<string:word>')
def get_word(word):
    result = db.translateDB.get_translation(word)

    if result is not None:
        return jsonify({ 'trans': result }), 200

    return jsonify({ 'message': None }), 404

@app.route('/words', methods=['POST'])
def post_word():
    request_data = request.get_json()
    word = request_data.get('word')
    trans = request_data.get('trans')

    if word and trans:
        db.translateDB.add_translation(word, trans)
        return jsonify({ word: trans }), 200

    return jsonify({ 'message': 'error' }), 400

@app.route('/words/<string:word>', methods=['PUT'])
def put_word(word):
    request_data = request.get_json()
    trans = request_data.get('trans')

    if word and trans:
        if db.translateDB.get_translation(word) is not None:
            db.translateDB.update_translation(word, trans)
            return jsonify({ word: trans }), 200

        return jsonify({ 'message': 'error' }), 404

    return jsonify({ 'message': 'error' }), 400

@app.route('/words/<string:word>', methods=['DELETE'])
def delete_word(word):
    if word:
        if db.translateDB.get_translation(word) is not None:
            db.translateDB.remove_translation(word)
            return jsonify({ 'message': 'deleted' }), 200

        return jsonify({ 'message': 'error' }), 404

    return jsonify({ 'message': 'error' }), 400

if 'live' not in socket.gethostname():
    app.run(debug=True)
