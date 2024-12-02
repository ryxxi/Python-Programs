def make_dict(keys, values):

	return {key: value for key,value in zip(keys,values)}

def dictstuff1(my_dict):

	return list(my_dict.values())

print(dictstuff1(make_dict([1,2,3,4,5], ["a","b","c","d","e"])))
