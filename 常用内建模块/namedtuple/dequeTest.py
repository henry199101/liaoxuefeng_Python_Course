# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)