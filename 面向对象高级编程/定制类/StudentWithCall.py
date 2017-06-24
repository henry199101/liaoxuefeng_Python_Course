# coding:gbk

class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name

	def __call__(self):
		print('我的名字是%s.' % self.name)


s = Student('Mike')
print(s())
print(callable(Student('Mike')))
print(callable(max))
print(callable(None))