"""
Generator expressions ("genexps") are like list comprehensions,
except that where listcomps are greedy, generator expressions are lazy.

Listcomps compute the entire result list all at once, as a list.

Generator expressions compute one value at a time, when needed, as individual values.
This is especially useful for long sequences where the computed list
is just an intermediate step and not the final result.
"""


# As a loop
total = 0
for num in range(1, 101):
    total += num * num
print(total)


# As a list comprehension
total = sum([num * num for num in range(1, 1001)])
print(total)


# As a generator expression
total = sum(num * num for num in range(1, 10001))
print(total)
