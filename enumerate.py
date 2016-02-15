"""
The enumerate function takes a list and returns (index, item) pairs
"""

# We need to use a 'list' wrapper because enumerate
# only generates one item, a pair at a time - and only when required.
# The enumerate function is a generator function.
# A 'for' loop takes one result at a time, but the print function does not
# so we need to explicitly convert the generator function when we print

items = 'zero one two three'.split()
print("Print items using split: ", list(enumerate(items)),'\n')

# using a for loop
print('Index and items using a for loop')
for (index, item) in enumerate(items):
	print(index, '-->', item)
