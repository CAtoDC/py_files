'''
Use a for Loop to cycle through a list of lists

Each row is a list of values.
Each value represents a cell.
The reader object can be looped over only once.

For python 2x, use IOError
'''

import csv

try:
    exampleFile = open('data/names.csv')
    exampleReader = csv.reader(exampleFile)
# use this in python 2x    
#except IOError as (errno, strerror):
        #print("I/O error({0}): {1}".format(errno, strerror))
        #exit()
except OSError as e:
    print (e)
    exit()

# loop through all rows
for row in exampleReader:
    print ('Row #' + str(exampleReader.line_num) + ' ' + str(row))
