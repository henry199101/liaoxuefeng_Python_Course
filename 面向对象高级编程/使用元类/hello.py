class  Hello(object):
	"""docstring for  Hello"""
	def hello(self, name='world'):
		print('Hello, %s.' % name)


# from hello import Hello
h = Hello()
h.hello()

print(type(Hello))
print(type(h))