''' In FreeCodeCamp's exercise you're given a different word, but the algorithm is a
simple one and the idea is that in JavaScript you can utilize arr.split("") and 
arr.reverse() to easily reverse a string.

This is how you do it in Python. '''

def reverseString(str):
	revStr = ""

	for i in str:
		revStr = i+revStr
		
	return revStr
	
	
	
print(reverseString("hello") )
print(reverseString("world") )