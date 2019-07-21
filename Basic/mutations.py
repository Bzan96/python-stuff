'''
Return true if the string in the first element of the array contains all of
the letters of the string in the second element of the array.
For example, ["hello", "Hello"], should return true because all of the
letters in the second string are present in the first, ignoring case.
The arguments ["hello", "hey"] should return false because the string
"hello" does not contain a "y".
Lastly, ["Alien", "line"], should return true because all of the letters
in "line" are present in "Alien".
'''

def mutation(arr):
	splitStr1 = arr[0].lower()
	splitStr1.split()
	splitStr2 = arr[1].lower()
	splitStr2.split()
	
	for i in range(len(splitStr2) ):
		if not splitStr2[i] in splitStr1:
			return False
	
	
	return True
	
	
	
print(mutation(["hello", "hey"]) )
print(mutation(["hello", "Hello"]) )
print(mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"]) )
print(mutation(["Mary", "Army"]) )
print(mutation(["Mary", "Aarmy"]) )
print(mutation(["Alien", "line"]) )
print(mutation(["floor", "for"]) )
print(mutation(["hello", "neo"]) )
print(mutation(["voodoo", "no"]) )