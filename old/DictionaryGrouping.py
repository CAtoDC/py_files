"""
Grouping with dictionaries

"""

import collections

names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']


#Python 3.x
d = collections.defaultdict(list)
for name in names:
	key = len(name)
	d[key].append(name)

print(names)