"""
findall string pattern
"""

# Regular expression module
import re

# Simple matching: \d+ means match one or more digits
date_pattern = re.compile(r'\d+/\d+/\d+')

text1 = 'This file was created on 11/27/2012. Pycon starts 3/13/2013.'
text2 = 'Today is August first.'

# findall finds all occurrences of a pattern
# within a string
if date_pattern.findall(text1):
	print(text1)
else:
	print('No digit pattern found.')