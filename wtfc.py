"""WTFC"""


from os import environ

from flask import Flask, redirect, render_template, request, url_for
from requests import get


##### GLOBALS
app = Flask(__name__)
app.config['OPENCNAM_ACCOUNT_SID'] = environ.get('OPENCNAM_ACCOUNT_SID', '')
app.config['OPENCNAM_AUTH_TOKEN'] = environ.get('OPENCNAM_AUTH_TOKEN', '')


##### VIEWS
@app.route('/')
def index():
    number = request.args.get('number')
    name = get('https://api.opencnam.com/v2/phone/%s?format=pbx&account_sid=%s&auth_token=%s' % number,
            auth=(app.config['OPENCNAM_ACCOUNT_SID'], app.config['OPENCNAM_AUTH_TOKEN'])).text if number else ''
    return render_template('index.html', name=name)
