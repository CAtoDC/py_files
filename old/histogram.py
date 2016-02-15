'''
The name of the function is histogram, which is a statistical term for
a set of counters (or frequencies).

Here, we're getting the frequency (and counts) to letters in a word.
'''

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    return d

# since it's a dict(), it is unsorted by default
def print_hist(h):
    for c in h:
        print (c, h[c])

# but we can force a sort
def print_sorted_hist(h):
    lst = h.keys()
    sorted(lst)
    for c in lst:
        print (c, h[c])

# test it
h = histogram('parrot')
print ('Unsorted: \n', print_hist(h))
print ('\n')
print ('Sorted: \n', print_sorted_hist(h))
