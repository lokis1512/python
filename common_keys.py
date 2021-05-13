def func(d1,d2):
	get_intersection = set(d1.keys()).intersection(d2.keys())
	new_dict = {key:(d1.get(key),d2.get(key)) for key in get_intersection}
	print(new_dict)
func(d1={"a":1,"b":20,"c":3,"d":4},d2={"b":30,"c":40,"e":40})
