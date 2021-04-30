import json
with open("old.json","r") as f:
	data = json.load(f)

with open("new.json","w") as l:
	json.dump(data,l)

