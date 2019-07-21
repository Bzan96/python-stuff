'''
Check if a string (first argument, str) ends with the given target string
(second argument, target).
This challenge can be solved with the .endsWith() method, which was introduced
in ES2015. But for the purpose of this challenge, we would like you to use one 
of the JavaScript substring methods instead.
'''

# Python also as a str.endswith() function, but I'll bypass that here.

def confirmEnding(str, target):
	if(str.find(target, len(str)-len(target) ) != -1):
		return True
	else:
		return False

		

print(confirmEnding("Bastian", "n") )
print(confirmEnding("Congratulation", "on") )
print(confirmEnding("Connor", "n") )
print(confirmEnding("Walking on water and developing software from a specification are easy if both are frozen", "specification") )
print(confirmEnding("He has to give me a new name", "name") )
print(confirmEnding("Open sesame", "same") )
print(confirmEnding("Open sesame", "pen") )
print(confirmEnding("Open sesame", "game") )
print(confirmEnding("If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing", "mountain") )
print(confirmEnding("Abstraction", "action") )