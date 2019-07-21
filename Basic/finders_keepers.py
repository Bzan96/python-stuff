'''
Create a function that looks through an array (first argument) and returns
the first element in the array that passes a truth test (second argument).
If no element passes the test, return undefined.
'''

def findElement(arr, func):
	
	for i in range(len(arr) ):
		if func(arr[i]):
			return arr[i]
			
	if not func(arr[i]):
		return "undefined"

		
# Had to write my own "func" because Python doesn't have arrow functions
def modCheck(num):
	if(num % 2 == 0):
		return True
	
print(findElement([1, 2, 3, 4], modCheck) )
print(findElement([1, 3, 5, 8, 9, 10], modCheck) )
print(findElement([1, 3, 5, 9], modCheck) )