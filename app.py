from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Jose, Welcome to your first webapp!"


@app.route("/html")
def html():
    return render_template('index.html')