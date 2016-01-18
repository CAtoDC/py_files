from collections import Counter


'''
Common patterns for working with Counter objects:

sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
'''

c = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    c[word] += 1

# prints words and num occurrences in list
print 'Items and number of occurrences in list:', c

# print list of items
print 'Items and values in list:', c.items()

# print least common item(s)
print 'Least common items:', c.most_common()[:-2-1:-1]

# prints unique list
print 'Unique list items:', list(c)

# total num of items in list
print 'Total number of items in list:', sum(c.values())
