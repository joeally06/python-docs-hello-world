from flask import Flask
from flask import render_template
def method_name():
    from flask import jinja2
    return jinja2

jinja2 = method_name()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Jose, Welcome to your first webapp!"


@app.route("/html")
def html():
    return render_template('index.html')