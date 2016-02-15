# findall string pattern - split into tuples

# Regular expression module
import re

# Simple matching: \d+ means match one or more digits
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

text = 'Today is 11/27/2012. Pycon starts 3/13/2013.'

print (datepat.findall(text))

# print using format
for month, day, year in datepat.findall(text):
	print ('{}-{}-{}'.format(year, month, day))
