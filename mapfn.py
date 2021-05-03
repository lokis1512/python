a = [ 1, 2, 3, 4 ]
b = []
for i in a:
	c = (i**2)
	b.append(c)
print(b)


#using map

def func(element):
	return element*element
d = list(map(func,[1,2,3,4]))
print(d)