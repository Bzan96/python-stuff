'''
Return the provided string with the first letter of each word capitalized.
Make sure the rest of the word is in lower case.
For the purpose of this exercise, you should also capitalize connecting
words like "the" and "of".
'''

def titleCase(str):
	tempArr = str.lower()
	tempArr = tempArr.split(" ")
	newStr = ""
	
	for i in range(len(tempArr) ):
		newStr = newStr + tempArr[i].capitalize()+" "  # Hehe Python... :-)
	
	return newStr
	

	
print(titleCase("I'm a little tea pot") )
print(titleCase("sHoRt AnD sToUt") )
print(titleCase("HERE IS MY HANDLE HERE IS MY SPOUT") )