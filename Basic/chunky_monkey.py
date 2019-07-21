'''
Write a function that splits an array (first argument) into groups the length
of size (second argument) and returns them as a two-dimensional array.
'''

def chunkArrayInGroups(arr, size):
	newArr = []
	tempArr = []
	
	for i in range(len(arr) ):
		# Controls the size of each array. When i reaches a number that's
		# evenly divisible by whatever number size-1 is, a new array is created
		# , until len(arr) is reached. We use size-1 because the array count
		# starts at 0 and not 1.
		if(i % size != size-1):
			tempArr.append(arr[i])
		else:
			tempArr.append(arr[i])
			newArr.append(tempArr)
			tempArr = []
	
	# If "size" is greater than len(arr), the remaining numbers are passed
	# into the outer array.
	if(len(tempArr) != 0):
		newArr.append(tempArr)
	
	return newArr
	
	
	
print(chunkArrayInGroups(["a", "b", "c", "d"], 2) )
print(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 3) )
print(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 2) )
print(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 4) )
print(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6], 3) )
print(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 4) )
print(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 2) )