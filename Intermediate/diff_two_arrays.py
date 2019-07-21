'''
Compare two arrays and return a new array with any items only found in one of the two
given arrays, but not both. In other words, return the symmetric difference of the two
arrays.

Note: You can return the array with its elements in any order.
'''

def diffArray(arr1,arr2):
	newArr = []
	

	for j in range(len(arr1) ):
		if arr1[j] not in arr2:
			newArr.append(arr1[j])
	
	for i in range(len(arr2) ):
		if arr2[i] not in arr1:
			newArr.append(arr2[i])


	return newArr
			
print(diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]) )
print(diffArray(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"]) )
print(diffArray(["andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"]) )
print(diffArray(["andesite", "grass", "dirt", "dead shrub"], ["andesite", "grass", "dirt", "dead shrub"]) )
print(diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]) )
print(diffArray([1, "calf", 3, "piglet"], [1, "calf", 3, 4]) )
print(diffArray([], ["snuffleupagus", "cookie monster", "elmo"]) )
print(diffArray([1, "calf", 3, "piglet"], [7, "filly"]) )