"""
Truth testing
"""

# Testing for boolean truth values
x = True

# Bad
if x == True:
	print 'x is true.'

# Good
if x:
	print 'Yup, x is true.'


# Testing for list truth values
names = ['John', 'Michael']
# Bad
if len(names) != 0:
	pass

# Also bad
if names != []:
	pass

# Good
if names:
	print names