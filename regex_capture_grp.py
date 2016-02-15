'''findall string pattern'''

# Regular expression module
import re

# Simple matching: \d+ means match one or more digits
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')

# Reg Ex capture groups encloses parts of a pattern in parenthesis
# This allows the contents to be extracted individually
print (m.group(0))
print (m.group(1))
print (m.group(2))
print (m.group(3))
print (m.groups())
month, day, year = m.groups()
