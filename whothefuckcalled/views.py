from django.shortcuts import render
from requests import get


def index(request):
    number = request.REQUEST.get('number')
    name = get('https://api.opencnam.com/v2/phone/%s' % number).text if number else ''

    return render(request, 'index.html', {'name': name})
