'''
You are given two arrays and an index.
Use the array methods slice and splice to copy each element of the first 
array into the second array, in order.
Begin inserting elements at index n of the second array.
Return the resulting array. The input arrays should remain the same after
the function runs.
'''

# This one is troublesome since strings are inmutable in Python and
# .splice() doesn't exist.
# Therefore: loop through each element in arr2 until n is reached.
# Then copy in each element from arr1
# Then continue the loop (a new loop) to add the rest of the elements
# from arr2. It starts at n.

def frankenSplice(arr1, arr2, n):
	# Pointless since we can't use splice().
	# newArr = arr2[slice(0, len(arr2) )]
	newArr = []
	
	for i in range(n):
		newArr.append(arr2[i])
		
	for j in range(len(arr1) ):
		newArr.append(arr1[j])
		
	for k in range(n, len(arr2)):
		newArr.append(arr2[k])
		
	return newArr
	
	
	
	
print(frankenSplice([1, 2, 3], [4, 5], 1) )
print(frankenSplice([1, 2], ["a", "b"], 1) )
print(frankenSplice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2) )