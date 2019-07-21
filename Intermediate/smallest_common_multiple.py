'''
Find the smallest common multiple of the provided parameters that can be evenly
divided by both, as well as by all sequential numbers in the range between
these parameters.

The range will be an array of two numbers that will not necessarily be in
numerical order.

For example, if given 1 and 3, find the smallest common multiple of both 1
and 3 that is also evenly divisible by all numbers between 1 and 3.
The answer here would be 6.
'''

def smallestCommons(arr):
	multiArr = []
	bandAidArr = []
	startNum = 1
	smallestMulti = 0
	booControl = False
	
	arr.sort(reverse=True)
	
	for num in range(arr[0],arr[1]-1,-1):
		multiArr.append(num)
	
	
	while(booControl == False):
		smallestMulti = multiArr[0]*startNum*multiArr[1]
		
		for i in range(len(multiArr) ):
			if(smallestMulti % multiArr[i] == 0):
				bandAidArr.append(multiArr[i])
				if(len(bandAidArr) == len(multiArr) ):
					print(bandAidArr)
					booControl = True
			
			if(smallestMulti % multiArr[i] != 0):
				bandAidArr = []
				break
				
	
		startNum+=1
			
	return smallestMulti
	
	
print(smallestCommons([1, 5]) ) # 60
print(smallestCommons([5, 1]) ) # 60
print(smallestCommons([2, 10]) ) # 2520
print(smallestCommons([1, 13]) ) # 360360
print(smallestCommons([23, 18]) ) # 6056820