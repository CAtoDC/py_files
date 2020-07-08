'''Solution to Fizz Buzz problem

If a number is divisible by 3, print Fizz.
If a number is divisible by 5, print Buzz.
If a number is divisible by both 3 and 5, print FizzBuzz.

For python 2x, use xrange
'''

for num in range(1, 101):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
