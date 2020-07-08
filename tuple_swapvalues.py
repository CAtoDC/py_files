"""
Swap values

The right-hand side is unpacked into the names of the tuple on the left-hand side
The comma is the tuple constructor syntax
"""


a = 5
b = 6

print ('a is', a, 'and b is', b)

# swap values
b, a = a, b	

print ('a is now', a, 'and b is now', b)