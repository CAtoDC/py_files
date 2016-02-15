'''Fibonacci sequence solved with a generator.
Very efficient - yield processes one-at-a-time

For python 2x, use xrange
'''
def fib(num):
    a, b = 0, 1
    for i in range(0, num):
        # print the count of each item and its fibonacci number
        #yield "{}: {}".format(i + 1, a)
        yield (a)
        a, b = b, a + b

for item in fib(10):
    print(item)
