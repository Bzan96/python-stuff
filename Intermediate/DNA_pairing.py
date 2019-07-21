'''
The DNA strand is missing the pairing element. Take each character, get its
pair, and return the results as a 2d array.

Base pairs are a pair of AT and CG. Match the missing element to the provided
character.

Return the provided character as the first element in each array.

For example, for the input GCG, return [["G", "C"], ["C","G"],["G", "C"]]

The character and its pair are paired up in an array, and all the arrays are
grouped into one encapsulating array.
'''

def pairElement(str):
	dnaString = []
	
	for letter in str:
		if(letter == "A"):
			dnaString.append(["A","T"])
		elif(letter == "T"):
			dnaString.append(["T","A"])
		elif(letter == "C"):
			dnaString.append(["C","G"])
		elif(letter == "G"):
			dnaString.append(["G","C"])
		
	return dnaString


print(pairElement("GCG") )
print(pairElement("ATCGA") )
print(pairElement("TTGAG") )
print(pairElement("CTCTA") )