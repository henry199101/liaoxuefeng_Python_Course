# appTest.py
'''
Run a Simple Web Server
In order to implement a web server, first create a request handler.
'''
'''
A request handler is a coroutine or regular function that 
accepts a Request instance as its only parameter and returns a Response instance:
'''
from aiohttp import web

async def hello(request):
	return web.Response(text="Hello, world")
'''
Next, create an Application instance and register the request handler 
with the application’s router on a particular HTTP method and path:
'''
appTest = web.Application()
appTest.router.add_get('/', hello)
'''
That’s it. Now, head over to http://localhost:8080/ to see the results.
'''