'''
Password Generator
Combines letters, punctuation and digits; then randomly
joins as few or as many as designated in range
'''

import string
from random import *

punct = '!@#$%^&*+=?|~'

characters = string.ascii_letters + string.digits + punct  # string.punctuation
password =  "".join(choice(characters) for x in range(randint(8, 10)))

print ("Your new password is: " + password)
