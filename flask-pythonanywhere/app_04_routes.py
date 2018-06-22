from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({ 'message': 'hi there' })

@app.route('/get', methods=['GET'])
def get_message():
    return jsonify({ 'message': 'hi there form a GET call' })

@app.route('/post', methods=['POST'])
def post_message():
    return jsonify({ 'message': 'hi there form a POST call' })

@app.route('/put', methods=['PUT'])
def put_message():
    return jsonify({ 'message': 'hi there form a PUT call' })

@app.route('/delete', methods=['DELETE'])
def delete_message():
    return jsonify({ 'message': 'hi there form a DELETE call' })

@app.route('/test')
def test():
    return jsonify({ 'message': 'I\'m a Teapot!' }), 418

app.run(debug=True)
