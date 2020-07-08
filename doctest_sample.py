import doctest
'''
YouTube:  Albert Sweigart, "Logging and Testing and Debugging, Oh My!", PyBay2017

The simple addition of doctest allows us to actually run
the code from our doc string - as a test.

Kind of a unit test for the documentation.
'''

def addTwoNumbers(x, y):
    '''
    Returns the sum of x and y.

    >>> addTwoNumbers(2, 2)
    5
    >>> addTwoNumbers(3, 6)
    9
    '''
    return int(x) + int(y)

doctest.testmod()
