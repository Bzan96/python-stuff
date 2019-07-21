'''
Check if a value is classified as a boolean primitive. Return true or false.
Boolean primitives are true and false.
'''

# Needed to check if argument is a number
import math

# Changed passed argument from 'bool' to 'argument' because 'bool is an actual
# keyword in Python.
def booWho(argument):
	if(isinstance(argument, bool) == True):
		print("true")
	else:
		print("false")
		

		
booWho(True)
booWho(False)
booWho([1, 2, 3])
booWho(slice([]) ) # Changed to fit Python
booWho({ "a": 1 })
booWho(1)
booWho(math.isnan) # Changed to fit Python
booWho("a")
booWho("true")
booWho("false")