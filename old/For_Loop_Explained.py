# The For loop is really like a For Each loop
# It iterates over lists; but this is ugly and inefficient

for i in [0, 1, 2, 3, 4, 5, 6]:
	print (i **2)

# You can also use the range function
# which is functionally equivalent to the above, but prettier
for i in range(6):
	print (i **2)

# A better way:
# xrange produces an iterator over the range
# creating the values one-at-a-time
# This is much more efficient memory-wise
# In Python 3, "range" has the functionality that xrange has in Python 2
for i in range(6):
	print (i **3)

# A beautiful way to iterate a collection
colors = ['red', 'green', 'blue', 'yellow']
for color in colors:
	print (color)

# We can also go backwards
# But note that colors is in parenthesis here
colors = ['red', 'green', 'blue', 'yellow']
for color in reversed (colors):
	print (color)
