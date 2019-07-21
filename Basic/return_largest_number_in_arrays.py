'''
Return an array consisting of the largest number from each provided sub-array.
For simplicity, the provided array will contain exactly 4 sub-arrays.
Remember, you can iterate through an array with a simple for loop, and access each 
member with array syntax arr[i].
'''

def largestOfFour(arr):
	largestNums = []
	
	for i in range(len(arr) ):
		tempVar = arr[i][0]
		
		for j in range(len(arr[i]) ):
			if(arr[i][j] > tempVar):
				tempVar = arr[i][j]
		
		largestNums.append(tempVar)
	
	return largestNums
	

	
print(largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]) )
print(largestOfFour([[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]) )
print(largestOfFour([[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]]) )
print(largestOfFour([[17, 23, 25, 12], [25, 7, 34, 48], [4, -10, 18, 21], [-72, -3, -17, -10]]) )