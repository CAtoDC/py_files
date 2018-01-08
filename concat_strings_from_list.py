"""
Concatenating Strings from a list using join
"""

names = (['raymond', 'rachel', 'matthew', 'roger', 'betty',
					'melissa', 'judith', 'charlie'])

# Pythonic
# The join() method does all the copying in one pass


# If you want spaces between the substrings
result = ' '.join(names)
print('With spaces between names:', result, '\n')


# If you want commas and spaces
result = ', '.join(names)
print('With commas and spaces between names: ', result, '\n')


# To make a grammatically nice sentence (using "or" before the last word) we can use slice.
# The ([:-1]) gives all but the last value.
print('Grammtically correct - Choose:', ', '.join(names[:-1]), 'or', names[-1])
