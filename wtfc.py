"""WTFC"""


from os import environ

from flask import Flask, make_response, render_template, request
from requests import get


##### GLOBALS
app = Flask(__name__)
app.config['DEBUG'] = True if environ.get('DEBUG') else False
app.config['OPENCNAM_ACCOUNT_SID'] = environ.get('OPENCNAM_ACCOUNT_SID', '')
app.config['OPENCNAM_AUTH_TOKEN'] = environ.get('OPENCNAM_AUTH_TOKEN', '')

# Cache all static content for 30 days.
CACHE_TIMEOUT = 60 * 60 * 24 * 30

# Default HTTP Cache-Control header content.
app.config['CACHE_CONTROL'] = 'max-age=%s, s-maxage=%s, must-revalidate' % (
       CACHE_TIMEOUT, CACHE_TIMEOUT)


##### VIEWS
@app.route('/')
def index():
    """Look up a person by phone number."""
    name = ''
    number = request.args.get('q')

    if number:
        resp = get('https://api.opencnam.com/v1/phone/%s?format=json' % number,
            auth = (app.config['OPENCNAM_ACCOUNT_SID'], app.config['OPENCNAM_AUTH_TOKEN'])
        )
        name = resp.json['name'] if resp.status_code == 200 else ''
        number = resp.json['number'] if resp.status_code == 200 else number

    return render_template('index.html', name=name, number=number)


@app.route('/robots.txt')
def robots():
    response = make_response(render_template('robots.txt'))
    response.headers['Cache-Control'] = app.config['CACHE_CONTROL']
    response.mimetype = 'text/plain'
    return response


@app.route('/sitemap.xml')
def sitemap():
    response = make_response(render_template('sitemap.xml'))
    response.headers['Cache-Control'] = app.config['CACHE_CONTROL']
    response.mimetype = 'application/xml'
    return response
