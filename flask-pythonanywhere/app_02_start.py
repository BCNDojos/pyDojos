from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('<h1>Hi from Flask</h1>')

app.run()
