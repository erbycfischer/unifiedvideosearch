import bottle
from bottle import route, run, template

@route('/hello/<name>')
def index(name='World'):
	return template('<b>Hello {{name}}</b>!', name=name)

if __name__ == "__main__":
	run(host='localhost', port=8080)

app = bottle.default_app()
