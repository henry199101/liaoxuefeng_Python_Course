'''
try:
	f = open('test.txt', 'r')
	print(f.read())

finally:
	if f:
		f.close()
'''

with open('test.txt', 'r') as f:
	print(f.read())