# coding:utf-8

class MyObject(object):
	"""docstring for MyOb"""
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x')) # ÓĞÊôĞÔxÂğ

print(obj.x)

print(hasattr(obj, 'y'))

setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))

print(getattr(obj, 'y'))

print(obj.y)

getattr(obj, 'z')
