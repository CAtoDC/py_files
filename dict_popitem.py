"""
Dictionary PopItems

Another way to iterate through a dictionary
"""

# popitem removes an arbitrary item
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

while d:
	key, value = d.popitem()
	print (key, '-->', value)
