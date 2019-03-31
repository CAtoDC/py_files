"""
Iterating through dictionaries

For python 2x, use iteritems()
"""

# create dict (i.e., key/value pairs)
my_dict = {'name': 'Wasabi', 'age': '4', 'occupation': "Mark's Dog"}

# Loop over keys and values using items
for key, val in my_dict.items():	# items will return an iterator
	print("My {} is {}.".format(key, val))
