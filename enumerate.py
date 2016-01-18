"""
The enumerate function takes a list and returns (index, item) pairs
"""

# We need to use a 'list' wrapper because enumerate
# only generates one item, a pair at a time - and only when required.
# The enumerate function is a generator function.
# A 'for' loop takes one result at a time, but the print function does not
# so we need to explicitly convert the generator function when we print
items = 'zero one two three'.split()
print "Printing items with split: ", list(enumerate(items))

# It's simpler if we use a For loop
for (index, item) in enumerate(items):
	print index, '-->', item
