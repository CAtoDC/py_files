'''Storing and retrieving dictionary info'''

# storing
d = {}	# define the dict

# add key/value pairs
d['a'] = 'alpha'
d['o'] = 'omega'
d['g'] = 'gamma'

# lookup
print ("The value of 'a' is:", d['a'])

# alternative lookup
print ("Another way to get the value of 'a':", d.get('a'))

# determing whether value is IN dictionary
print ("Assertion: the key 'a' is in the dict:", 'a' in d)
