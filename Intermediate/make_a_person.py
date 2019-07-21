'''
Fill in the object constructor with the following methods below:

    getFirstName() getLastName() getFullName()
	setFirstName(first) setLastName(last) setFullName(firstAndLast)

Run the tests to see the expected output for each method.

The methods that take an argument must accept only one argument and it has
to be a string.

These methods must be the only available means of interacting with the object.
'''

class Person:
	def __init__(self, firstAndLast):
		self.firstAndLast = firstAndLast
		
	def setFullName(self, fullName):
		self.firstAndLast = fullName
		
	def setFirstName(self, first):
		self.firstAndLast = first + " " + self.firstAndLast.split(" ")[1]
	
	def setLastName(self, last):
		self.firstAndLast = self.firstAndLast.split(" ")[0] + " " + last
		
	def getFullName(self):
		return self.firstAndLast
	
	def getFirstName(self):
		return self.firstAndLast.split(" ")[0]
		
	def getLastName(self):
		return self.firstAndLast.split(" ")[1]
	
bob = Person("Bob Ross")

#bob.setFirstName("Haskell")
#bob.setLastName("Curry")
bob.setFullName("Haskell Curry")

try:
	count = -1 # Because it counts the "method" created in the __init__()
	for method in dir(bob):
		if not method[0] == "_":
			count += 1
	print(count) ##should return 6.
	print(isinstance(bob, Person) ) ##should return True.
	#print(bob.firstName ) ##should return None.
	#print(bob.lastName ) ##should return None.
	print(bob.getFirstName() ) ##should return "Bob".
	print(bob.getLastName() ) ##should return "Ross".
	print(bob.getFullName() ) ##should return "Bob Ross".
	print(bob.getFullName() ) ##should return "Haskell Ross" after bob.setFirstName("Haskell").
	print(bob.getFullName() ) ##should return "Haskell Curry" after bob.setLastName("Curry").
	print(bob.getFullName() ) ##should return "Haskell Curry" after bob.setFullName("Haskell Curry").
	print(bob.getFirstName() ) ##should return "Haskell" after bob.setFullName("Haskell Curry").
	print(bob.getLastName() ) ##should return "Curry" after bob.setFullName("Haskell Curry")
except AttributeError as e:
	print(e)
	print(None)