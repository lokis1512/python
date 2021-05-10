a = "lokesh"
if "loke" in a:
	print("true")
else:
	print("false")
##
def str(a):
	if "loke" in a:
		print("true")
	else:
		print("false")
str("lokesh")

##
import re 
print(dir(re))
def str(a):
	b = re.search("loke" , a)
	if b :
		print("true")
	else:
		print("false")
str("lokesh")