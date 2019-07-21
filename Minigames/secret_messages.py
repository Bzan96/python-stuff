# To encrypt a word, replace each letter by the letter that comes 7 steps 
# after it. (adding 7)
# HELLO becomes OLSSV
# To decrypt it, just reverse the procedure. (subtracting 7)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
newMsg = ""

key = int(input("Enter a number to use as your key (no decimals) ") )
msg = str.upper(input("Please enter a message: ") )

for character in msg:
	if character in alphabet:
		pos = alphabet.find(character)
		newPos = (pos + key) % 29
		newChar = alphabet[newPos]
		newMsg += newChar

	else:
		newChar = character
		newMsg += newChar
		
print("The new character is " + newMsg )