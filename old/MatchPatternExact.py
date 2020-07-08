# Match a string pattern

# Regular expression module
import re

# Simple matching: \d+ means match one or more digits
# $ matches exactly
# r is Regular Expression
datepat = re.compile(r'\d+$/\d+$/\d+$')

text1 = '11abc/27/2012'
text2 = 'Nov 27, 2012'

print("Text 1: ", text1)
print("Text 2: ", text2,'\n')

# match always tries to find the match at
# the start of the string
if datepat.match(text1):
	print ('text1 is an exact match')
else:
	print ('text1 is not an exact match')
	
if datepat.match(text2):
	print('text2 is an exact match')
else:
	print('text2 is not an exact match')
