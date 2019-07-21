'''
Convert the characters &, <, >, " (double quote), and ' (apostrophe), in a
string to their corresponding HTML entities.
'''

import html
#Schindler's List works, but doesn't return the same in Python and JavaScript

def convertHTML(str):
	newStr = ""
	
	for i in str:
		if(i == "&"):
			i = i.replace(i, html.escape("&") )
		elif(i == "<"):
			i = i.replace(i, html.escape("<") )
		elif(i == ">"):
			i = i.replace(i, html.escape(">") )
		elif(i == "'"):
			i = i.replace(i, html.escape("'") )
		elif(i == '"'):
			i = i.replace(i, html.escape('"') )
			
		newStr += i
	
	return newStr

	

print(convertHTML("Dolce & Gabbana") )
##should return Dolce &​amp; Gabbana
print(convertHTML("Hamburgers < Pizza < Tacos") )
##should return Hamburgers &​lt; Pizza &​lt; Tacos
print(convertHTML("Sixty > twelve") )
##should return Sixty &​gt; twelve
print(convertHTML('Stuff in "quotation marks"') )
##should return Stuff in &​quot;quotation marks&​quot;
print(convertHTML("Schindler's List") )
##should return Schindler&​apos;s List
##NOTE: This doesn't return &apos; because instead it is converted to &#x27; which is still 
## valid HTML (instead of XML actually). html.unescape("&#x27;") still returns an apostrophe.
print(convertHTML("<>") )
##should return &​lt;&​gt;
print(convertHTML("abc") )
##should return abc