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