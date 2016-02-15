"""
Updating Sequences
"""

names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']


# All these are very slow
del names[0]
names.pop(0)
names.insert(0, 'mark')


# Use this
names = deque(['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie'])
