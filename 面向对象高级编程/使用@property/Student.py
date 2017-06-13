# coding:gbk

class Student(object):
	"""docstring for Student"""
	def get_score(self):
		return self._score

	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('score必须是int型')
		if value < 0 or value > 100:
			raise ValueError('score必须在0和100之间')
		self._score = value

s = Student()
s.set_score(60)
print(s.get_score())
s.set_score(1000)