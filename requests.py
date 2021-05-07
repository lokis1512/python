import requests
url = input("enter the url : ")
if r.status_code ==200:
	r = requests.get(url)
	print("true")
else:
	print("false")
