'''
Repeat a given string str (first argument) for num times (second argument).
Return an empty string if num is not a positive number.
'''

def repeatStringNumTimes(str, num):
	newStr = ""
	
	if num < 0:
		return ""
	else:
		for i in range(num):
			newStr += str
		
	return newStr
	
	
print(repeatStringNumTimes("*", 3) )
print(repeatStringNumTimes("abc", 3) )
print(repeatStringNumTimes("abc", 4) )
print(repeatStringNumTimes("abc", 1) )
print(repeatStringNumTimes("*", 8) )
print(repeatStringNumTimes("abc", -2) )