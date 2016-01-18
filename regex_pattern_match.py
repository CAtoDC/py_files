# Match a string pattern

# Regular expression module
import re

# Simple matching: \d+ means match one or more digits
datepat = re.compile(r'\d+/\d+/\d+')

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

# match always tries to find the match at
# the start of the string
if datepat.match(text1):
	print('text1 is a match')
else:
	print('no')
