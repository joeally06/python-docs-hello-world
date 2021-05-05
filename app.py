from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Jose, Welcome to your first webapp!"


@app.route("/html")
def index():
    return render_template ('index.html')