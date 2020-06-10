# set up a range of numbers to use
nums = range(10)
#print nums


# LISTS
# List even numbers
evens = []
for num in nums:
    # if dividing by 2 results in no remainder, then it's even
    if(num % 2 == 0):
        # add it to the list
        evens.append(num)
print (evens)


# List odd numbers
odds = []
for num in nums:
    if(num % 2 != 0):
        odds.append(num)
print (odds)


# List Comprehension
my_list = []
my_list = nums  # range of nums is now a list
squares = [num*num for num in my_list]
print (type(squares), "-->", squares)


