from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home01.html')

app.run(debug=True)
