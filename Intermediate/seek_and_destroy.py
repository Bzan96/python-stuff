'''
You will be provided with an initial array (the first argument in the destroyer function), followed by one or more arguments. Remove all elements from the initial array that are of the same value as these arguments.

Note: You have to use the arguments object. (*args in Python)
'''

# Unclear if it's actually possible to just pass in (arr) as in the JavaScript example:
# function destroyer(arr) where
# destroyer([1, 2, 3, 1, 2, 3], 2, 3);
def destroyer(arr,*args):
	tempArr = [*args]
	newArr = list(filter(lambda num: num not in tempArr, arr) )

	return newArr






print(destroyer([1, 2, 3, 1, 2, 3], 2, 3) )
print(destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3) )
print(destroyer([3, 5, 1, 2, 2], 2, 3, 5) )
print(destroyer([2, 3, 2, 3], 2, 3) )
print(destroyer(["tree", "hamburger", 53], "tree", 53) )
print(destroyer(["possum", "trollo", 12, "safari", "hotdog", 92, 65, "grandma", "bugati", "trojan", "yacht"], "yacht", "possum", "trollo", "safari", "hotdog", "grandma", "bugati", "trojan") )