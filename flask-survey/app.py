from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'for'
debug = DebugToolbarExtension(app)

@app.route("/")
def home_page():
    return("Home Page")