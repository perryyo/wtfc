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
    """Look up a person by phone number."""
    name = ''
    number = request.args.get('q')

    if number:
        resp = get('https://api.opencnam.com/v2/phone/%s?format=json' % number,
            auth = (app.config['OPENCNAM_ACCOUNT_SID'], app.config['OPENCNAM_AUTH_TOKEN'])
        )
        name = resp.json['name'] if resp.status == 200 else ''
        number = resp.json['number'] if resp.status == 200 else number

    return render_template('index.html', name=name, number=number)
