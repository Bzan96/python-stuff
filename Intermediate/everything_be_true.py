'''
Check if the predicate (second argument) is truthy on all elements of a
collection (first argument).

In other words, you are given an array collection of objects. The predicate
pre will be an object property and you need to return true if its value is
truthy. Otherwise, return false.

In JavaScript, truthy values are values that translate to true when evaluated
in a Boolean context.

Remember, you can access object properties through either dot notation or
[]notation.
'''

def truthCheck(collection, pre):
	falsyValues = [None, 0, ""]

	for i in collection:
		for key in i.keys():
			if pre not in i.keys():
				return False
			else:
				for value in i.values():
					if key == pre and value in falsyValues:
						return False
						


	return True

print(truthCheck([{"user": "Tinky-Winky", "sex": "male"}, {"user": "Dipsy", "sex": "male"}, {"user": "Laa-Laa", "sex": "female"}, {"user": "Po", "sex": "female"}], "sex") )
##should return true.
print(truthCheck([{"user": "Tinky-Winky", "sex": "male"}, {"user": "Dipsy"}, {"user": "Laa-Laa", "sex": "female"}, {"user": "Po", "sex": "female"}], "sex") )
##should return false.
print(truthCheck([{"user": "Tinky-Winky", "sex": "male", "age": 0}, {"user": "Dipsy", "sex": "male", "age": 3}, {"user": "Laa-Laa", "sex": "female", "age": 5}, {"user": "Po", "sex": "female", "age": 4}], "age") )
##should return false.
print(truthCheck([{"name": "Pete", "onBoat": True}, {"name": "Repeat", "onBoat": True}, {"name": "FastFoward", "onBoat": None}], "onBoat") )
##should return false
print(truthCheck([{"name": "Pete", "onBoat": True}, {"name": "Repeat", "onBoat": True, "alias": "Repete"}, {"name": "FastFoward", "onBoat": True}], "onBoat") )
##should return true
print(truthCheck([{"single": "yes"}], "single") )
##should return true
print(truthCheck([{"single": ""}, {"single": "double"}], "single") )
##should return false
print(truthCheck([{"single": "double"}, {"single": None}], "single") )
##should return false
print(truthCheck([{"single": "double"}, {"single": None}], "single") )
##should return false