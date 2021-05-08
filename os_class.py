import os
import subprocess
a = os.getcwd()
b = input("enter a file : ")
c = os.path.join(a,b)
if os.path.isfile(c):
	print("file exist")
else:
	subprocess.call(["touch",c])
	print("file does not exist")

