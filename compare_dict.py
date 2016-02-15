'''Comparing dictionary key/value pairs'''

a = {
    'a' : 5,
	'x' : 1,
	'y' : 2,
	'z' : 3
}


b = {
	'w' : 10,
	'x' : 11,
	'z' : 2,
    'a' : 5
}

# Find keys in common
print('Keys that a and b have in common:', a.keys() & b.keys()) 	#  x, z, a

# Find keys in "a" that are not in "b"
print('Keys in a that are not in b:', a.keys() - b.keys())		#  y

# Find (key, value) pairs in common
print('Key/value pairs in common:', a.items() & b.items())	#  a --> 5
