class Fib2(object):
	"""docstring for Fib2"""
	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a, b = b, a + b
		return a

f = Fib2()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[50])