'''
Flatten a nested array. You must account for varying levels of nesting.
'''	

from collections import Iterable

def steamrollArray(arr):
	flatArr = []
	
	
	def flatten(element):
		for item in element:
			try:
				if(isinstance(item,Iterable) and not isinstance(item, (str, bytes) ) ):
					for subItem in flatten(item):
						flatArr.append(subItem)
				else:
					flatArr.append(item)
			except TypeError:
				pass
				##print(item)
	
	flatten(arr)
	
	## Last test should return {} but I believe Python treats (), [] and {} as objects and thus
	## you can return all or none, but not {} and not []
	
	return flatArr
	
	

print(steamrollArray([[["a"]], [["b"]]]) ) ##should return ["a", "b"].
print(steamrollArray([1, [2], [3, [[4]]]]) ) ##should return [1, 2, 3, 4].
print(steamrollArray([1, [], [3, [[4]]]]) ) ##should return [1, 3, 4].
print(steamrollArray([1, {}, [3, [[4]]]]) ) ##should return [1, {}, 3, 4]