"""WTFC"""


from flask import Flask, redirect, render_template, request, url_for
from requests import get


##### GLOBALS
app = Flask(__name__)


##### VIEWS
@app.route('/')
def index():
    number = request.args.get('number')
    name = get('https://api.opencnam.com/v2/phone/%s?format=pbx' % number) if number else ''
    return render_template('index.html', name=name)
