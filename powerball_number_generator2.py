import random

tickets = 5

print 'Powerball Number Generator'
for i in xrange(tickets):
    five = random.sample(xrange(1, 69),5)
    one = random.sample(xrange(1, 29), 1)
    print five, one
