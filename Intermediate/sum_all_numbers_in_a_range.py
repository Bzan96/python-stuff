'''
We'll pass you an array of two numbers. Return the sum of those two numbers plus the
sum of all the numbers between them.

The lowest number will not always come first.
'''

def sumAll(arr):
	arr.sort()
	
	sumArr = 0
	for i in range(arr[0], arr[1]+1): #arr[1]+1 because the loop runs up TO, but not INCLUDING
		sumArr += i

	return sumArr

print(sumAll([1, 4]) )
print(sumAll([1, 4]) )
print(sumAll([4, 1]) )
print(sumAll([5, 10]) )
print(sumAll([10, 5]) )