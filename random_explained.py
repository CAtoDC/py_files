import random

# random is a module
print random


# The function random returns a random float between 0.0 and 1.0
# (including 0.0 but not 1.0)
for i in range(10):
    x = random.random()
    print x


# The function randint takes parameters low and high and
# returns an integer between low and high (including both)
x = random.randint(1, 20)
print(x)


# To choose an element from a sequence at random, you can use choice
t = [1, 2, 3, 'a', 'b', 'c']
print random.choice(t)
