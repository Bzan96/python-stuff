import re

def telephoneCheck(str):
	regex = r"^(1\s?)?(\(\d{3}\)|(\d{3}))[\-\s]?(\d{3})[\-\s]?(\d{4})$"
	
	if(re.match(regex, str) ):
		return True
	else:
		return False
		


print(telephoneCheck("1 555-555-5555") ) ##should return true.
print(telephoneCheck("1 (555) 555-5555") ) ##should return true.
print(telephoneCheck("5555555555") ) ##should return true.
print(telephoneCheck("555-555-5555") ) ##should return true.
print(telephoneCheck("(555)555-5555") ) ##should return true.
print(telephoneCheck("1(555)555-5555") ) ##should return true.
print(telephoneCheck("555-5555") ) ##should return false.
print(telephoneCheck("5555555") ) ##should return false.
print(telephoneCheck("1 555)555-5555") ) ##should return false.
print(telephoneCheck("1 555 555 5555") ) ##should return true.
print(telephoneCheck("1 456 789 4444") ) ##should return true.
print(telephoneCheck("123**&!!asdf#") ) ##should return false.
print(telephoneCheck("55555555") ) ##should return false.
print(telephoneCheck("(6054756961)") ) ##should return false
print(telephoneCheck("2 (757) 622-7382") ) ##should return false.
print(telephoneCheck("0 (757) 622-7382") ) ##should return false.
print(telephoneCheck("-1 (757) 622-7382") ) ##should return false
print(telephoneCheck("2 757 622-7382") ) ##should return false.
print(telephoneCheck("10 (757) 622-7382") ) ##should return false.
print(telephoneCheck("27576227382") ) ##should return false.
print(telephoneCheck("(275)76227382") ) ##should return false.
print(telephoneCheck("2(757)6227382") ) ##should return false.
print(telephoneCheck("2(757)622-7382") ) ##should return false.
print(telephoneCheck("555)-555-5555") ) ##should return false.
print(telephoneCheck("(555-555-5555") ) ##should return false.
print(telephoneCheck("(555)5(55?)-5555") ) ##should return false.