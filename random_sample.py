'''Generates a list of n random numbers in the
range of 0 to n without repetition'''

import random

random_list = []
random_list = random.sample(range(1000), 5)
print(sorted(random_list))
