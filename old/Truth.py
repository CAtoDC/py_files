'''
Example to show how to control the truth value of 
instances of a user-defined class
'''

class MyContainer(object):     

# To control the truth value of instances of a user-defined class,
# use the __nonzero__ or __len__ special methods.
# Use __len__ if your class is a container which has length.

    def __init__(self, data):  
        self.data = data       
                                      
    def __len__(self):         
        """Return my length."""
        return len(self.data)

a = MyContainer([])
print 'object a:'
print '  data   =', a.data
print '  length =', len(a)
print '  truth  =', bool(a)
print

b = MyContainer([1,2,3])
print 'object b:'
print '  data   =', b.data
print '  length =', len(b)
print '  truth  =', bool(b)
print


class MyClass(object):

    def __init__(self, value):
        self.value = value

    def __nonzero__(self):
        """Return my truth value (True or False)."""
        # This could be arbitrarily complex:
        return bool(self.value)

    # Python 3 compatibility:
    __bool__ = __nonzero__

c = MyClass(0)
print 'object c:'
print '  value =', c.value
print '  truth =', bool(c)
print

d = MyClass(3.14)
print 'object d:'
print '  value =', d.value
print '  truth =', bool(d)
print