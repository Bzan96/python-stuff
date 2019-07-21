alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
oldMsg = ""

key = int(input("Enter a number to use as your key (no decimals) ") )
msg = str.upper(input("Please enter a message: ") )

for character in msg:
	if character in alphabet:
		pos = alphabet.find(character)
		oldPos = (pos - key) % 29
		oldChar = alphabet[oldPos]
		oldMsg += oldChar

	else:
		oldChar = character
		oldMsg += oldChar
		
print("The new character is " + oldMsg )