'''
Return the factorial of the provided integer.
If the integer is represented with the letter n, a factorial is the product of all positive integers less than or equal to n.
Factorials are often represented with the shorthand notation n!
For example: 5! = 1 * 2 * 3 * 4 * 5 = 120
Only integers greater than or equal to zero will be supplied to the function.
'''

def factorialize(num):
	factor = num
	
	if(num == 0):
		return 1
	else:
		for i in range(1, num):
			factor = factor*i
		
		return factor
		
print(factorialize(5) )
print(factorialize(10) )
print(factorialize(20) )
print(factorialize(0) )