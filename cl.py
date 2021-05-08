a = ["1","1","2","3","4","4"]
b = {}
for d in a:
    if d in b:
        b[d] =b[d] + 1
    else:
        b[d] = 1
print(b) 

import collections
a = [ 1, 1, 2, 3, 4, 4]
print(collections.Counter(a))
        
        
