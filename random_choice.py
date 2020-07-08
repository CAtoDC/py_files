from random import choice

# heads or tails
print (choice(['heads', 'tails']))

# choice from 1 to 10
t = choice(range(1,10))
print(t)


# betting game
num_flips = 100
total = 0
i = 1

while i <= num_flips:
    # This is the bet; -10 or +20
    bet = choice([-10,20])

    # Add to the total
    total = total + bet

    # Increment the counter - goes up to num_files
    i = i + 1

print(total)
