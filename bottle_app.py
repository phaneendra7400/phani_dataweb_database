
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

@route('/list')
def get_list():
    cursor = connection.cursor()
    rows = cursor.execute("select id, description from list")
    rows = list(rows)
    rows = [ {'id':row[0] ,'desc':row[1]} for row in rows ]
    return template("bike_list.tpl", name="phaneendra", bike_list=rows)

application = default_app()

