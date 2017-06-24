try:
	print('try...')
	r = 10 / 0
	print('result:', r)

except ZeroDivisionError as e:
	print('except:', e)

finally:
	print('finally...')

print('END')

'''
当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，
即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
上面的代码在计算10 / 0时会产生一个除法运算错误：

try...
except: division by zero
finally...
END

'''

try:
	print('try...')
	r = 10 / 2
	print('result:', r)

except ZeroDivisionError as e:
	print('except:', e)

finally:
	print('finally...')

print('END')

'''
如果把除数0改成2，则执行结果如下：

try...
result: 5
finally...
END
由于没有错误发生，所以except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句）。
'''