import re

def rot13(str):
	regex = r"\w"
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	realSentence = ""
	
	for i in range(len(str) ):
		if re.match(regex, str[i]):
			for j in range(len(alphabet) ):
				if re.match(alphabet[j], str[i]):
					if(j+13 >= 26):
						realSentence += alphabet[j+13-26]
					else:
						realSentence += alphabet[j+13]
						
		else:
			realSentence += str[i]
			
	return realSentence
	
	
	
print(rot13("SERR PBQR PNZC") ) ##should decode to FREE CODE CAMP
print(rot13("SERR CVMMN!") ) ##should decode to FREE PIZZA!
print(rot13("SERR YBIR?") ) ##should decode to FREE LOVE?
print(rot13("GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT.") ) ##should decode to THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.