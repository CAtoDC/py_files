"""
Dictionaries
"""

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

# iterate over dict and print out key values
for k in d:
	print k
print '\n'

# Looping over keys and values and print both
for k, v in d.iteritems():	# iteritems will return an iterator
	print k, '-->', v
