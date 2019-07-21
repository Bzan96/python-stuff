'''
Make a function that looks through an array of objects (first argument) and returns
an array of all objects that have matching name and value pairs (second argument).
Each name and value pair of the source object has to be present in the object from the
collection if it is to be included in the returned array.

For example, if the first argument is [{ first: "Romeo", last: "Montague" },
{ first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }],
and the second argument is { last: "Capulet" }, then you must return the third object
from the array (the first argument), because it contains the name and its value, that
was passed on as the second argument.
'''

def whatIsInAName(collection, source):
	arr = []
	sourceKeys = list(source.keys() )
	sourceValues = list(source.values() )
	
	keys = []
	for entry in collection:
		keys.append(entry.keys() )
		
	count = 0
	
	for i in range(len(keys) ):
		for j in range(len(sourceKeys) ):
			if(sourceKeys[j] in keys[i]):
				count += 1

		if(count == len(sourceKeys) ):
			arr.append(collection[i])
			
		count = 0
		
	newArr = []
	filtered = []
	
	for key in arr[0].keys():
		filtered.append(key)
		
	for input in arr:
		srcInc = 0
		count = 0
		for item in input.items():
			if(item in source.items() ):
				count += 1
						
		srcInc += 1
					
		if(count == len(sourceKeys) ):
			newArr.append(input)
				
				
				
	return newArr


	
print(whatIsInAName([{ "first": "Romeo", "last": "Montague" }, { "first": "Mercutio", "last": None }, { "first": "Tybalt", "last": "Capulet" }], { "last": "Capulet" }) )
##should return [{ first: "Tybalt", last: "Capulet" }]
print(whatIsInAName([{ "apple": 1 }, { "apple": 1 }, { "apple": 1, "bat": 2 }], { "apple": 1 }) )
##should return [{ "apple": 1 }, { "apple": 1 }, { "apple": 1, "bat": 2 }]
print(whatIsInAName([{ "apple": 1, "bat": 2 }, { "bat": 2 }, { "apple": 1, "bat": 2, "cookie": 2 }], { "apple": 1, "bat": 2 }) )
##should return [{ "apple": 1, "bat": 2 }, { "apple": 1, "bat": 2, "cookie": 2 }]
print(whatIsInAName([{ "apple": 1, "bat": 2 }, { "apple": 1 }, { "apple": 1, "bat": 2, "cookie": 2 }], { "apple": 1, "cookie": 2 }) )
##should return [{ "apple": 1, "bat": 2, "cookie": 2 }]
print(whatIsInAName([{ "apple": 1, "bat": 2 }, { "apple": 1 }, { "apple": 1, "bat": 2, "cookie": 2 }, { "bat":2 }], { "apple": 1, "bat": 2 }) )
##should return [{ "apple": 1, "bat": 2 }, { "apple": 1, "bat": 2, "cookie":2 }]
print(whatIsInAName([{"a": 1, "b": 2, "c": 3}], {"a": 1, "b": 9999, "c": 3}) )
## should return []