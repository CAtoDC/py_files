"""
List Comprehensions and Generator Expressions
"""

# Old way
result = []
for i in range(10):
	s = i**2
	result.append(s)
print sum(result)


# Pythonic
print sum(i**2 for i in xrange(10))	# Taking out the brackets creates a generator version
																		# which makes things go faster
