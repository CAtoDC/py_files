"""
Use split on text
"""

# A quick way to get a list of words
words = 'Now is the time for all good men to come to the aid of their country'.split()
# print (words)

# Iterate over them and add an item number before each word
i = 0
for word in words:
	print (i, word )
	i += 1
