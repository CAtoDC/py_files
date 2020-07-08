"""
Counting with dictionaries
"""

colors = ['red', 'green', 'red', 'blue', 'green', 'red']

# count number of item occurrences
d = {}
for color in colors:
	# if color is not found, 0; otherwise 1
	d[color] = d.get(color, 0) + 1
print(d)
