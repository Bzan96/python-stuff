'''
Sum all the prime numbers up to and including the provided number.

A prime number is defined as a number greater than one and having only two
divisors, one and itself. For example, 2 is a prime number because it's only
divisible by one and two.

The provided number may not be a prime.
'''

# The variable 'boo' is a bandaid-fix to stop the looping
## Sidenote: Do people not realise that the formula "prime=(X % 2 === 0)"
## doesn't actually give us prime numbers, but ALL odd numbers?

def sumPrimes(num):
	primeArr = []
	sum = 0
	boo = False
	
	primeArr.append(2)

	for i in range(3,num+1,2):
		if boo==False:
			for j in primeArr:
				if (i % j == 0):
					boo = True
			if boo == False:
				primeArr.append(i)
				
		boo = False
	
	for num in primeArr:
		sum+=num

	return sum
	

		
print(sumPrimes(10) )
print(sumPrimes(977) )