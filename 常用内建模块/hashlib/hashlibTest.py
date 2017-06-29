import hashlib

md5_1 = hashlib.md5()
md5_1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5_1.hexdigest())

md5_2 = hashlib.md5()
md5_2.update('how to use md5 in '.encode('utf-8'))
md5_2.update('python hashlib?'.encode('utf-8'))
print(md5_2.hexdigest())