"""WTFC"""


from flask import Flask, redirect, render_template, url_for


##### GLOBALS
app = Flask(__name__)


##### VIEWS
@app.route('/')
def index():
    return render_template('index.html')
