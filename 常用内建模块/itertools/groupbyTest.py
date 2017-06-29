import itertools
for key, group in itertools.groupby('AAABBBCCAAA'):
	print(key, list(group))