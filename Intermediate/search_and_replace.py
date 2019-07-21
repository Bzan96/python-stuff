'''
Perform a search and replace on the sentence using the arguments provided
and return the new sentence.

First argument is the sentence to perform the search and replace on.

Second argument is the word that you will be replacing (before).

Third argument is what you will be replacing the second argument with (after).

Note: Preserve the case of the first character in the original word when you
are replacing it. For example if you mean to replace the word "Book" with the
word "dog", it should be replaced as "Dog"
'''

import re

def myReplace(str, before, after):
	newStr = ""
	
	if(re.match(r"([A-Z])", before) ):
		letterName = after[0].upper()
		newAfter = after.replace(after[0], letterName)
		newStr = str.replace(before,newAfter)

	else:
		newStr = str.replace(before,after)
		
	return newStr


print(myReplace("Let us go to the store", "store", "mall") )
print(myReplace("He is Sleeping on the couch", "Sleeping", "sitting") )
print(myReplace("This has a spellngi error", "spellngi", "spelling") )
print(myReplace("His name is Tom", "Tom", "john") )
print(myReplace("Let us get back to more Coding", "Coding", "algorithms") )