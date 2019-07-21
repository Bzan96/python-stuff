'''
Find the missing letter in the passed letter range and return it.

If all letters are present in the range, return undefined (None in Python).
'''

def fearNotLetter(str):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	startIter = alphabet.find(str[0])
	
	for i in range(len(str) ):
		if(str[i] != alphabet[startIter+i]):
			return alphabet[startIter+i]

	return None;

print(fearNotLetter("abce") )
print(fearNotLetter("abcdefghjklmno") )
print(fearNotLetter("stvwx") )
print(fearNotLetter("bcdf") )
print(fearNotLetter("abcdefghijklmnopqrstuvwxyz") )