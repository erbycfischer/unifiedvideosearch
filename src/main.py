import bottle
from bottle import route, run, template

import configparser

@route('/')
def index():
	return template('''
			<html>
			<head><title>Test</title></head>
			<body>
			<div align=\'center\'>
			<h2>Test site!</h2>
			</div>
			</body>
			</html>
			''')

if __name__ == "__main__":
	run(host='localhost', port=8080)

config = configparser.ConfigParser()
config.read('../redis.ini')

#redis_host = config['redis']['host']
#redis_port = config['redis']['port']

app = bottle.default_app()
