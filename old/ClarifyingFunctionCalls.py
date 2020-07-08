"""
Best Practices

Clarify function calls with keyword arguments
"""

# Bad
twitter_search('@obama', False, 20, True)

# Good
twitter_search('@obama', retweets=False, numtweets=20, popular=True)


# Clarify multiple return values with named tuples

# This is terrible
doctest.testmod()
(0, 4)

# This is much better
doctest.testmod()
TestResults(failed=0, attempted=4)

# And this is Pythonic
TestResults = namedtuple('TestResults', ['failed', 'attempted'])
