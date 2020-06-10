'''This is an example of a recursive algorithm.
It's being used to compute any factorial.'''

def getFactorial(n):
    if n < 2:
        return 1
    else:
        return n * getFactorial(n-1)

print (getFactorial(5))

