'''
Translate the provided string to pig latin.

Pig Latin takes the first consonant (or consonant cluster) of an English word,
moves it to the end of the word and suffixes an "ay".

If a word begins with a vowel you just add "way" to the end.

Input strings are guaranteed to be English words in all lowercase.
'''

import re

def translatePigLatin(str):
	vowelPos = 0
	newStr = ""
	
	if re.search(r"[aeiou]", str, re.X):
		if re.match(r"[aeiou]",str[0]):
			return str+"way";
		else:
			for i in str:
				if re.match(r"[aeiou]", i):
					vowelPos = str.index(i)
					for j in range(vowelPos, len(str) ):
						newStr += str[j]
					
					for k in range(vowelPos):
						newStr += str[k]
					break
		
		return newStr + "ay"
	
	else:
		return str + "ay"




print(translatePigLatin("california") )
print(translatePigLatin("paragraphs") )
print(translatePigLatin("glove") )
print(translatePigLatin("algorithm") )
print(translatePigLatin("eight") )
#Should handle words where the first vowel comes in the end of the word.
#Should handle words without vowels.