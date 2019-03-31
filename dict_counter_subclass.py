'''Find the ten most common words in Alice In Wonderland'''

# A Counter is a dict subclass for counting hashable objects.
# It's an unordered collection where elements are stored as dictionary
# keys and their counts are stored as dictionary values.
# Counts are allowed to be any integer value including zero or negative counts.

# The Counter class is similar to bags or multisets in other languages.

from collections import Counter
import re

words = re.findall(r'\w+', open('c:/py/sample_text/AliceInWonderland.txt').read().lower())
print (Counter(words).most_common(10))
