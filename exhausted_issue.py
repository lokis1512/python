import itertools
a = dict(zip("helowsrfd",range(10)))
b = dict(zip("abc",range(1,4)))
for k , v in itertools.izip_longest(a,b,fillvalue = 'iteration exhausted'):
	print(k,v)