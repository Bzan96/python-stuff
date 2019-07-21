'''
Given the array arr, iterate through and remove each element starting from
the first element (the 0 index) until the function func returns true when
the iterated element is passed through it.

Then return the rest of the array once the condition is satisfied, otherwise,
arr should be returned as an empty array.
'''

# Python code is read linear, the function needs to be defined at the top
# and therefore I need one specific function for each test.
def func(n):
	return n >= 3
	
def funcTwo(n):
	return n == 1

def funcThree(n):
	return n > 0

def funcFour(n):	
	return n > 5
	
def funcFive(n):
	return n > 3
	
def funcSix(n):
	return n > 2

def dropElements(arr, func):
	arrLen = len(arr)
	
	for i in range(arrLen):
		if(func(arr[0]) ):
			return arr
		else:
			arr.pop(0)
			
	return arr


print(dropElements([1, 2, 3, 4], func) )
print(dropElements([0, 1, 0, 1], funcTwo) )
print(dropElements([1, 2, 3], funcThree) )
print(dropElements([1, 2, 3, 4], funcFour) )
print(dropElements([1, 2, 3, 7, 4], funcFive) )
print(dropElements([1, 2, 3, 9, 2], funcSix) )