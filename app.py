from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Jose, Welcome to your first webapp!"


@app.route("/")
def index():
    return 'index.html'