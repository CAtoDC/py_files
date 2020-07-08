'''
Password Generator
Combines letters, punctuation and digits; then randomly
joins as few or as many as designated in range
'''

import string
from random import *

punct = '!@#$%^&*+=?|~'

characters = string.ascii_letters + string.digits + punct
password =  "".join(choice(characters) for x in range(randint(8, 9)))

print ("Your new password is: " + password)
