class Student1(object):
	def __init__(self, name):
		self.name = name

print(Student1('Henry'))


class Student2(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student2 object (name: %s)' % self.name
	__repr__ = __str__

print(Student2('Mike'))