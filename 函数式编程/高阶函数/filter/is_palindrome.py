# 练习

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：

# -*- coding: utf-8 -*-

def is_palindrome(n):
    for i in range( int(n/2) ):
        return str(n)[i] == str(n)[-i-1]

# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))
