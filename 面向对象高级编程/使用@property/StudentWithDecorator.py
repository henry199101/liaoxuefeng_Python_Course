# coding:utf-8

class Student(object):
	"""docstring for Student"""
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score必须是int型')
		if value < 0 or value > 100:
			raise ValueError('score必须在0和100之间')
		self._score = value

s = Student()
s.score = 60
print(s.score)
s.score = 999