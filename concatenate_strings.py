"""
Building Strings, Variations 2
"""

# Bad. This involves a generator expression.
#result = ''.join(fn(i) for i in items)

# Good. Accumulate the list first, then apply the join() method, for efficiency.
items = ['a', 'b', 'c']
#...
items.append(items)	# many times
#...
# items is now complete
result = ''.join(fn(i) for i in items)
