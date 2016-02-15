

def square_numbers(nums):
    ''' traditional way - no generator'''
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1, 2, 3, 4, 5])

print('My list of nums:', my_nums, "\n")



def square_numbers(nums):
    ''' as a generator '''
    for i in nums:
        yield (i*i)  # returns one-at-a-time
        
my_nums = square_numbers([5, 4, 3, 2, 1])

for num in my_nums:
    print (num,)



my_nums = (x*x for x in [5, 6, 7, 8, 9])
''' generator (like a list comprehension) but
uses parens instead of brackets'''

print ('\n',)

for num in my_nums:
    print (num)
