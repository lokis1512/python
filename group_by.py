import itertools

def func(data_list):
	group = itertools.groupby(data_list,key = lambda x : x["country"])
	for country,actual_records in group:
		print(country)
		for record in actual_records:
			print(record)
func(data_list = [{
'country': 'USA', 
'state': 'Colorado', 
'name': 'Ariyana'
}, 
{
'country': 'USA', 
'state': 'Missouri', 
'name': 'Michelle'
}, 
{
'country': 'SA', 
'state': 'Pretoria', 
'name': 'Elon Musk'
},
{
'country': 'SA', 
'state': 'Pretoria', 
'name': 'ABD'
}, 
{
'country': 'Finland', 
'state': 'Helsinky', 
'name': 'Linux Torvalds'
},
 {
	"country": "India",
 	"state": "Bengaluru",
 	"name": "Virat"
 },
 {
 	"country": "India",
 	"state": "Kerala",
 	"name": "Mithun"
 }
])
