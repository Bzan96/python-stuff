'''
The algorithm to convert from Celsius to Fahrenheit is the temperature in Celsius times 
9/5, plus 32. (F=C*9/5+32)
You are given a variable "celsius" representing a temperature in Celsius. Use the variable
"fahrenheit" already defined and assign it the Fahrenheit temperature equivalent to the 
given Celsius temperature. Use the algorithm mentioned above to help convert the Celsius 
temperature to Fahrenheit.
'''

def convertToF(celsius):
	fahrenheit = ((celsius*9)/5)+32
	return fahrenheit
	
print(convertToF(0) )
print(convertToF(-30) )
print(convertToF(-10) )
print(convertToF(20) )
print(convertToF(30) )