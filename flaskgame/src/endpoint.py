from flask import Flask, request, abort

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

if __name__ == '__main__':
    app.run(debug=True)
