import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口：
s.bind(('127.0.0.1', 9999))

s.listen(5)
print('Waiting for connection...')

while True:
	# 接受一个新连接：
	sock, addr = s.accept()
	# 创建新线程来处理TCP连接：
	t = threading.Thread()
	t.start()

def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit' :
			break
		sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('Connection from %s%s closed.' % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接：
s.connect(('127.0.0.0', 9999))
# 接收欢迎消息：
print(s.recv(1024).decode('utf-8'))
for data in [b'Mike', b'Tracy', b'Sarah']:
	# 发送数据：
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()