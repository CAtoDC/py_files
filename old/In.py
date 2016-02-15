"""
Use "in" wherever possible
"""

# Bad
for key in d.keys():
    print key

# Good
for key in d:
    print key

# but .keys() is necessary when mutating a dictionary
# do this:
if key in d:
    # ... do something with d[key]
# not this:
if d.has_key(key):
    #... do something with d[key]
