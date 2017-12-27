"""
Unpacking sequences
"""

p = 'Mark', 'Cuevas', 0x37, 'python@example.com'

# Pythonic
fname, lname, age, email = p
print (fname, lname, '-', age, '-', email)
