'''Streamlined version of Powerball Number Generator

For python 2x, use xrange
'''
import random

# set number of tickets
tickets = 5

print ('Powerball Number Generator', '\n')

for i in range (tickets):
    five = random.sample(range(1, 69),5)
    one = random.sample(range(1, 29), 1)
    print (five, '\t', one)
