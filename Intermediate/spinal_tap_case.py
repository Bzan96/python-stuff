'''
Convert a string to spinal case.
Spinal case is all-lowercase-words-joined-by-dashes.
'''

# Need to import the regex library
import re

def spinalCase(str):
	str = re.sub(r"(?=([A-Z]))|\s|\_+", "-", str)
	noSpaceStr = ""

	for char in str:
		if(str[0] == "-" and len(noSpaceStr) < 1):
			noSpaceStr += " "
		else:
			noSpaceStr += char
			
	return noSpaceStr.lstrip().lower()

print(spinalCase("This Is Spinal Tap") ) ##should return "this-is-spinal-tap"
print(spinalCase("thisIsSpinalTap") ) ##should return "this-is-spinal-tap"
print(spinalCase("The_Andy_Griffith_Show") ) ##should return "the-andy-griffith-show"
print(spinalCase("Teletubbies say Eh-oh") ) ##should return "teletubbies-say-eh-oh"
print(spinalCase("AllThe-small Things") ) ##should return "all-the-small-things"