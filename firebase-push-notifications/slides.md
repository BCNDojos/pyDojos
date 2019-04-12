---
theme : "black"
transition: "zoom"
highlightTheme: "atom-one-dark"
logoImg: "https://raw.githubusercontent.com/evilz/vscode-reveal/master/images/logo-v2.png"
slideNumber: true
---

## April PyBCN Practice Sessions

<span>pythonanywhere.com & firebase push notifications</span>


<small>Ricardo Martinez [@lordrip](http://twitter.com/lordrip)</small>

---

## Who am I?

I'm Ricardo Martinez, I'm a front-end developer (WTF?) that loves JS & Python.
Sharing things keeps a little bit more in touch with the language and the community.
I'm using python for automate task and craft tooling for myself (like the stress-loader for servers)

---

### First things first

--

### What is firebase?

<p>Firebase is set of cloud based services that Google offers with a free tier for testing and personal projects</p>
<p>Today we'll try one of those services, Firebase Messaging. It is a service that allows us to send and receive push notifications on mobiles and web</p>

--

### What is pythonanywhere.com?

<p>pythonanywhere.com is a service that allows us to use python in the cloud; The scope of this service ranges from bash and python terminals, web applications with Django, Flask and more, an instance of MySQL to save data and also allows you to specify tasks that will be executed at certain times.</p>
<p>Luckily for us, they also have a free level to do personal projects.</p>

---

### What are we gonna build?

<iframe src="https://giphy.com/embed/32aOlpp5lG9AyjDBWl" width="480" height="268" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

--

<p>Lets build a simple app with Flask that will receive a web token and store it in a sqlite database and later send push notifications</p>

---

### What are we gonna need?

<ul>
  <li>Flask app</li>
  <li>Notifier</li>
  <li>Serve our app</li>
  <li>Schedule our notifier</li>
</ul>

---

### Flask app

<ul>
  <li>Serve static code (firebase.js, service worker and templates)</li>
  <li>Provide an endpoint for submit the token</li>
</ul>

--

## Simple Flask app

<pre><code class="hljs python">
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask"

app.run()
</code></pre>

--

## Render a template

<pre><code class="hljs python">
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home01.html')

app.run()
</code></pre>

--

## Defining a route

<pre><code class="hljs python">
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post_message():
    return jsonify({ 'message': 'hi there form a POST call' })

app.run()
</code></pre>

---

### Notifier.py

<ul>
  <li>A script that will be triggering push notifications to all users in our database</li>
</ul>

--

## Notifier

<pre><code class="hljs python">
import requests
from models import User
from sqlalchemy import create_engine, orm

def notify_all():
    engine = create_engine('sqlite:///notifications.db')
    session = orm.sessionmaker(bind=engine)()

    for record in session.query(User).all():
        data["to"] = record.token

        req = requests.post(fcm_url, json=data, headers=headers)
        print(req.json())


if __name__ == "__main__":
    notify_all()
</code></pre>

---

## Pythonanywhere

<ul>
  <li>Generate database</li>
  <li>Serve our web app</li>
  <li>Schedule our notifier.py</li>
</ul>

--

### Generate database

<pre><code>
>>> import models
>>> from sqlalchemy import create_engine
>>> engine = create_engine('sqlite:///notifications.db')
>>> models.Base.metadata.create_all(engine)
</code></pre>
