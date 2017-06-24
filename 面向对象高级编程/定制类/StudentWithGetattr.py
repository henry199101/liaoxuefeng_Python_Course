class Student2(object):
    def __init__(self):
    	self.name = 'Mike'

s2 = Student2()
print(s2.name)
# print(s2.score)会报错，提示AttributeError: 'Student' object has no attribute 'score'

class Student3(object):
	def __init__(self):
		self.name = 'Henry'

	def __getattr__(self, attr):
		if attr=='score':
			return 99

s3 = Student3()
print(s3.name)
print(s3.score)
# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，
# 这样，我们就有机会返回score的值

class Student4(object):
	def __getattr__(self, attr):
		if attr=='age':
			return lambda:25
		raise AttributeError('\'Student4\'object has no attribute \'%s\'' % attr)

s4 = Student4()
print(s4.age())