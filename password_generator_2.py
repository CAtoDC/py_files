'''
Password Generator
Combines letters, punctuation and digits, then
randomly joins as few or as many as designated in range
'''

import string

from random import *
characters = string.ascii_letters + string.punctuation + string.digits
password =  "".join(choice(characters) for x in range(randint(7, 8)))

print ("Your new password is: " + password)
