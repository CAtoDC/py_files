"""
Unpacking sequences
"""

p = 'Mark', 'Cuevas', 0x35, 'python@example.com'

# Pythonic
fname, lname, age, email = p
print (fname, lname, '-', age, '-', email)
