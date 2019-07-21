name1 = input("Enter the name of the first person: ")
name2 = input("Enter the name of the second person: ")
names = name1 + name2
score = 0

for character in names:
	if character in "aouåeiyäö":
		score += 7
	
	elif character in "bcdfghjklmnpqrstvwxz":
		score += 4
		
if (score % 7) > 3:
	print("You are lovers!")
	
elif (score % 7) > 2:
	print("You are best friends!")
	
elif (score % 7) > 1:
	print("You are slightly friendly.")
	
else:
	print("You don't like each other.")