'''
Truncate a string (first argument) if it is longer than the given maximum 
string length (second argument). Return the truncated string with a ... ending.
'''

def truncateString(str, num):
	newStr = ""
	
	if(num >= len(str) ):
		return str			
	else:
		for i in range(num):
			newStr = newStr+str[i]
		
		return newStr + "..."



print(truncateString("A-tisket a-tasket A green and yellow basket", 8) )
print(truncateString("Peter Piper picked a peck of pickled peppers", 11) )
print(truncateString("A-tisket a-tasket A green and yellow basket", len("A-tisket a-tasket A green and yellow basket") ) )
print(truncateString("A-tisket a-tasket A green and yellow basket", len("A-tisket a-tasket A green and yellow basket") + 2) )
print(truncateString("A-", 1) )
print(truncateString("Absolutely Longer", 2) )