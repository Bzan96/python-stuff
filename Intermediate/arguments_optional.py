'''
Create a function that sums two arguments together. If only one argument is
provided, then return a function that expects one argument and returns the sum.

For example, addTogether(2, 3) should return 5, and addTogether(2) should
return a function.

Calling this returned function with a single argument will then return the sum:

var sumTwoAnd = addTogether(2);

sumTwoAnd(3) returns 5.

If either argument isn't a valid number, return undefined.
'''

# Undefined is None in Python
# Need to add commas in between the arguments for this to work in Python
"""
	I'm gonna leave it like this, because technically it works, and it
	gives me an opportunity to really show differences in the languages.
	The second and fifth tests return the "wrong" answer for a JavaScript
	test, but in Python, a list defined inside of parenthesis is a "tuple",
	and while you can add two tuples together, it is like using .concat()
	in JavaScript!
"""

def addTogether(*args):
	argsArr = [*args]
	sum = 0
	
	for arg in argsArr:
		if(type(arg) != int):
			return None
		else:
			sum += arg

	return sum


print(addTogether(2, 3) )
##should return 5.
print(addTogether((2),(3) ) )
##should return 5.
print(addTogether("http://bit.ly/IqT6zt") )
##should return undefined.
print(addTogether(2, "3") )
##should return undefined.
print(addTogether((2),([3]) ) )
##should return undefined.