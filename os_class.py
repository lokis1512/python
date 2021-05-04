import os
a = os.getcwd()
b = input("enter a file : ")
c = os.path.join(a,b)
if os.path.isfile(c):
	print("ok")
else:
	print("create a new file")
	