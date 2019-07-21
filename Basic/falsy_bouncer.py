'''
Remove all falsy values from an array.
Falsy values in JavaScript are false, null, 0, "", undefined, and NaN.
Hint: Try converting each value to a Boolean.
'''

# Needed to see if something is a number
import math

def bouncer(arr):
	# Both null and undefined translate to None in Python
	falsyValues = [False, None, 0, "", math.isnan]
	filteredArr = []
	
	for i in range(len(arr) ):
		if arr[i] not in falsyValues:
			filteredArr.append(arr[i])
			
	return filteredArr
	
	
	
print(bouncer([7, "ate", "", False, 9]) )
print(bouncer(["a", "b", "c"]) )
print(bouncer([False, None, 0, math.isnan, None, ""]) )
print(bouncer([1, None, math.isnan, 2, None]) )