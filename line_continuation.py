"""
Parentheses allow implicit line continuation.
Although the \ is allowed for line continuation, it's ugly.
"""

text = ('Long strings can be made up '
        'of several shorter strings. '
        'Even whole paragraphs can be '
        'written!')
print (text)


# An even better way
text2 = '''
This is free form text. I can break the lines
where ever I like
in code
and they will print that way.
'''
print(text2)
