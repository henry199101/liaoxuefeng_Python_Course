# app.py

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

# 制作响应函数
def index(request):
	return web.Response(body=b'<h1>Hello,wolrd. I&apos;m Henry.</h1>', content_type='text/html') 
	# content_type解决打开网页后变成下载的问题

@asyncio.coroutine
def init(loop): # Web app服务器初始化
	app = web.Application(loop=loop) # 制作响应函数集合
	app.router.add_route('GET', '/', index) # 把响应函数添加到响应函数集合
	srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
	logging.info('server started at http://127.0.0.1:9000...') # 创建服务器(连接网址、端口，绑定handler)
	return srv

loop = asyncio.get_event_loop() # 创建事件
loop.run_until_complete(init(loop)) # 运行
loop.run_forever() # 服务器不关闭

app = web.Application(loop=loop, middlewares=[
	logger_factory, response_factory
])
init_jinja2(app, filters=dict(datetime=datetime_filter))
add_routes(app, 'handlers')
add_static(app)

@asyncio.coroutine
def logger_factory(app, handler):
	@asyncio.coroutine
	def logger(request):
		# 记录日志:
		logging.info('Request: %s %s' % (request.method, request.path))
		# 继续处理请求:
		return (yield from handler(request))
	return logger

@asyncio.coroutine
def response_factory(app, handler):
	@asyncio.coroutine
	def response(request):
		# 结果:
		r = yield from handler(request)
		if isinstance(r, web.StreamResponse):
			return r
		if isinstance(r, bytes):
			resp = web.Response(body=r)
			resp.content_type = 'application/octet-stream'
			return resp
		if isinstance(r, str):
			resp = web.Response(body=r.encode('utf-8'))
			resp.content_type = 'text/html;charset=utf-8'
			return resp
		if isinstance(r, dict):
			...












