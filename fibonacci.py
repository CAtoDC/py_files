'''
One solution to the fibonacci sequence
Print out a number.
The next number is a result of the previous two added together.

For python 2x, use xrange
'''
a, b = 0, 1
for i in range(0, 10):
    print (a)
    a, b = b, a + b
