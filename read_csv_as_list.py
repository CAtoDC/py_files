'''
To read data from a csv file with the csv module,
you need to create a Reader object. A Reader object lets you
iterate over the lines in a csv file.

Using list() on this Reader object returns a list of lists,
which you can store in a variable.

Now that we have a csv file as a list of lists, we can access
a particular [row] or [col].

OSError is new in python 3x
'''

import csv, os

try:
    exampleFile = open('data/food_types.csv')
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
except OSError as e:
        print(e)
        exit()

# print a few examples
#print (exampleData)
print (exampleData[0][0])   # goes to first list and first string
print (exampleData[1][1])   # Apple
print (exampleData[2][1])   # Orange
