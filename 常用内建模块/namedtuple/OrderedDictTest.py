from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

# 注意，OrderedDict的Key会按照插入的顺序排列，
# 不是Key本身排序：

od2 = OrderedDict()
od2['z'] = 1
od2['y'] = 2
od2['x'] = 3
print(list(od2.keys()))