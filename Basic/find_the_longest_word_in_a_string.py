'''
Return the length of the longest word in the provided sentence.
Your response should be a number.
'''

def findLongestWordLength(str):
	splitStr = str.split(" ")
	longestWord = ""

	for word in range(1, len(splitStr) ):
		if(len(splitStr[word]) > len(longestWord) ):
			longestWord = splitStr[word]
			
	return len(longestWord)

print(findLongestWordLength("The quick brown fox jumped over the lazy dog") )
print(findLongestWordLength("May the force be with you") )
print(findLongestWordLength("Google do a barrel roll") )
print(findLongestWordLength("What is the average airspeed velocity of an unladen swallow") )
print(findLongestWordLength("What if we try a super-long word such as otorhinolaryngology") )