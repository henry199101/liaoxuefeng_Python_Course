# hello.py

def application(environ, start_response):
	start_response('200 0K', [('Content-Type', 'text/html')])
	return [b'<h1>Hello, Henry!</h1>']