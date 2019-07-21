def convertToRoman(num):
	numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
	numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	
	paraNum = num
	roman = ""
	
	for i in range(len(numbers) ):
		while(paraNum-numbers[i] >= 0):
			roman += numerals[i]
			paraNum -= numbers[i]
			
	return roman
	


print(convertToRoman(2) ) ##should return "II".
print(convertToRoman(3) ) ##should return "III".
print(convertToRoman(4) ) ##should return "IV".
print(convertToRoman(5) ) ##should return "V".
print(convertToRoman(9) ) ##should return "IX".
print(convertToRoman(12) ) ##should return "XII".
print(convertToRoman(16) ) ##should return "XVI".
print(convertToRoman(29) ) ##should return "XXIX".
print(convertToRoman(44) ) ##should return "XLIV".
print(convertToRoman(45) ) ##should return "XLV"
print(convertToRoman(68) ) ##should return "LXVIII"
print(convertToRoman(83) ) ##should return "LXXXIII"
print(convertToRoman(97) ) ##should return "XCVII"
print(convertToRoman(99) ) ##should return "XCIX"
print(convertToRoman(400) ) ##should return "CD"
print(convertToRoman(500) ) ##should return "D"
print(convertToRoman(501) ) ##should return "DI"
print(convertToRoman(649) ) ##should return "DCXLIX"
print(convertToRoman(798) ) ##should return "DCCXCVIII"
print(convertToRoman(891) ) ##should return "DCCCXCI"
print(convertToRoman(1000) ) ##should return "M"
print(convertToRoman(1004) ) ##should return "MIV"
print(convertToRoman(1006) ) ##should return "MVI"
print(convertToRoman(1023) ) ##should return "MXXIII"
print(convertToRoman(2014) ) ##should return "MMXIV"
print(convertToRoman(3999) ) ##should return "MMMCMXCIX"