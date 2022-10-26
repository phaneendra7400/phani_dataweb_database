
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route

@route('/')
def hello_world():
    return 'Hello from venkata sai phaneendra!'

@route('/hi')
def hi_world():
    return 'Hi from Phaneendra!'

@route('/bye')
def bye_world():
    return 'Bye from Phaneendra!'

application = default_app()

