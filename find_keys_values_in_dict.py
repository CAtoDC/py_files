# Find keys, values in dict

d = {}	# define the dictionary

# add key, value pairs
d['a'] = 'alpha'
d['o'] = 'omega'
d['g'] = 'gamma'


# Find the keys
print("Keys: ", d.keys(),'\n')

# Find the values
print("Values: ", d.values())

# Loop over keys, values
print("\nLoop over key/value pairs: ")
for k in sorted(d.keys()):	# sorted is necessary to get alpha order; otherwise random, as hashed
	print(k, '-->', d[k])

# Pulling out key, value pairs (tuples)
print("\nPrint key/value tuples: ", d.items())

# Another way to get tuples
print("\nAnother way to get tuples: ")
for tuple in d.items():
	print (tuple)
