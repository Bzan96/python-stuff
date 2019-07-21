'''
Given a positive integer num, return the sum of all odd Fibonacci numbers that
are less than or equal to num.

The first two numbers in the Fibonacci sequence are 1 and 1. Every additional
number in the sequence is the sum of the two previous numbers. The first six
numbers of the Fibonacci sequence are 1, 1, 2, 3, 5 and 8.

For example, sumFibs(10) should return 10 because all odd Fibonacci numbers
less than or equal to 10 are 1, 1, 3, and 5.
'''

def sumFibs(num):
	fib = [0,1]
	totSum = 0
	
	while(fib[len(fib)-2]<=num):
		fib.append(fib[len(fib)-1]+fib[len(fib)-2])
		
	for i in range(len(fib)-2):
		if fib[i] % 2 != 0:
			totSum+=fib[i]
			
	return totSum
	

	
print(sumFibs(1) )
print(sumFibs(1000) )
print(sumFibs(4000000) )
print(sumFibs(4) )
print(sumFibs(75024) )
print(sumFibs(75025) )